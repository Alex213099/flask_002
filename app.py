from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    return" Hello this is Alex Gitonga 22/05770 "

if __name__=="__main__":
    app.run(debug=True)