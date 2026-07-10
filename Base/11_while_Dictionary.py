"""
    Dictionary in Python
    Cos'è un dictionary?
    ----------------------

    Un dizionario è una struttura cha salva dati in questo modo
    chiave -> valore
"""

# Esempio reale:
# nome = 'mario'
# eta = 20
# citta = 'Roma'

studente = {
    'nome': 'Mario',
    'cognome': 'Rossi',
    'eta': 25,
    'citta': 'Bologna',
    'corsi': [
        'Python', 'SQL Server', 'Pandas', 'MatplotLib', 'FastApi'
    ]
    'telefono': '+3932718901524'
}

# Accedere ai valori
print(studente[nome])
print(studente.get('telefono'))

# Modificare un valore
studente['eta'] = 26
print(studente['eta'])


# Ciclo su dictionaryù
# Esempio 1: Solo valori
for key in studente:
    print(key)

# Esemipo 2: Solo valori
for value in studente:
    print(value)

# Chiave e valori
for key, value in studente.items():
    print(key, value)


# Dictionry con Liste (Avanzato)
utenti = {
    "name": "Mario",
    "age": 30,
    "isStudent": False,
    "courses": {
        "Math": ["Algerb", "Geometry", "Analys"],
        "Science": ["Bilogy", "Chemestry"]},
    "address": {
        "city": ["Ferrara","Bologna", "Roma", "Napoli", "Paris", "Yaoundé", "Barcelon"],
        "country": ["Italy", "France", "Cameroon", "Spain"],
    }
}

for key, value in utenti.items():
    print(key, value)

    studenti = {
    'Stefano': [5, 10, 28, 30, 26, 7],
    'Massa': [10, 3, 18, 25, 30, 28],
    'Lucia': [50, 40, 30, 20, 10, 5]
}
    
    # Calcolare la media dei voti
for nome, voti in studenti.items():
    media = sum(voti) / len(voti)
      print('Nome:', nome, 'Voto media:', media:.3f)
    
    # Ciclo while
numero = 10

while numero:
    print('Ciaoooooo 😅')
    break


while True:
    if numero == 10:
        print('Ciaoooooo 😅')
        break
    else:
        print('😭😭😭😭')


while True:
    if numero >= 1:
        print('Ciaoooooo 😅')
        break
    else:
        print('😭😭😭😭')

