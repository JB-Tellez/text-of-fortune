from http.server import BaseHTTPRequestHandler
from urllib import parse
import json

from api.pygirl2 import game_turn, start_game


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if dic.get("id"):
            id_ = int(dic["id"])
            guess = dic["guess"]
            guesses = dic.get("guesses","")
            game_data = game_turn(id_, guess, guesses)
        else:
            game_data = start_game()

        message = json.dumps(game_data)

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(message.encode())
