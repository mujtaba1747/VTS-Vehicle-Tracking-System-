# This is a Simple Python server which sends JSON file when it receives a GET request
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
import json
import cgi
counter = 0 # variable to increment to read al JSON files
class Server(BaseHTTPRequestHandler):

    def _send_cors_headers(self):
      """ Sets headers required for CORS """
      self.send_header('Access-Control-Allow-Origin', '*')
      self.send_header("Access-Control-Allow-Origin", "*")
      self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
      self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
      self.send_header("Access-Control-Allow-Headers", "x-api-key,Content-Type")
    def do_OPTIONS(self):
        #self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8080')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With, Content-type")
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        global counter
        if counter == 1548:
            counter = 0
        string = "json" + str(counter) + ".json"
        # with open(string) as file:
        #     data = file
        data = open(string, "r").read()
        self._set_headers()
        self.wfile.write(data)
        counter = counter + 1
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.getheader('content-length'))
        message = json.loads(self.rfile.read(length))
        
        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message))
        
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('127.0.0.1', port)
    httpd = server_class(server_address, handler_class)
    
    print ('Starting httpd on port %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    run(port = 8080)   # Running on port 8080
    #from sys import argv
    
    #if len(argv) == 2:
    #    run(port=int(argv[1]))
        
