#dichiarazione della variabile

nome = 'Marco'
eta = 65
stipendio = 1.800
lavoratore = True
c='ciao, mi chiamo ' + nome + ' ed ho ' + str(eta) + ' anni'
print(c)
input('premi un tasto per continuare')
# Formattazione
print(f'ciao mi chiamo {nome} ho {eta} anni, guadagno {stipendio}€ al mese')
print('\n') #vai a capo

# Concatenazione
print('ciao mi chiamo ' + nome + ' ho ' + str(eta) + ' anni , guadagno ' + str(stipendio) + ' €  al mese')
# Interpolazione
print('mi chiamo:', nome, ' ho ', eta, ' anni')
