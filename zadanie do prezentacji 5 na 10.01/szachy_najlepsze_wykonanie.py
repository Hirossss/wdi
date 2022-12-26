import random
from figures import Bishop

run=True
while(run):
    n=int(input("Podaj ile gońców chcesz na szachownicy? "))
    if n <= 1 or n > 99:
        print("Wprowadź ilosc goncow pononwie")
        run=True
    else:
        run=False

def check(data):
    c=0
    for a in data:
        for b in data:
            if (b[0] - a[0] == b[1] - a[1]) or (-b[0] + a[0] == b[1] - a[1]):
                if b[0] - a[0] != 0 and b[1] - a[1] != 0:
                    print("Kordynaty pierwszego gońca: " + str((a[0], a[1])),
                          "Kordynaty drugiego gońca: " + str((b[0], b[1])))
                    c+=1
    if c == 0:
        print("Zadne gonce sie nie bija")
    if c==2:
        print("Dokladnie dwa gonce sie bija")
    if c>2:
        print("Bija sie ponad dwa gonce, a dokladnie "+str(c)+" gonce")

dane=[] #w formie (posx,posy)
for i in range(n):
    bishop=Bishop("bishop",random.randint(1,100),random.randint(1,100))     #1,100
    dane.append((bishop.posx,bishop.posy))
print(dane)


probna=[(3,8),(5,6),(4,4)]

check(dane)


