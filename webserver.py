# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == "/sky.jpg"):
            self.send_response(200)
            self.send_header("Content-type", "image/jpg")
            self.end_headers()

            file = open("C:/Users/l.hefti/Desktop/test-ef5/sky.jpg", "rb")
            content = file.read()
            #print("test")
            self.wfile.write(bytes(content))

        if (self.path == "/example"):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            print(self.path)
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
            self.wfile.write(bytes("<img src=/sky.jpg alt=Flowers style=width:50vw;>", "utf-8"))
            self.wfile.write(bytes("<script></script>"))

        if (self.path == "/favicon.ico"):
            self.send_response(404)

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        print(post_data)

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")