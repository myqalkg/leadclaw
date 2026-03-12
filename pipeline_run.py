import time
import logging
from src.backend.miyuan_collector import MiyuanCollector
from src.backend.data_bridge import DataBridge

# 配置全链路日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [Lead-Claw Pipeline] - %(message)s'
)

def run_pipeline():
    """
    Lead-Claw 全自动数据流水线 (SOP V1.0 研发实现)
    1. 从蜜源 API 采集爆品 (Collector)
    2. 计算神价指数 (Scoring)
    3. 同步至前端 JSON (Bridge)
    """
    collector = MiyuanCollector()
    bridge = DataBridge()

    logging.info("Step 1: Fetching raw burst data from Miyuan API...")
    raw_goods = collector.fetch_burst_goods()
    
    if not raw_goods:
        logging.error("No goods fetched from API. Pipeline suspended.")
        return

    logging.info(f"Step 2: Scoring {len(raw_goods)} items based on V5.5 algorithm...")
    processed_items = []
    for item in raw_goods:
        # 简单评分逻辑：(1 - 现价/原价) + 销量增量加权
        discount_rate = (1 - item['actualPrice'] / item['originPrice'])
        sales_weight = min(item['twoHourSales'] / 5000, 1.0)
        final_score = round((discount_rate * 0.6 + sales_weight * 0.4) * 100, 1)

        processed_items.append({
            "title": item['title'],
            "price": item['actualPrice'],
            "original": item['originPrice'],
            "score": final_score,
            "trend": "历史新低" if discount_rate > 0.5 else "爆款返现",
            "platform": "蜜源精选"
        })

    logging.info("Step 3: Syncing processed data to frontend shared path...")
    bridge.sync_to_frontend(processed_items)
    logging.info("Pipeline Cycle Completed. Frontend should auto-refresh in 10s.")

if __name__ == "__main__":
    print("🐾 LEAD-CLAW AUTOMATED PIPELINE v1.0")
    print("-------------------------------------")
    while True:
        run_pipeline()
        # 模拟生产环境频率：每 30 秒轮询一次 API 并更新看板
        time.sleep(30)
