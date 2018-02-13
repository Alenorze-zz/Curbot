import requests
import json 

from flask import Flask
# from flask__sslify import SSLify

# app = Flask(__name__)
# sslify = SSLify(app)

# wsgi_app = app.wsgi_app


# @app.route('/')
# def index():
#     """Renders a sample page."""
#     return "Hello World!"

URL = 'https://api.telegram.org/bot<token>/'

def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def send_message(chat_id, text="bla-bla"):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()
    

def main():
    r = get_updates()
    chat_id = r['result'][-1]['message']['chat']['id']
    send_message(char_id)


if __name__ == '__main__':
    # import os
    # HOST = os.environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(os.environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    # app.run(HOST, PORT)
