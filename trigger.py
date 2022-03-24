
import labelImg as data
from flask import Flask, request, render_template
import sys
app = Flask(__name__)


@app.route("/")
def hello():

    return render_template("index.html")


@app.route("/r")
def open():
    if __name__ == '__main__':
        sys.exit(data.main())


if __name__ == "__main__":
    app.run()
