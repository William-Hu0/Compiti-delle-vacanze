import random
import pandas as pd
def menu():
    print(f"inserisci 1 per aprire un pacchetto")
    print(f"inserisci 2 per aprire 10 pacchetti")
    print(f"inserisci 3 per mostare la collezione")
    print(f"inserisci 4 per mostare i punti")
    print(f"inserisci 5 per salvare la collezione in un file csv")
    print(f"inserisci 0 per uscire")
df = pd.read_csv("pokemon.csv")
dfcomune=df[df["Rarità"]=="Comune"]
dfncomune=df[df["Rarità"]=="Non Comune"]
dfrara=df[df["Rarità"]=="Rara"]
dfuber=df[df["Rarità"]=="Ultra Rara"]
crediti=100
collezione=pd.DataFrame()
while True:
    menu()
    d=int(input("cosa vuoi fare?"))
    if d == 1:
        if crediti>=10:
            for i in range(5):
                numero=random.randint(1, 100)
                if numero <= 70:
                    h=dfcomune.sample()
                    print(h)
                    rezero = pd.DataFrame(h)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=1
                elif 71<= numero <91:
                    f=dfncomune.sample()
                    print(f)
                    rezero = pd.DataFrame(h)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=3
                elif 91<= numero <100:
                    k=dfncomune.sample()
                    print(k)
                    rezero = pd.DataFrame(k)
                    colelzione = pd.concat([collezione, rezero])
                    crediti+=6
                elif numero==100:
                    L=dfncomune.sample()
                    print(L)
                    rezero = pd.DataFrame(L)
                    collezione = pd.concat([collezione, rezero])
                    crediti+=888
            crediti -=10
        else:
            print("crediti insufficienti")
    elif d==2:
        if crediti>=100:
            for i in range(10):
                for i in range(5):
                    numero=random.randint(1, 100)
                    if numero <= 70:
                        h=dfcomune.sample()
                        print(h)
                        rezero = pd.DataFrame(h)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=1
                    elif 71<= numero <91:
                        f=dfncomune.sample()
                        print(f)
                        rezero = pd.DataFrame(f)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=3
                    elif 91<= numero <100:
                        k=dfrara.sample()
                        print(k)
                        rezero = pd.DataFrame(k)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=6
                    elif numero==100:
                        L=dfuber.sample()
                        print(L)
                        rezero = pd.DataFrame(L)
                        collezione = pd.concat([collezione, rezero])
                        crediti+=888
                crediti -=10
        else:
            print("crediti insufficienti")
    elif d==3:
        print(collezione)
    elif d==4:
        print(crediti)
    elif d==5:
        collezione.to_csv("collezione.csv", index=False)
        print("Collezione salvata ")
    elif d==0:
        break