import os
import http.server
import cgi
import json
import socket

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.answer_dat = None  # Inicjalizacja zmiennej answer_data

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
                    self.server.web_output_queue.put(fields)
                except Exception as e:
                    print('Błąd pobierania danych!')
                    print('Kod błędu - ', e)
            #testowe do poprawienia
            while True:
                answer = self.server.web_input_queue.get()
                if answer:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.end_headers()

                    doc = 'website/answer.html'

                    with open(doc, 'r') as f:
                        page_content = f.read()

                    page_content = page_content.replace('<!-- INSERT_ANSWER_HERE -->', str(answer))
                    self.wfile.write(page_content.encode())
                    break
                else:
                    continue
