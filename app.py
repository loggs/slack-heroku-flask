from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Your ip is: <b>{}</b>'.format(request.remote_addr)

if __name__ == '__main__':
    app.run(port=3000)
