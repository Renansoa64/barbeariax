from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
 return render_template("index.html")

@app.route("/galeria")
def gallery():
 return render_template("Galeria.html")

@app.route("/contatos")
def contact():
 return render_template("Contatos.html")

@app.route("/sobre")
def about():
 return render_template("Sobre nós.html")