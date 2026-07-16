import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


plt.ion()
# Generazione di dati casuali
dati = np.random.randn(1000)

# Creazione dell'istogramma con parametri
plt.hist(dati, bins=10, density=True, color='skyblue', edgecolor='black', alpha=0.8,cumulative=False)

# Personalizzazione del grafico
plt.title('Istogramma con parametri')
plt.xlabel('Valori')
plt.ylabel('Frequenza normalizzata')

# Mostra il grafico
plt.show()
# aaltro sempio

# Generazione di dati casuali (es. temperature)
dati = np.random.normal(25, 5, 1000) # media 25, deviazione standard 5

# Creazione della figura e degli assi
fig, ax = plt.subplots()

# Creazione dell'istogramma
ax.hist(dati, bins=20, color='skyblue', edgecolor='black')

# Aggiunta dei gradi agli assi
ax.set_xlabel('Temperatura ($^{\circ}$C)')
ax.set_ylabel('Frequenza')

plt.title('Distribuzione delle Temperature')
plt.show()
s=input("premi un tasto x chiudre")

# esmpio piu complsso
# 1. Dataset di esempio
data = {
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino'],
    'Popolazione': [2.8, 1.4, 0.9, 0.8]
}
df = pd.DataFrame(data)

# 2. Definizione dei colori specifici per ciascuna barra
colori_personalizzati = ['#E63946', '#F1FAEE', '#A8DADC', '#457B9D'] 

# Nota: puoi usare una lista di colori (HEX o nomi) o un colore singolo es. color='darkorange'

# 3. Creazione del grafico (assegniamo il grafico a una variabile 'ax')
ax = df.plot.bar(
    x='Città', 
    y='Popolazione', 
    color=colori_personalizzati, 
    edgecolor='black', # Aggiunge un bordo nero alle barre
    legend=False
)

# 4. Aggiunta delle etichette sopra le barre (Metodo automatico di Matplotlib)
ax.bar_label(ax.containers[0], padding=3, fmt='%.1f')

# 5. Personalizzazione dei testi
plt.title('Popolazione per Città', fontsize=14, fontweight='bold')
plt.ylabel('Milioni di abitanti', fontsize=12)
plt.xlabel('Città', fontsize=12)
plt.xticks(rotation=0) # Mantiene i nomi delle città in orizzontale
plt.tight_layout() # Evita che i testi o i bordi vengano tagliati nel salvataggio

# 6. Salvataggio del grafico come immagine
plt.savefig('.\Dataset_DataFrame\grafico_popolazione.png', dpi=300, bbox_inches='tight')

# 7. Mostra il grafico a schermo
plt.show()

s=input("premi un tasto x chiudre")
