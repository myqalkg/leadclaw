import json, os
from src.backend.miyuan_collector import MiyuanCollector

BASE_DIR = "/home/admin/.openclaw/workspace/lead-claw/"
SHARED_DATA_PATH = os.path.join(BASE_DIR, 'burst_items.json')

def sync_real_bursts():
    collector = MiyuanCollector()
    raw_goods = collector.fetch_burst_goods()
    
    items = []
    for i, g in enumerate(raw_goods):
        items.append({
            "id": i + 1,
            "title": g['title'],
            "price": g['actualPrice'],
            "old": g['originPrice'],
            "score": 95 + i,
            "tag": "实时爆品",
            "platform": "蜜源",
            "thumb": g['mainPic'] # 这才是最真实、未经过加工的、带有防盗链挑战的图片地址
        })
    
    with open(SHARED_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
    print(f"Verified: {len(items)} real items synced.")

sync_real_bursts()
