"""
    Obiettivo del progetto:
    il computer ssceglie un numero tra 1 e 10.
    L'utente ha 5 tentativi per indovinarlo.
    
    Ad ogni tentativo il programma dice se il nume è troppo alto o troppo basso.
"""
import random


# Il computer sceglie un numero casuale
numerp_egreto = random.randint(1, 10)

print('=' * 50) # genera 70 ================================================
print("🎮 INDOVINA IL NUMERO 🎮")
print('=' * 50)

print("il computer ssceglie un numero tra 1 e 10.")
print("Hai a disposizione 5 tentativi.\n")

# il ciclo for permette al gioccatore(utente) di fare 5 tentativi.
for tentativo in range(1, 6):
    print(f"\nTentativo {tentativo} di 5")
    
# inserimento dell'utente
    numero = int(input("Inserisci il tuo numero: "))

# Verifica se il numero dell'utente è uguale al numero generato del computer
    if numero == numerp_egreto:
        print("🎉 Complimenti! Hai indovinato!")
         break
    
     if numero < numerp_egreto:
        print("📈 Il numero segreto è più grande!")
    
    if numero > numerp_egreto:
        print('📉 Il numero è più piccolo')


 # Se il ciclo termina seza break
if numero != numerp_egreto:
    print('\n😭 Hai terminato i tentativi.')
    print('Il numero era', numerp_egreto)    