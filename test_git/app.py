from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Shiyanlou002!Hello Shiyanlou003!Hello Shiyanlou004!!!!!!!!!!!!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8002, debug=True)