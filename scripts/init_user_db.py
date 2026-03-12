import sqlite3
DB_PATH = "/home/admin/.openclaw/workspace/lead-claw/leadclaw_user.db"

def upgrade_system():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    # 创建用户表
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (openid TEXT PRIMARY KEY, 
                  nickname TEXT, 
                  avatar_url TEXT,
                  last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()
    print("Database: User Identity Table DEPLOYED.")

upgrade_system()
