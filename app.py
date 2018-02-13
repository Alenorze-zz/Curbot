import requests
import json 

from flask import Flask, request, jsonify

# from flask__sslify import SSLify

app = Flask(__name__)
# sslify = SSLify(app)
wsgi_app = app.wsgi_app

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
    pass



@app.route('/', methods=['POST', 'GET'])
def index():
    """Renders a sample page."""
    if request.method == 'POST':
        r = request.get_json()
        char_id = r['message']['chat']['id']
        message = r['message']['text']
        write_json(r)
        return jsonify(r)
    return "<h1>WELCOME!</h1>"


if __name__ == '__main__':
    app.run()
