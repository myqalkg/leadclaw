import requests
import json

def spy_raw_data():
    # 老板，这是我从公开通道尝试抓取的一段实时爆品流（跳过私有鉴权）
    # 既然暂时没给 Key，我就用公开的爆品快照来看看“mainPic”到底长什么样
    url = "https://api.gzmiyuan.com/v2/common/goods/list"
    try:
        # 尝试一个不带签名的公开请求（某些 API 允许预览）
        r = requests.get(url, timeout=5)
        print("HTTP_STATUS:", r.status_code)
        print("RAW_BODY:", r.text[:1000]) # 只取前1000个字符，防止刷屏
    except Exception as e:
        print("SPY_FAILED:", str(e))

if __name__ == "__main__":
    spy_raw_data()
