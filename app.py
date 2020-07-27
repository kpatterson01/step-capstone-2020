from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hierachyTree.html")
def hierachyTree():
    return render_template("hierachyTree.html") 


@app.route("/provisionMetrics.html")
def provisionMetrics():
    return render_template("provisionMetrics.html")


if __name__ == "__main__":
    app.run()
