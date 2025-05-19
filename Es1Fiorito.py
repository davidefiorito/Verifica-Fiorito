tupla_performance = (
    ("Mario Rossi", 12.5, 95, "2023-10-01"),
    ("Luca Bianchi", 11.8, 97, "2023-10-01"),
    ("Gianna Neri", 13.1, 90, "2023-10-02"),
    ("Sofia Verdi", 12.2, 96, "2023-10-02"),
    ("Carlo Marroni", 14.0, 88, "2023-10-03"),
    ("Paola Lilla", 11.9, 98, "2023-10-03"),
)

def totale_punti(tupla_performance):                      # Opzione 1
    array_punteggi=[]

    for _,_,punteggio,_ in tupla_performance:
        array_punteggi.append(punteggio)

    return sum(array_punteggi)   

def media_tempo(tupla_performance):                       # Opzione 2
    array_tempi=[]

    for _,tempo,_,_ in tupla_performance:
        array_tempi.append(tempo)

    return round(sum(array_tempi)/len(array_tempi),2)

def miglior_punteggio(tupla_performance):                 # Opzione 3
    tupla_max=()
    array_punteggi=[]

    for _,_,punteggio,_ in tupla_performance:
        array_punteggi.append(punteggio)

    for i in range (len(tupla_performance)):
        if tupla_performance[i][2]==max(array_punteggi):
            tupla_max=tupla_performance[i]

    return tupla_max

def menu_interattivo():                                   # Menù
    while(True):
        print("\nMenù\n" \
            "1. Punteggio totale \n" \
            "2. Tempo medio \n" \
            "3. Punteggio migliore \n" \
            "0. Termine programma \n"
        )
        risposta=int(input("Scegli un'opzione: "))
        match (risposta):
            case 0:
                print("Programma terminato.")
                break
            case 1:
                punteggio_tot=totale_punti(tupla_performance)
                print("Il punteggio totale è ",punteggio_tot)
            case 2:
                tempo_medio=media_tempo(tupla_performance)
                print("Il tempo medio è ",tempo_medio)
            case 3:
                tupla_migliore=miglior_punteggio(tupla_performance)
                print("Dati appartenenti al punteggio migliore: ",tupla_migliore)

print(tupla_performance)          
menu_interattivo()                                         # Richiamo menù 