from flask import Flask
import music # this will be your file name; minus the `.py`

app = Flask(__name__)

@app.route('/')
def dynamic_page():
    return music.fund()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)