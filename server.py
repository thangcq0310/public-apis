#!/usr/bin/env python3
"""
Simple HTTP Server để phục vụ Public APIs Search
Chạy lệnh: python server.py
Rồi mở trình duyệt vào: http://localhost:8000
"""

from http.server import HTTPServer, SimpleHTTPRequestHandler
import os
import webbrowser
import time

class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Thêm CORS headers để cho phép tải file JSON
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

    def log_message(self, format, *args):
        # Format log thân thiện hơn
        print(f"[{self.log_date_time_string()}] {format % args}")

def run_server(port=8000):
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    
    print("=" * 60)
    print("🚀 Public APIs Search Server đang chạy!")
    print("=" * 60)
    print(f"📍 Địa chỉ: http://localhost:{port}")
    print(f"📂 Thư mục: {os.getcwd()}")
    print("=" * 60)
    print("💡 Tip: Nhấn Ctrl+C để dừng server")
    print("=" * 60)
    
    # Cố gắng mở trình duyệt tự động
    try:
        time.sleep(1)
        webbrowser.open(f'http://localhost:{port}/search_apis.html')
        print("✅ Đang mở trình duyệt...")
    except:
        print(f"⚠️  Vui lòng mở: http://localhost:{port}/search_apis.html")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server đã dừng.")
        httpd.server_close()

if __name__ == '__main__':
    run_server(8000)
