tupla_traffico_siti = (
    ("Google",
        ("gennaio", ("ricerca", 120000)),
        ("febbraio", ("ricerca", 115000)),
        ("marzo", ("ricerca", 130000)),
        # Altri mesi...
    ),
    ("Facebook",
        ("gennaio", ("social", 90000)),
        ("febbraio", ("social", 85000)),
        ("marzo", ("social", 95000)),
        # Altri mesi...
    ),
    ("Amazon",
        ("gennaio", ("e-commerce", 70000)),
        ("febbraio", ("e-commerce", 65000)),
        ("marzo", ("e-commerce", 75000)),
        # Altri mesi...
    ),
    # Altri siti...
)

def presenza(sito,servizio):                                     # Controllo validità dati
    for sito_tupla,*informazioni in tupla_traffico_siti:
        if sito==sito_tupla:
            for mese,dati in informazioni:
                servizio_tupla,visite=dati
                if servizio_tupla==servizio:
                    return True
    return False

def analizza_traffico(sito,servizio):                            # Opzione 3
    visite_medie_tuplaAnalisi = media_traffico(tupla_traffico_siti,sito,servizio)
    massimo_visite_tuplaAnalisi,mesi_massimo_tuplaAnalisi = massimo_traffico(tupla_traffico_siti,sito,servizio)

    tupla_analizzata=(visite_medie_tuplaAnalisi,(massimo_visite_tuplaAnalisi,mesi_massimo_tuplaAnalisi))
    return tupla_analizzata

def media_traffico(tupla_traffico_siti,sito,servizio):           # Opzione 1
    array_visite=[]

    for sito_tupla,*informazioni in tupla_traffico_siti:
        if sito==sito_tupla:
            for _,dati in informazioni:
                servizio_tupla,visite=dati
                if servizio_tupla==servizio:
                    array_visite.append(visite)

    return round(sum(array_visite)/len(array_visite),2)

def massimo_traffico(tupla_traffico_siti,sito,servizio):         # Opzione 2 
    array_visite=[]
    array_mesi=[]

    for sito_tupla,*informazioni in tupla_traffico_siti:
        if sito==sito_tupla:
            for mese,dati in informazioni:
                servizio_tupla,visite=dati
                if servizio_tupla==servizio:
                    array_visite.append(visite)
    
    massimo_visite=max(array_visite)

    for sito_tupla,*informazioni in tupla_traffico_siti:
        if sito==sito_tupla:
            for mese,dati in informazioni:
                servizio_tupla,visite=dati
                if servizio_tupla==servizio and massimo_visite==visite:
                    array_mesi.append(mese)
    
    return massimo_visite,array_mesi


def menu_interattivo():                                          # Menù
    sito=input("Inserisci il nome del sito da analizzare: ")
    servizio=input("Inserisci il nome del servizio da analizzare: ")
    
    if presenza(sito,servizio):
        while(True):
            print("\nMenù\n" \
                "1. Media traffico \n" \
                "2. Visite massime \n" \
                "3. Analisi \n" \
                "0. Termine programma \n"
            )
            risposta=int(input("Scegli un'opzione: "))
            match (risposta):
                case 0:
                    print("Programma terminato.")
                    break
                case 1:
                    visite_medie=media_traffico(tupla_traffico_siti,sito,servizio)
                    print("Le visite medie inerenti al sito ed al servizio sono ",visite_medie)
                case 2:
                    massimo_visite,mesi_massimo=massimo_traffico(tupla_traffico_siti,sito,servizio)
                    print("Il valore massimo delle visite è di ",massimo_visite,", raggiunto nel/nei mese/i di ",mesi_massimo)
                case 3:
                    tupla_analizzata=analizza_traffico(sito,servizio)
                    print("Dati appartenenti al sito e al servizio richiesto: ",tupla_analizzata)
    else:
        print("Sito e/o servizio non presenti. ")      

menu_interattivo()                                                # Richiamo menù