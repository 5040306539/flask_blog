from cProfile import run
from flask import Flask

app=Flask(__name__)

@app.route("/")
def index():
    return "home page"

if __name__=="__main__":
    app.run(debug=True)