studenti = {}

while True:
    print("\n--- Registro Studenti ---")
    print("1. AGGIUNGI STUDENTE:")
    print("2. MOSTRA REGISTRO")
    print("3. CALCOLA LA MEDIA")
    print("4. PROMOSSI/BOCCIATI")
    print("0. USCIRE")

    scelta = int(input("Scelta: "))

    if scelta == 1 :
        nome = input("Nome: ")

        voti = []

        for i in range(3):
            while True:
                try:
                    voto = int(input(f"Voto {i+1}: "))
                    voti.append(voto)
                    break
                except:
                    print("Inserisci un numero valido!")

        studenti[nome] = voti
         else: 
        print("Scelta non valida!")

