oreP=[17,10,15]
oreA=[22,13,21]
destinazioni=["Roma","Parigi","Milano"]

for i in len(destinazioni):
    print(f"Destinazione {destinazioni[i]}")
    print(f"Ora di partenza: {oreP[i]}")
    print(f"Ora di arrivo: {oreA[i]}")
    print()

intervalloP=18
intervalloA=20

for i in len(destinazioni):
    if intervalloP>=oreP[i] and intervalloA>=oreA[i]:
        print(f"Il volo delle {oreP[i]} - {oreA[i]} per {destinazioni[i]} è disponibile")
