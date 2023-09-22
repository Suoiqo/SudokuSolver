from collections.abc import Callable, Iterable, Mapping
import threading
import socketserver
import queue
import http.server
from typing import Any
from RequestHandler import RequestHandler

class WebWorker(threading.Thread):
    def __init__(self, port):
        super().__init__()
        self.port = port
        #self.q_output = q_output
        self.Handler = RequestHandler
    
    def run(self):
        with socketserver.TCPServer(("", self.port), self.Handler) as httpd:
            print("Http Server Serving at port", self.port)
            httpd.serve_forever()


def init_threads():
    web_worker = WebWorker(8000).start()