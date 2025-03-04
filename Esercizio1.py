negozi=["negozio1","negozio2","negozio3"]
venditeMax=[900,890,967]
venditeMin=[500,320,446]
mediaMax=0
mediaMin=0

for i in len(negozi):
    mediaMax+=venditeMax[i]
mediaMax=mediaMax/3

for i in len(negozi):
    mediaMin+=venditeMin[i]
mediaMin=mediaMin/3

print(f"La media delle vendite minime dei negozi in giornata è {mediaMin}, la media delle vendite massime è {mediaMax}")

for i in len(venditeMin):
    if venditeMin[i]<mediaMin:
        print(f"Il {negozi[i]} ha avuto una vendita minima inferiore minore della vendita minima media ({venditeMin[i]})")

risposta="negozio4"
if risposta in negozi:
    print("Il negozio è nell'elenco negozi")
else:
    print("Il negozio non è nell'elenco negozi")

