# zeiten.py 
import sys

def zeitInSekunden(h,m,s):
    gesamt = 0
    gesamt += h * 3600
    gesamt += m * 60
    gesamt += s
    return gesamt

b = sys.argv
a = b[1].split(":")
h = int(a[0])
m = int(a[1])
s = int(a[2])
beginnSekunden = s + m*60 + h*3600

e = b[2].split(":")
h = int(e[0])
m = int(e[1])
s = int(e[2])
endeSekunden = s + m*60 + h*3600

print("Die Differenz beträgt: ", endeSekunden-beginnSekunden, " Sekunden")