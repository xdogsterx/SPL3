# parkhaus.py 
# Angabe für das Beispiel: siehe moodle

print("Linienbus-Simulator")

haltestellen = input("Wie viele Haltestellen gibt es?")

print("Der Bus steht an Haltestelle ", haltestellen)

einsteiger = input("Wie viele Personen steigen ein?")
personen = int(einsteiger)

for h in range (0,10):
    
    print("Es sind ", personen, " Personen im Bus.")