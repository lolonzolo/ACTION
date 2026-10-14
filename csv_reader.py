import csv 


"""
Input: 
Studente,A,B,C,D
A,0,1,2,2
B,1,0,4,0
C,2,2,0,2
D,1,1,5,0

Il file csv viene inizialmente trasformato in una lista di liste. Ogni lista sarà una riga del csv. I valori letti saranno stringhe:
rows = [
    ["Studente", "A", "B", "C", "D"],
    ["A", "0", "1", "2", "2"],
    ["B", "1", "0", "4", "0"],
    ["C", "2", "2", "0", "2"],
    ["D", "1", "1", "5", "0"]
]


CONTROLLI IMPLEMENTATI:
- check vincolo numero studenti: min 4, in modo da formare gruppi da due, max per non esagerare coi costi computazionali
- check matrice quadrata 
- check che la diagonale sia stringhe "NULL" e il resto della matrice abbia valutazioni comprese tra 0 e 10
"""
def read_csv(file):
        reader = csv.reader(file)
        rows = list(reader)

        #check csv vuoto
        if not rows:
            raise ValueError("CSV vuoto")

        students = [name.strip() for name in rows[0][1:]]
        n = len(students)
        #check vincoli studenti
        if n < 4 or n > 12:
            raise ValueError("Il numero di studenti deve essere compreso tra 4 e 12")

        #check matrice quadrata: numero righe(esclusa la prima)=num studenti
        if len(rows) -1 != n:
            raise ValueError("Il numero di righe non corrisponde al numero di studenti")

        matrix = []

        for i, row in enumerate(rows[1:]): 

            #check matrice quadrata: check numero colonne per ogni riga
            if len(row) -1 != n:
                raise ValueError("Numero colonne non valido")
            values = []
            
            for j, value in enumerate(row[1:]):
                value = value.strip()  

                #check diagonale NULL
                if i == j:
                    if value != "NULL":
                        raise ValueError(f"L'elemento ({i},{j}) deve essere NULL")
                    values.append(None)

                #check elementi fuori dalla diagonale
                else:
                    try:
                        number = int(value)
                    except ValueError:
                        raise ValueError(f"L'elemento ({i},{j}) deve essere un numero intero")
                    if number <0 or number >10:
                        raise ValueError(f"L'elemento ({i},{j}) deve essere compreso tra 0 e 10")
                    values.append(number)
            matrix.append(values)
        return students, matrix

