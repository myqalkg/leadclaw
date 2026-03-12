import http.server
import ssl
import os

# 路径锁定
CERT_PEM = "/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.pem"
CERT_KEY = "/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.key"
JSON_DIR = "/home/admin/.openclaw/workspace/lead-claw/"

class SecureHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def run_secure_server():
    server_address = ('0.0.0.0', 443)
    httpd = http.server.HTTPServer(server_address, SecureHandler)
    
    # 注入负责人提供的证书
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=CERT_PEM, keyfile=CERT_KEY)
    
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print("🐾 Lead-Claw SECURE DATA SERVER IS LIVE ON 443 [HTTPS]")
    print(f"Server Root: {JSON_DIR}")
    
    os.chdir(JSON_DIR)
    httpd.serve_forever()

if __name__ == "__main__":
    run_secure_server()
