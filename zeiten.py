# zeiten.py 

beginnZeit = input("Beginnzeit: ")
##endeZeit = input("Endezeit: ")

# Zeit in Format HH:MM:SS
beginn = beginnZeit.split(":")
print (beginn)

h = int(beginn[0])
m = int(beginn[1])
s = int(beginn[2])

print("Stunden: ", h)
print("Minuten: ", m)
print("Sekunden: ", s)

beginnSekunden = s + m*60 + h*3600
print("Gesamt Sekunden Beginn: ", beginnSekunden)