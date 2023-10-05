import threading
import socketserver
from RequestHandler import RequestHandler
import queue

class QueuingTCPServer(socketserver.TCPServer):
    '''
    Adding input and output queue to socketserver.TCPServer class.
    '''
    def __init__(self, server_address, RequestHandlerClass, web_output_queue, web_input_queue, bind_and_activate=True):
        socketserver.TCPServer.__init__(self, server_address, RequestHandlerClass, bind_and_activate)
        self.web_output_queue = web_output_queue
        self.web_input_queue = web_input_queue

class WebWorker(threading.Thread):
    '''
    This is a class for TCPSercer thread.
    It's running http server with given input/output queues and RequestHandler class.
    '''
    def __init__(self, port, web_output_queue, web_input_queue):
        super().__init__()
        self.port = port
        self.Handler = RequestHandler
        self.web_output_queue = web_output_queue
        self.web_input_queue = web_input_queue

    def run(self):
        '''
        Start serving TCPServer with added queues.
        '''
        try:
            with QueuingTCPServer(("", self.port), self.Handler, self.web_output_queue, self.web_input_queue) as server:
                print("Http Server Serving at port", self.port)
                server.serve_forever()
        except Exception as e:
            print("Error while running the server: ", str(e))



def init_threads(port=8000):
    '''
    Initialization of queues and web server thread
    Server is hosting on localhost on port 8000.
    Function is returning input and output queues.
    '''
    try:
        web_output_queue = queue.Queue()
        web_input_queue = queue.Queue()
        WebWorker(port, web_output_queue, web_input_queue).start()
        return web_output_queue, web_input_queue
    except Exception as e:
        print("Error initializing web server: ", str(e))
        return None, None
