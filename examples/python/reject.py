#!/usr/bin/env python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import urlparse
import logging
from xml.dom.minidom import Document

logging.basicConfig(level=logging.DEBUG)

class MegaAwesomePythonServer(BaseHTTPRequestHandler):

    def do_POST(self):
        length = int(self.headers.getheader('Content-Length'))
        data = urlparse.parse_qs(self.rfile.read(length))

        logging.debug("from: " + data.get("from")[0])
        logging.debug("to: " + data.get("to")[0])

        doc = Document()
        response = doc.createElement('Response');
        reject = doc.createElement('Reject')
        reject.setAttribute('reason', 'busy')
        response.appendChild(reject);
        doc.appendChild(response)

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(doc.toxml())


server = HTTPServer(('', 3000), MegaAwesomePythonServer)
server.serve_forever()
