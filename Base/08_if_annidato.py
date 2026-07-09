"""
    If Annidato in python 
    
    Sintassi base:
    if condizione 
        codice eseguito se la condizione è vera 

        if altra_condizione:
            codice eseguito se anche la seconda condizione è vera
        else:
            codice eseguito se la seconda condizione è falsa 
    else:
        codice eseguito se la prima condizione è falsa      
"""

# Esempio 1 Maggiore età
eta = int(input('Inserisci la tua età: '))
patente = True

if eta >= 18:
    print('Sei aggiorenne.')
    
    if patente:
        print('Poi guidare...🚗')
    else:
        print('Non poi gruidare perché non hai la patente...')
else:
    print('Se minorenne!')


if email == email_utente:
    if password == password_utente:
        print('Accesso consentito nel sistema')
    else:
        print('password errata')
else:
    print('Utente inesistente nel sistema')


voto: int = int(input('inserisci il voto: '))

if voto >= 18: 
    print('hai superato l\'esame ')
    if voto >= 30:
        print('Complimenti! Hai superato l\'esame con il massimo dei voti')
    else : 
        print('Promosso! con un voto', voto)
else :
    print('Non ammesso! perché hai ottenuto un punteggio che è minore di', voto)
