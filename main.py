from __future__ import annotations
from flask import Flask, render_template, request
import flask
import music
import sqlite3

app = Flask(__name__)



@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
    <div  class="center" style="border:1px solid black;width:50%;align:center;padding-right:50px;margin:auto" >
    <h1 style="text-align:center;">MUSIC GENAROTOR</h1>
        <form style="text-align:center;" action="/oop" method="get">
         <label>ENTER FILE NAME (exm.mid)</label>
            <input type="text" name="file_name" required>
            <button type="submit">Hit</button>
        </form>
          </br>
        </div>
      
    </body>
</html>'''

@app.route('/oop/')
def oop():
    p = request.args.get("file_name")
    music.abcd(p)
    return flask.redirect("/")

    


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080', debug=True)

            