from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import random
app = Flask(__name__) 
df = pd.read_csv("pokemon.csv")
dfcomune=df[df["Rarità"]=="Comune"]
dfncomune=df[df["Rarità"]=="Non Comune"]
dfrara=df[df["Rarità"]=="Rara"]
dfuber=df[df["Rarità"]=="Ultra Rara"]
crediti=100
collezione=pd.DataFrame()
pacchetto=pd.DataFrame()
def ri():
    global crediti, collezione, pacchetto
    for i in range(5):
                numero=random.randint(1, 100)
                if numero <= 70:
                    h=dfcomune.sample()
                    rezero = pd.DataFrame(h)
                    pacchetto=pd.concat([pacchetto, rezero])
                    collezione = pd.concat([collezione, rezero])
                    crediti+=1
                elif 71<= numero <91:
                    f=dfncomune.sample()
                    rezero = pd.DataFrame(f)
                    pacchetto=pd.concat([pacchetto, rezero])
                    collezione = pd.concat([collezione, rezero])
                    crediti+=3
                elif 91<= numero <100:
                    k=dfrara.sample()
                    rezero = pd.DataFrame(k)
                    pacchetto=pd.concat([pacchetto, rezero])
                    collezione = pd.concat([collezione, rezero])
                    crediti+=6
                elif numero==100:
                    L=dfuber.sample()
                    rezero = pd.DataFrame(L)
                    pacchetto=pd.concat([pacchetto, rezero])
                    collezione = pd.concat([collezione, rezero])
                    crediti+=888
    crediti -=10
def apri():
        global crediti, collezione, pacchetto
        if crediti>=10:
            pacchetto.drop(pacchetto.index, inplace=True)
            ri()
        else:
            return "crediti insufficienti"
def apri10():
    global crediti, collezione
    if crediti>=100:
        pacchetto.drop(pacchetto.index, inplace=True)
        for i in range(10):
            ri()
    else:
        print("crediti insufficienti")
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        eh = request.form.get("eh")
        if eh == "apri":
            risultato = apri()
        elif eh == "apri10":
            risultato = apri10()
        elif eh == "collezione":
            global collezione
            collezione.to_csv("collezione.csv", index=False)
    return render_template("index.html", crediti=crediti, pacchetto=pacchetto.to_html(index=False), df=df)

@app.route("/guardacollezione")
def guardacollezione():
    return render_template("collezione.html", collezione=collezione.to_html(index=False))








 
if __name__  == "__main__":
    app.run(debug=True)