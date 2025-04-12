from http.server import HTTPServer, BaseHTTPRequestHandler
import requests
import os

auth_key = os.environ['auth']
client_id = os.environ['client']

broadcaster_id = os.environ['broadcaster']
sender_id = os.environ['sender']


url = 'https://api.twitch.tv/helix/chat/messages'

vars = {}
class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        message = post_body.decode('utf-8')

        x = requests.post(url, data = f'{{"broadcaster_id": "{broadcaster_id}", "sender_id": "{sender_id}", "message": "{message}"}}', headers = {'Authorization': f'Bearer {auth_key}','Client-Id': client_id, 'Content-Type': 'application/json'})


server = HTTPServer(('0.0.0.0',8080),MyHandler)
server.serve_forever()
