# submissions.py 

abgabe = "10:00:00 3 1 10:20:00 wrong 1 10:45:00 correct 2 10:20:01 correct"
t = abgabe.split(" ")

startzeit = t[0]
submissions = t[1]
besteZeit = "23:59:59"
besterUser = -1

for position in range(2, len(t), 3):
    userId = t[position]
    zeit = t[position+1]
    loesung = t[position+2]
    print("Abgabe: ", userId, zeit, loesung)
    if(zeit < besteZeit and loesung == "correct"):
        besteZeit = zeit
        besterUser = userId

print(besterUser, besteZeit)