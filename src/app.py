from flask import Flask, render_template, redirect, request, url_for
from model.CriarPersonagem.personagem import Personagem
from model.CriarPersonagem.classes import ClassePersonagem
from model.CriarPersonagem.racas import RacaPersonagem
from model.Atributos.distribuicao import Distribuicao

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("criar_personagem"))

@app.route("/criar", methods=["GET", "POST"])
def criar_personagem():
    if request.method == "POST":
        nome = request.form.get("nome")
        estilo = request.form.get("estilo").lower()
        raca = request.form.get("raca").upper()
        classe = request.form.get("classe").upper()

        personagem = Personagem(nome, RacaPersonagem[raca], ClassePersonagem[classe])

        distribuicao = Distribuicao()


        return render_template("criar_personagem.html", personagem=personagem, criado=True)
    
    return render_template("criar_personagem.html",personagem=None, criado=False)

if __name__ == "__main__":
    app.run(debug=False)