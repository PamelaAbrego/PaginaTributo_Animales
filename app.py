from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.htm")


# Extensión en el url para más htmls


@app.route("/vertebrados")
def about():
    return render_template("vertebrados.htm")


if __name__ == "__main__":
    app.run(debug=True)
