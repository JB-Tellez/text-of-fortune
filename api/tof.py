from http.server import BaseHTTPRequestHandler
from urllib import parse
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if dic.get("id"):
            game_data = {
                "id": int(dic["id"]),
                "used": "xyz",
                "status": "incorrect",
                "working_word": "_ _ t _ _",
            }
        else:
            game_data = {
                "id": 1,
                "used": "",
                "status": "start",
                "working_word": "_ _ _ _ _",
                "guesses": "",
            }

        message = json.dumps(game_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(message.encode())
