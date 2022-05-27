import requests
from flask import Flask, request
from Utils import SCORE_FILE_NAME
from Utils import BAD_RETURN_CODE

app = Flask("something")


@app.route('/', methods=['GET', 'POST', 'DELETE'])
def score_server():
    if request.method == 'GET':
        ERROR = 0
        SCORE = 0
        data = ""
        filename = 'C:/Users/User/PycharmProjects/WorldOfGames/venv/Scripts/' + SCORE_FILE_NAME
        try:
            file = open(filename, "r")
            file.seek(0)
            SCORE = file.read()
            if not SCORE:
                SCORE = 0
        except FileExistsError as e:
            ERROR = {e.args}
        except FileNotFoundError as e:
            ERROR = {e.args}
        except BaseException as e:
            ERROR = {e.args}
        finally:
            if not ERROR and file:
                file.close()

        if ERROR:
            str = f'<h1><div id="score" style="color:red">{ERROR}</div></h1>'
        else:
            str = f'<h1>The score is <div id="score">{SCORE}</div></h1>'

        data = f"""
                 <html>
                     <head>
                         <title>Scores Game</title>
                     </head>
                     <body>
                           {str}
                     </body>
                 </html> """

        return data

    elif request.method == 'POST':
        return "saved new car"


@app.route('/test')
def my_func():
    return "hello and welcome to the world of games"


app.run(host="0.0.0.0", port=5001, debug=True)
