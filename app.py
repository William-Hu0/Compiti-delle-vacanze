from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__) 

crediti=100

@app.route("/")
def index():
    df = pd.read_csv("profilo.csv")
    dati = df.iloc[0].to_dict()
    return render_template("index.html", crediti=crediti, dati=dati)











 
if __name__  == "__main__":
    app.run(debug=True)