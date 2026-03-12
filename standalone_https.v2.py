import http.server, ssl, os

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()

def start():
    # 核心修正：绝对路径绑定
    base_dir = "/home/admin/.openclaw/workspace/lead-claw/"
    cert_path = os.path.join(base_dir, "opencloud-uat.gzmiyuan.com.pem")
    key_path = os.path.join(base_dir, "opencloud-uat.gzmiyuan.com.key")
    
    server_address = ('0.0.0.0', 8443)
    httpd = http.server.HTTPServer(server_address, Handler)
    
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile=cert_path, keyfile=key_path)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print("SUCCESS::PORT_8443_IS_ACTIVE")
    httpd.serve_forever()

if __name__ == "__main__":
    start()
