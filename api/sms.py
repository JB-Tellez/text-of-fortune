from http.server import BaseHTTPRequestHandler
from urllib import parse
from twilio.twiml.messaging_response import MessagingResponse


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        resp = MessagingResponse()

        resp.message("ok then")

        message = str(resp)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        name = dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stranger"

        resp = MessagingResponse()

        resp.message(message)

        message = str(resp)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())
