# zeiten.py 

def zeitInSekunden(h,m,s):
    gesamt = 0
    gesamt += h * 3600
    gesamt += m * 60
    gesamt += s
    return gesamt

beginnZeit = input("Beginnzeit: ")
endeZeit = input("Endezeit: ")

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

ende = endeZeit.split(":")
print(ende)

h = int(ende[0])
m = int(ende[1])
s = int(ende[2])

print("Stunden: ", h)
print("Minuten: ", m)
print("Sekunden: ", s)

endeSekunden = s + m*60 + h*3600
print("Gesamt Sekunden Ende: ", endeSekunden)