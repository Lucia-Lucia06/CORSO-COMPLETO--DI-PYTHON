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
        
         elif scelta == 2:
        if not studenti:
            print("Registro vuoto")
        else:
            for nome, voti in studenti.items():
                print(nome, voti)
   
 elif scelta == 3:
        if not studenti:
            print("Nessuno studente inserito")
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)
                print(f"{nome} - media: {media:2f}")

             elif scelta == 4:
        if not studenti:
            print('Nessun studente iserito')
        else:
            for nome, voti in studenti.items():
                media = sum(voti) / len(voti)

                if media >= 8:
                    print(nome, 'è stato "PROMOSSO"')
                else:
                    print(nome, 'è stato "BOCCIATO"')
    elif scelta == 0:
        print('Uscita del programma scolastico')
        break
    else:
        print("Scelta non valida!")    






