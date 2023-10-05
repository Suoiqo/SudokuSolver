import http.server
import cgi
import time

class RequestHandler(http.server.BaseHTTPRequestHandler):
    '''
    Class for handling get and post requests arrive at the server.
    It's using methods and instance variables provided by BaseHTTPRequestHandler.
    '''

    #Variable containing path to file, content type and variable pointing on handlig image for every url
    URL_TO_PATH = {
                    '/': ('website/index.html', 'text/html', False),
                    '/index.html': ('website/index.html', 'text/html', False),
                    '/help.html': ('website/help.html', 'text/html', False),
                    '/website/img/sudoku.png': ('website/img/sudoku.png', 'image/png', True),
                    '/styles.css': ('website/styles.css', 'text/css', False),
                    '/scripts.js': ('website/scripts.js', 'text/javascript', False),
                    }
    
    TIMEOUT_SECONDS = 60

    def send_response_headers(self, content_type):
        #Sending 'OK' response
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.end_headers()

    def send_error_response(self, status_code, message):
        #Sending error response
        self.send_response(status_code)
        self.end_headers()
        self.wfile.write(message.encode())
    
    def send_redirect_respons(self, location):
        #Redirect to diffrent URL
        self.send_response(302)
        self.send_header("Location", location)  
        self.end_headers()


    def do_GET(self):
        #Handling simple GET request
        if self.path in RequestHandler.URL_TO_PATH:
            #Read path to file, content type and is_image varible from URL_TO_PATH
            ptah_to_file, content_type, is_image = RequestHandler.URL_TO_PATH[self.path]

            #Send OK response headers
            self.send_response_headers(content_type)

            #Reading the html/css/js file on given path
            #If file 'is_image' it is readed binary and not encoded
            try:
                with open(ptah_to_file, 'rb' if is_image else 'r') as f:
                    page_content = f.read()
                self.wfile.write(page_content if is_image else page_content.encode())
            except FileNotFoundError:
                self.send_error(404, "File not found!")

        #Handling GET '/answer' - display answer.html after receving result in input queue
        elif self.path == '/answer.html':
            #Seting a start time
            start_time = time.time()
            try:
                #Waiting for the response with answer for TIMEOUT_SECONDS 
                while time.time() - start_time < RequestHandler.TIMEOUT_SECONDS:
                    # Check if there's Sudoku board data in the input queue
                    if not self.server.web_input_queue.empty():
                        answer = self.server.web_input_queue.get()

                        #If there is response send OK headers
                        self.send_response_headers('text/html')

                        #Reading answer.html file
                        doc = 'website/answer.html'
                        with open(doc, 'r') as f:
                            page_content = f.read()

                        #Replacing prepered piece of code in answer.html with loaded answer
                        page_content = page_content.replace('<!-- INSERT_ANSWER_HERE -->', str(answer))
                        self.wfile.write(page_content.encode())
                        break
                else:
                        #Rise TimeoutError if loop ended without data
                        raise TimeoutError("Timeout while waiting for data!")
            except TimeoutError as e:
                # Handle the timeout error
                self.send_error_response(500, f"Timeout error: {str(e)}")
                    
        else:
            self.send_error_response(404, "URL not found!")

  
    def do_POST(self):
        #Handling user input 
        print('Sending data from user')
        if self.path == '/data':
            #Reading input data with cgi
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')

            if ctype == 'multipart/form-data':
                try:
                    fields = cgi.parse_multipart(self.rfile, pdict)
                    #Put user input in output queue
                    self.server.web_output_queue.put(fields) 
                except Exception as e:
                    print('Error with reading input data:' , str(e))
                    self.send_error_response(500, "Error with reading input data!")

            self.send_redirect_respons("/answer.html")
            
        else:
            self.send_error_response(404, "URL not found!")
