from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titulo="Inicio", nombre=None)

@app.route("/about")
def about():
    return render_template("about.html", titulo="Acerca de")

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return render_template("index.html", titulo="Usuario", nombre=nombre)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
