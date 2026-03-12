import json, os
BASE_DIR = "/home/admin/.openclaw/workspace/lead-claw/"
SHARED_DATA_PATH = os.path.join(BASE_DIR, 'burst_items.json')

def run_self_hosted_img_test():
    # 采用我们服务器上 100% 能访问的图片 (虽然是我们的 Logo，但至少它必须能亮)
    self_url = "https://opencloud-uat.gzmiyuan.com/index.html" # 先由于 1.3.1 版代码限制，我们指向一个真实路径进行测试
    
    items = [
        {
            "id": 1, 
            "title": "自托管图片测试 (如果您能看到 Logo，说明链路彻底通了)", 
            "price": 0.01, "old": 100, "score": 99,
            "thumb": "https://www.baidu.com/img/flexible/logo/pc/result.png" # 第一张：用最稳的百度
        },
        {
            "id": 2, 
            "title": "百度高清源验证", 
            "price": 99, "old": 199, "score": 95,
            "thumb": "https://www.baidu.com/img/flexible/logo/pc/result.png"
        }
    ]
    with open(SHARED_DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(items, f, ensure_ascii=False, indent=2)

run_self_hosted_img_test()
