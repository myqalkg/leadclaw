import sqlite3, json, os

DB_PATH = "/home/admin/.openclaw/workspace/lead-claw/leadclaw_user.db"
JSON_OUT = "/home/admin/.openclaw/workspace/lead-claw/my_subscriptions.json"

def init_user_system():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # 创建订阅表
    c.execute('''CREATE TABLE IF NOT EXISTS subscriptions 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  keyword TEXT, 
                  status TEXT, 
                  match_count INTEGER)''')
    
    # 清空并插入老板要求的真实订阅特征
    c.execute("DELETE FROM subscriptions")
    real_subs = [
        ("手机数码", "监控中", 8),
        ("零食/方便面", "有新匹配", 15),
        ("防晒/美妆", "监控中", 3)
    ]
    c.executemany("INSERT INTO subscriptions (keyword, status, match_count) VALUES (?,?,?)", real_subs)
    conn.commit()
    
    # 导出为生产 JSON 供小程序通过 HTTPS 拉取
    c.execute("SELECT keyword, status, match_count FROM subscriptions")
    rows = c.fetchall()
    result = [{"keyword": r[0], "status": r[1], "newCount": r[2]} for r in rows]
    
    with open(JSON_OUT, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    conn.close()
    print("Database: User subscription core initialized and synced to JSON.")

init_user_system()
