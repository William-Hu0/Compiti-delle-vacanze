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
pacchetto=[]
def apri():
        global crediti, collezione, pacchetto

        if crediti>=10:
            for i in range(5):
                numero=random.randint(1, 100)
                if numero <= 70:
                    h=dfcomune.sample()
                    rezero = pd.DataFrame(h)
                    pacchetto.append(h)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=1
                elif 71<= numero <91:
                    f=dfncomune.sample()
                    rezero = pd.DataFrame(f)
                    pacchetto.append(f)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=3
                elif 91<= numero <100:
                    k=dfncomune.sample()
                    rezero = pd.DataFrame(k)
                    pacchetto.append(k)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=6
                elif numero==100:
                    L=dfncomune.sample()
                    rezero = pd.DataFrame(L)
                    pacchetto.append(L)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=888
            crediti -=10
        else:
            return "crediti insufficienti"
def apri10():
    global crediti, collezione
    if crediti>=100:
            for i in range(10):
                apri()
    else:
        print("crediti insufficienti")
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        azione = request.form.get("azione")
        if azione == "apri":
            risultato = apri()
        elif azione == "apri10":
            risultato = apri10()
        elif azione == "collezione":
            global collezione
            collezione.to_csv("collezione.csv", index=False)
    return render_template("index.html", crediti=crediti, pacchetto=pacchetto, df=df)

@app.route("/guardacollezione")
def guardacollezione():
    return render_template("collezione.html", collezione=collezione.to_html(index=False))








 
if __name__  == "__main__":
    app.run(debug=True)