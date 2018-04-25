# parkhaus.py 
# Angabe für das Beispiel: siehe moodle

print("Linienbus-Simulator")

haltestellen = input("Wie viele Haltestellen gibt es?")
 

for h in range (1,haltestellen):
    print("Der Bus steht an Haltestelle ", h, ".") 
    einsteiger = input("Wie viele Personen steigen ein?")
    personen = int(einsteiger)   
    print("Es sind ", personen, " Personen im Bus.")

print("Der Bus hat die Endstation erreicht.")
print("Bitte alle aussteigen!")