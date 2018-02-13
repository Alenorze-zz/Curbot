import requests
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

def main():
    r = requests.get(URL + 'getMe')
    print(r.json())

if __name__ == '__main__':
    # import os
    # HOST = os.environ.get('SERVER_HOST', 'localhost')
    # try:
    #     PORT = int(os.environ.get('SERVER_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    # app.run(HOST, PORT)
