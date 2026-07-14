"""
Scrivere un programma che presenta un menu di scelta come di seguito riportato

1. Somma tra 2 numeri
2. Concatenare 2 stringhe date in input
3. Pulire la consolle di debug
4. Terminare il programma
Il menu di scelta deve essere presentato a video fin quando l'utente non decide di terminare il programma
"""
import os

# Funzione che fa la somma di due numeri
def Somma (x, y):
     return x + y

# Funzione che concatena due numeri
def concatena(s1, s2):
    return s1 + s2

# Funzione che pulisce i debug
def pulisci_console():
    os.system('cls')

# Funzione che fa il print e pulisce la console in debug
def Stampa_In_Console(messaggio):
    pulisci_console()
    print(messaggio) 

while True:

    Stampa_In_Console('====MENU====')
    Stampa_In_Console('1. Somma tra 2 numeri')
    Stampa_In_Console('2. Concatenare 2 stringhe')
    Stampa_In_Console('3. Pulire la console')
    Stampa_In_Console('4. Terminare il programma')

    scelta= input('Scegli un\'opzione: ')

    if scelta == '1':
        x = float(input('Primo numero: '))
        y =float(input('Secondo numero: '))
        Stampa_In_Console('La somma è:', Somma(x,y))

    elif scelta == '2':
        s1 = input('Prima stringa: ')
        s2 = input('Seconda stringa: ')
        Stampa_In_Console ('Risultato:', concatena(s1, s2))
        

    elif scelta == "3":
        pulisci_console()

    elif scelta == '4':
        Stampa_In_Console('Programma Terminato')
        break
    else:
        Stampa_In_Console('Scelta non valida')

        


pulisci_console()

