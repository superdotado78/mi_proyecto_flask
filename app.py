from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola, Flask está funcionando!"

@app.route("/usuario/<nombre>")
def usuario(nombre):
    return f'Bienvenido a mi página, {nombre}!'

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
