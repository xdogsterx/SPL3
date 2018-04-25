# parkhaus.py 
# Angabe für das Beispiel: siehe moodle

print("Linienbus-Simulator")

personenMax = 60
personen = 0
haltestellen = input("Wie viele Haltestellen gibt es?")
haltestellenAusgabe = int(haltestellen)

for h in range (1,haltestellenAusgabe+1):
    personenOk = False
    while(personenOk == False):
        print("Der Bus steht an Haltestelle ", h, ".") 
        einsteiger = input("Wie viele Personen steigen ein?")
        personen = personen + int(einsteiger)   
        aussteiger = input("Wie viele Personen möchten aussteigen?")
        personen = personen-int(aussteiger)
        aussteigerAusgabe = int(aussteiger)
        insgesammtLeute = personen-aussteigerAusgabe
        personenImBus = personen
        print("Es sind ", personenImBus, " Personen im Bus.")
        if(personenImBus<=personenMax and personenImBus > 0):
            print("Der Bus fährt.")
            personenOk = True
        elif(personenImBus<0):
            print("Fehler! Negativer Wert erkannt! Es würden sich ", personen, " Personen im Bus befinden!")
            personen = personen+int(aussteiger)
            personen = personen-int(einsteiger)
            print("Es sind ", personen, " Personen im Bus.")
        else:
            print("Es können", personen-personenMax, "Personen nicht mitfahren")

print("Der Bus hat die Endstation erreicht.")
print("Bitte alle aussteigen!")