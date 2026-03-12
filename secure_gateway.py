import http.server, ssl, os, json

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def start():
    # 路径锁定
    os.chdir("/home/admin/.openclaw/workspace/lead-claw/")
    httpd = http.server.HTTPServer(('0.0.0.0', 443), Handler)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(
        certfile="/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.pem",
        keyfile="/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.key"
    )
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    print("ONLINE::SECURE_SERVER_LIVE")
    httpd.serve_forever()

if __name__ == "__main__":
    start()
