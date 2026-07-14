# 2f (è usato per formattare i numeri in virgola mobile)
media = 23.456781

#errore comune da non fare
#print(media.2f) # attenzione a questo tipo di errore 'float' object has no attribute 'f2'
print(f'la media è : {media:.5f}') # 5 (5 che è uguale a 6 perche si parte dallo 0) cifre dopo la virgola

