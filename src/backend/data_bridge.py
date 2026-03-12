import json
import os
import time
import logging

# 路径配置文件
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SHARED_DATA_PATH = os.path.join(BASE_DIR, 'src/shared/burst_items.json')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - [Lead-Claw Bridge] - %(message)s')

class DataBridge:
    """
    负责将后台扫描到的爆品数据(JSON)同步至前端预览层
    """
    def __init__(self):
        self.ensure_shared_dir()

    def ensure_shared_dir(self):
        shared_dir = os.path.dirname(SHARED_DATA_PATH)
        if not os.path.exists(shared_dir):
            os.makedirs(shared_dir)
            logging.info(f"Created shared directory: {shared_dir}")

    def sync_to_frontend(self, items):
        """
        按照 V5.5 设计规范格式化并写入 JSON
        """
        formatted_data = []
        for i, item in enumerate(items):
            # 字段对齐 SOP_V1.0.md
            formatted_data.append({
                "id": i + 1,
                "title": item.get('title', '未知商品'),
                "price": item.get('price', 0),
                "old": item.get('original', 0),
                "score": item.get('score', 0),
                "tag": item.get('trend', '热销中'),
                "platform": item.get('platform', '淘宝')
            })

        try:
            with open(SHARED_DATA_PATH, 'w', encoding='utf-8') as f:
                json.dump(formatted_data, f, ensure_ascii=False, indent=2)
            logging.info(f"Successfully synced {len(formatted_data)} items to frontend JSON.")
        except Exception as e:
            logging.error(f"Sync failed: {str(e)}")

# 研发攻坚：模拟后端扫描后的数据推送
if __name__ == "__main__":
    bridge = DataBridge()
    # 模拟从 Hunter Engine 或 gzmiyuan.com API 拿到的原始数据
    mock_scan_results = [
        {"title": "Apple iPhone 15 Pro Max", "price": 6999, "original": 8999, "score": 98.4, "trend": "历史新低", "platform": "京东"},
        {"title": "三松大米 5kg 东北长粒香", "price": 9.9, "original": 49.0, "score": 92.1, "trend": "突发直降", "platform": "淘宝"},
        {"title": "乐扣乐扣水壶 1L", "price": 19.9, "original": 69.0, "score": 85.5, "trend": "今日热推", "platform": "拼多多"}
    ]
    
    bridge.sync_to_frontend(mock_scan_results)
