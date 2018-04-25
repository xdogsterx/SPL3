# parkhaus.py 
# Angabe für das Beispiel: siehe moodle

print("Linienbus-Simulator")

haltestellen = input("Wie viele Haltestellen gibt es?")
haltestellenAusgabe = int(haltestellen)

for h in range (1,haltestellenAusgabe+1):
    print("Der Bus fährt.")
    print("Der Bus steht an Haltestelle ", h, ".") 
    einsteiger = input("Wie viele Personen steigen ein?")
    personen = int(einsteiger)   
    aussteiger = input("Wie viele Personen möchten aussteigen?")
    aussteigerAusgabe = int(aussteiger)
    print("Es sind ", personen-aussteigerAusgabe, " Personen im Bus.")

print("Der Bus hat die Endstation erreicht.")
print("Bitte alle aussteigen!")