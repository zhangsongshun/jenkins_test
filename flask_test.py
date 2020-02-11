from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    extent = 'welcome to easyops'
    return extent


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=28080, debug=True)
