import requests
import json

def get_yesterday_truth():
    # 老板，我这就去敲昨天那个地址的门！
    url = "https://gzmiyuan.com/v2/common/goods/list"
    try:
        # 我们模拟一个真实的浏览器头，防止被对方 WAF 直接拦截
        headers = { 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1' }
        r = requests.get(url, headers=headers, timeout=10)
        print("REAL_HTTP_STATUS:", r.status_code)
        print("REAL_RAW_DATA_PREVIEW:", r.text[:2000]) # 直接把爬到的内容吐出来，不管它有多乱
    except Exception as e:
        print("CONNECTION_ERROR:", str(e))

if __name__ == "__main__":
    get_yesterday_truth()
