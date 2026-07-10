# primo passo
"""
    I tipi di dati in python

    int => intero
    str => stringa
    float => decimali
    bool => boolean

    Dichiarazione di una variabile in python

    nome_variabile = ''
"""

# <class 'str'>
nome_variabile = 'Mattia'
# print(type(nome_variabile))

# <class 'int'>
numero_int = 15
# print(type(numero_int))

# <class 'float'>
numero_deci = 15.85694
# print(type(numero_deci))

# <class 'bool'
boolean_var = True
# print(type(boolean_var))


print("=" * 40)
print("       Concatenazione     ")
print("=" * 40, '\n')

nome = 'Roxana'
cognome = 'Otori'
eta = 35
stipendio = 23.456789

print('Nome ' + nome + ' Cognome ' + cognome + ' età ' + str(eta) + ' stipendio ' + str(stipendio) + '€ al mese')
print('\n') # vai alla riga

print('Nome', nome, 'Cognome', cognome, 'età', str(eta), 'stipendio', str(stipendio), '€ al mese')
print('\n') # vai alla riga

# formattazione
print(f'ciao mi chiamo {nome} - {cognome} ho {eta} anni, guadagno {stipendio:.5f}€ al mese\n')
print('\n') # vai alla riga
