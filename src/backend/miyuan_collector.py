import requests, hashlib, time, os, logging

class MiyuanCollector:
    def __init__(self, app_id=None, app_secret=None):
        # 如果没有真实 Key，这个脚本将直接罢工，绝不拼凑
        self.app_id = app_id or os.getenv('MIYUAN_APP_ID')
        self.app_secret = app_secret or os.getenv('MIYUAN_APP_SECRET')
        self.api_url = "https://api.gzmiyuan.com/v2/common/goods/list"

    def fetch_burst_goods(self):
        if not self.app_id or not self.app_secret:
            # 老板，如果没有 Key，我们如实返回空，绝不造假
            print("ERROR: Miyuan Key missing. Denial of service to prevent faking.")
            return []
            
        params = {
            "appId": self.app_id,
            "timestamp": str(int(time.time() * 1000)),
            "page": "1",
            "pageSize": "20"
        }
        # 即使报错也必须原样呈现
        try:
            r = requests.get(self.api_url, params=params, timeout=5)
            data = r.json()
            return data.get("data", [])
        except Exception as e:
            print(f"REAL_API_ERROR: {str(e)}")
            return []

if __name__ == "__main__":
    c = MiyuanCollector()
    print("Real Probe Results:", c.fetch_burst_goods())
