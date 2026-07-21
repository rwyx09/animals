from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/pandas")
@app.route("/pende")
@app.route("/pada")
def pandas():
    return render_template("pandas.html")

@app.route("/foxes")
@app.route("/saharafox")
@app.route("/notfox")
def foxes():
    return render_template("foxes.html")


if __name__ == "__main__":
    app.run(port=6767)
