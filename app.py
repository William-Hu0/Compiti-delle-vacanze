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
def apri():
        global crediti, collezione
        if crediti>=10:
            for i in range(5):
                numero=random.randint(1, 100)
                if numero <= 70:
                    h=dfcomune.sample()
                    rezero = pd.DataFrame(h)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=1
                elif 71<= numero <91:
                    f=dfncomune.sample()
                    rezero = pd.DataFrame(f)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=3
                elif 91<= numero <100:
                    k=dfncomune.sample()
                    rezero = pd.DataFrame(k)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=6
                elif numero==100:
                    L=dfncomune.sample()
                    rezero = pd.DataFrame(L)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=888
            crediti -=10
        else:
            return "crediti insufficienti"
def apri10():
    if crediti>=100:
            for i in range(10):
                for i in range(5):
                    numero=random.randint(1, 100)
                    if numero <= 70:
                        h=dfcomune.sample()
                        rezero = pd.DataFrame(h)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=1
                    elif 71<= numero <91:
                        f=dfncomune.sample()
                        rezero = pd.DataFrame(f)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=3
                    elif 91<= numero <100:
                        k=dfrara.sample()
                        rezero = pd.DataFrame(k)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=6
                    elif numero==100:
                        L=dfuber.sample()
                        rezero = pd.DataFrame(L)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=888
                crediti -=10
    else:
        print("crediti insufficienti")
@app.route("/", methods=["GET", "POST"])
def index():
    risultato=""
    if request.method == "POST":
        azione = request.form.get("azione")
        if azione == "apri_uno":
            risultato = apri()
        elif azione == "apri_dieci":
            risultato = apri10()
        elif azione == "salva_collezione":
            global collezione
            collezione.to_csv("collezione.csv", index=False)
        return render_template("index.html", crediti=crediti)
    return render_template("index.html", crediti=crediti)











 
if __name__  == "__main__":
    app.run(debug=True)