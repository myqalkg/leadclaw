import http.server, ssl, os

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def start():
    # 强制切换到数据目录
    os.chdir("/home/admin/.openclaw/workspace/lead-claw/")
    # 监听 8443 端口，普通用户即可发起
    server_address = ('0.0.0.0', 8443)
    httpd = http.server.HTTPServer(server_address, Handler)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(
        certfile="/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.pem",
        keyfile="/home/admin/.openclaw/workspace/lead-claw/opencloud-uat.gzmiyuan.com.key"
    )
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("STANDALONE_HTTPS_SUCCESS::LISTEN_ON_8443")
    httpd.serve_forever()

if __name__ == "__main__":
    start()
