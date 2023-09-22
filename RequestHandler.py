import _socket
import os
import http.server
import cgi
import queue


class RequestHandler(http.server.SimpleHTTPRequestHandler):
    
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()

            doc = 'website/index.html'

            f = open(doc)

            self.wfile.write(f.read().encode())
            #self.path = 'website/index.html'
            #return http.server.SimpleHTTPRequestHandler.do_GET(self)
        elif self.path == '/website/img/sudoku.png':
            self.send_response(200)
            self.send_header("Content-Type", "image/png")
            self.end_headers()

            self.wfile.write(open("website/img/sudoku.png", 'rb').read())
        else:
            self.send_response(404)
            self.end_headers()
  
    def do_POST(self):
        print('POSTING')
        if self.path == '/data':
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
            if ctype == 'multipart/form-data':
                try:
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    print(fields)
                except:
                    pass
        
        self.send_response(301)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header('Location', '/')
        self.end_headers()