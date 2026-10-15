
ACTION è una piccola applicazione web sviluppata in Python con Flask per suddividere gli studenti in due gruppi bilanciati, massimizzando la media dei punteggi delle preferenze interne ai gruppi.

Dalla cartella del progetto, con l'ambiente Python corretto attivo:
python app.py
Aprire http://127.0.0.1:5000 nel browser, selezionare un file CSV e premere Ottimizza.

FORMATO CSV RICHIESTO:
Il file è una matrice quadrata di preferenze, con una prima riga di intestazione e una prima colonna di nomi. I valori sono separati da virgole (,).

Studente,A,B,C,D
A,NULL,5,3,2
B,4,NULL,7,1
C,3,8,NULL,6
D,2,1,5,NULL