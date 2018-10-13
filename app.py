from flask import Flask, request
import os

app = Flask(__name__)

def get_ip(req):
    return req.get('remote_addr', '')

@app.route('/')
def hello_world():
    return 'Your IP is: <b>{}</b>'.format(request.remote_addr)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
