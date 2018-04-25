# submissions.py 

abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:01 correct"
t = abgabe.split(" ")
print(t)
startzeit = t[0]
submissions = t[1]

for x in range(2, len(t), 3):
    print("UserID", t[x])
    print("Zeit", t[x+1])
    print("Lösung", t[x+2])