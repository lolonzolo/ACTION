from flask import Flask #lib per gestione app web
from flask import render_template #lib per pagina html
from flask import request #lib per leggere i dati inviati dal browser
from pathlib import Path
from io import TextIOWrapper #lib per conversione del file da stream di byte in stringhe

from csv_reader import read_csv
from optimizer import optimize_groups

app = Flask(__name__) #creazione app Flask, name sarà l'oggetto che rappresenta il server web,
                        #al quale verranno assegnate tutte le risorse necessarie
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024 #dimensione massima richiesta HTTP 1.048.576 byte, per evitare che l'utente
                                                #carichi file troppo grandi, in quel caso Flask genera errore HTTP
"""
-GET metodo con cui il browser chiede i dati per mostrare la pagina HTML
-POST metodo con cui il browser chiede di effetturare l'ottimizzazzione 
e determinare i gruppi quando carico un file e premo il pulsante ottimizza gruppi
"""
@app.route("/", methods=["GET", "POST"]) #associazione indirizzo web a funzione python
                                            #quando si apre http://127.0.0.1:5000/ esegue def index():

def index():
    result = None #contiene il risultato dell' ottimizzazione
    error = None #contiene un messaggio d'errore

    if request.method == "POST": #verifica se il browser ha fatto una richiesta POST
        file = request.files.get("file") #recupero del nome del file che l'utente ha caricato attraverso l'interfaccia
        #check sul file
        if not file or not file.filename:
            error = "Seleziona un file csv."
        elif Path(file.filename).suffix != ".csv":
            error = "Il file deve avere estensione .csv."
        else:
            try: 
                text_file = TextIOWrapper(file.stream, encoding="utf-8-sig", newline="") #TextIOWrapper funzione del modulo io di python che permette di trasformare un flusso di byte in testo
                students, matrix = read_csv(text_file)
                result = optimize_groups(students, matrix)
            except (ValueError, OSError) as e:
                error = str(e)

                
    return render_template("index.html", result=result, error=error) 


if __name__ == "__main__":
    app.run(debug=False, host="127.0.0.1", port=5000)
