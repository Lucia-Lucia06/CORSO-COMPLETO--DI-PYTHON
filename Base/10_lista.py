# Creazione della lista
mia_lista = ["Mela", "Banana", "Pera"] # (variable) mia_lista: list

        #    0       1       2         3        4
colori = ["Rosso", "blu", "Verde", "Giallo", "Bianco"]



# Stampa della lista
print(mia_lista, '\n\n')

# Accedere ad un elemento della lista 
print(colori[1]) # select nome from colori where id = 1 

# Modificare un elemento della lista
mia_lista[1] = 'Kiwi'
print(mia_lista)

print('=' * 40, '\n')


# Lunghezza della lista 
studenti = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']

print(len(studenti))


# Aggiungere elementi nella lista 
voti: int = []

voti.append(10)
voti.append([10, 20, 30,40,50])

print('Lista dei voti', voti)

frutti = ['Mela', 'Banana']
frutti.insert(1, 'Ananas')

print(frutti)

# Eleminare un elemento nella lista
frutti.remove('Banana')

print()
print(frutti)

# Eliminare un elemento nella lista

print()
print(studenti)

studenti.pop(2) # DELETE FRON frutti Where nome = 'Banana'
print()
print(studenti)

# Svuotare gli elememnti della lista
utenti = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']

utenti.clear()
print(utenti)

print('=' * 40, '\n')
persone = ['Massa', 'Anntonella', 'Luigi', 'Eduardo', 'Matteo', 'Stefano', 'Lucia', 'Annaritantonia', 'Paolo']

for i in range(len(persone)):
    print('Nome ', i, persone[i])


print('=' * 40, '\n')
