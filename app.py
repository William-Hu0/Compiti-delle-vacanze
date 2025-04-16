from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__) 
lista=[1,2,3,4,5]

@app.route("/")
def index():
    return render_template("index.html", lista=lista)

@app.route("/profilo")
def profilo():

    return "Questa è la pagina profilo"

@app.route("/aggiungi",methods=["POST"])
def aggiungi():
    elemento = request.form['elemento']
    if elemento:
        lista.append(elemento)
    return redirect(url_for('index'))
    return render_template("index.html")









 
if __name__  == "__main__":
    app.run(debug=True)