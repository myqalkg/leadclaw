import json

raw_data = [
    {
        "title": "【29.9选5件】薛记炒货 西梅香菇脆芒果干",
        "price": 59.8,
        "voucherPrice": 11.98,
        "picture": "https://img.alicdn.com/bao/uploaded/i2/2200754110802/O1CN011pvWIh1HnMlVqqDIk_!!4611686018427380050-0-item_pic.jpg_400x400.jpg",
        "saleToday": 21709,
        "save": 47.8
    },
    {
        "title": "MissWiss双面防晒帽女士夏季户外防紫外线",
        "price": 179.9,
        "voucherPrice": 19.9,
        "picture": "https://img.alicdn.com/bao/uploaded/O1CN01havQ061S7C4am1EQK_!!6000000002199-2-yinhe.png",
        "saleToday": 87614,
        "save": 160.0
    },
    {
        "title": "参半酵素牙膏氨基酸美白旗舰店",
        "price": 16.2,
        "voucherPrice": 16.2,
        "picture": "https://img.alicdn.com/bao/uploaded/O1CN014cqHzr1yBNOBPTrIH_!!6000000006540-0-yinhe.jpg",
        "saleToday": 13428,
        "save": 0
    },
    {
        "title": "维达抽纸110抽*5包 大包装超强韧性",
        "price": 13.6,
        "voucherPrice": 9.9,
        "picture": "https://img.alicdn.com/bao/uploaded/bao/upload/O1CN01SsyqaO1WEIG0HykmF_!!6000000002756-2-yinhe.png",
        "saleToday": 1693,
        "save": 3.7
    }
]

html_cards = ""
for item in raw_data:
    save_tag = f'<span class="bg-red-100 text-red-600 text-[6px] px-1 rounded">省¥{item["save"]}</span>' if item["save"] > 0 else ""
    html_cards += f'''
    <div class="bg-white rounded-xl shadow-sm border p-2 mb-1 h-fit">
        <div class="bg-gray-100 h-28 rounded-lg mb-2 overflow-hidden flex items-center justify-center">
            <img src="{item["picture"]}" class="w-full h-full object-cover">
        </div>
        <div class="text-[9px] font-bold truncate leading-tight h-5">{item["title"]}</div>
        <div class="text-[7px] text-gray-400 line-through">¥{item["price"]}</div>
        <div class="flex justify-between items-center mt-0.5">
            <span class="text-red-600 font-black text-xs">¥{item["voucherPrice"]}</span>
            {save_tag}
        </div>
        <div class="text-[7px] text-gray-400 mt-1">🔥 已抢 {item["saleToday"]} 件</div>
        <button class="w-full bg-red-600 text-white text-[9px] py-1.5 rounded-lg mt-2 font-bold shadow-sm">去捡漏</button>
    </div>
    '''

print(html_cards)
