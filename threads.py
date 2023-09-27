import threading
import socketserver
from RequestHandler import RequestHandler
import queue
import http.server

class QueuingTCPServer(socketserver.TCPServer):
    def __init__(self, server_address, RequestHandlerClass, web_output_queue, web_input_queue, bind_and_activate=True):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.web_output_queue = web_output_queue
        self.web_input_queue = web_input_queue

class WebWorker(threading.Thread):
    def __init__(self, port, web_output_queue, web_input_queue):
        super().__init__()
        self.port = port
        self.Handler = RequestHandler
        self.web_output_queue = web_output_queue
        self.web_input_queue = web_input_queue

    def run(self):
        with QueuingTCPServer(("", self.port), self.Handler, self.web_output_queue, self.web_input_queue) as server:
            print("Http Server Serving at port", self.port)
            server.serve_forever()



def init_threads():
    web_output_queue = queue.Queue()
    web_input_queue = queue.Queue()
    web_worker = WebWorker(8000, web_output_queue, web_input_queue).start()
    return web_output_queue, web_input_queue
