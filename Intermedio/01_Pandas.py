# Pandas èn una libreria di python:
# Legge dati (CSV, Excel, Text)
# Analizza dati
# Filtrare, modificare, aggregare

# Quindi è lo strumento principale per un Data Analyst
# Istallazione di pandas: pip install pandas


"""
    .env => salvare pacchetti
         => riutilizzare i pacchetti istallati su ogni file di progetto
         => esempio: import pandas as pd
"""

""""
 
1 => per la creazione del .venv
    python -m venv .venv

2 => per l'attivazione del .venv
    .venv\Scripts\activate
se non va eseguire la riga sotto:

"""
 #(Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned) ; (& .venv\Scripts\Activate.ps1)

   #a) per disattivare il .venv
    #    deactivate

import pandas as pd

# Creazione della lista degli studenti con i voti
studenti = {
        'nome': ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo', 'Francesca'],
        'voti':  [10, 8, 9, 7, 10, 6, 5, 4, 10, 8]
        }

# Creazione del DataFrame(Foglio excel, Tabella, Entità)
df= pd.DataFrame(studenti)

print(df)