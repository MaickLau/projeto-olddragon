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

        if request.form.get("atributos_finais"):
            atributos_finais = {
                "Força": int(request.form.get("Força")),
                "Destreza": int(request.form.get("Destreza")),
                "Constituição": int(request.form.get("Constituição")),
                "Inteligência": int(request.form.get("Inteligência")),
                "Sabedoria": int(request.form.get("Sabedoria")),
                "Carisma": int(request.form.get("Carisma"))
            }

            personagem = Personagem(
                nome=nome,
                raca=RacaPersonagem[raca],
                classe=ClassePersonagem[classe]
            )
            personagem.atributos = atributos_finais

            return render_template("criar_personagem.html", criado=True, personagem=personagem)
        
        distribuicao = Distribuicao()

        if estilo == "classico":
            atributos = distribuicao.classico()
            personagem = Personagem(nome, RacaPersonagem[raca], ClassePersonagem[classe])
            personagem.atributos = atributos
            return render_template("criar_personagem.html", criado=True, personagem=personagem)
        
        else:
            if estilo == "aventureiro":
                valores = distribuicao.aventureiro()
            else:
                valores = distribuicao.heroico()

        return render_template(
            "criar_personagem.html",
            distribuindo=True,
            valores=valores,
            nome=nome,
            raca=raca,
            classe=classe,
            estilo=estilo)
    
    return render_template("criar_personagem.html",personagem=None, criado=False)

if __name__ == "__main__":
    app.run(debug=True)