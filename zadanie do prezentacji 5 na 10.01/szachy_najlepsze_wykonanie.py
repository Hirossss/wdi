'''
ZADANIE
Proszę przygotować implementację zadania z Części 1, zestawu 9 z wykorzystaniem klas,
tj. klasa powinna reprezentować np. punkt albo figurę na płaszczyźnie albo figurę w szachach.
Proszę skorzystać z mechanizmu dziedziczenia.

Proszę napisać po 3 testy z wykorzystaniem Unittest i Pytest.

Zadanie z zestawu 9:
Na szachownicy o wymiarach 100 na 100 umieszczamy N gońców (N<100).
Położenie gońców jest opisywane przez tablicę:
 dane = [(w1, k1), (w2, k2), (w3, k3), ..., (wN, kN)]
Proszę napisać funkcję, która zwróci położenie gońców wzajemnie się szachujących.
Do funkcji należy przekazać położenie gońców. Należy zwizualizować rozkład gońców na szachownicy.
Testy powinny uwzględniać między innymi:

1. Przypadek, w którym nie występuje szachowanie.
2. Przypadek, w którym szachują się dwa gońce.
3. Przypadek, w którym szachują się więcej niż dwa gońce.
'''

import random
from figures import Bishop  #korzystamy z klasy

def check(data):    #do wyjasnienia korzystam z artykulu, https://www.geeksforgeeks.org/check-whether-bishop-can-take-down-pawn-or-not/
    c=0 #licznik, przyda sie pozniej
    for a in data:
        for b in data:
            if (b[0] - a[0] == b[1] - a[1]) or (-b[0] + a[0] == b[1] - a[1]):
                if b[0] - a[0] != 0 and b[1] - a[1] != 0:   #warunek zeby nie sprawdzac dla tego samego puntu
                    print("Kordynaty pierwszego gońca: " + str((a[0], a[1])),
                          "Kordynaty drugiego gońca: " + str((b[0], b[1])))
                    c+=1
    if c == 0:
        print("Zadne gonce sie nie bija")
    if c==2:
        print("Dokladnie dwa gonce sie bija")
    if c>2:
        print("Bija sie ponad dwa gonce")

'''
run=True
while(run):
    n=int(input("Podaj ile gońców chcesz na szachownicy? "))
    if n <= 1 or n > 99:
        print("Wprowadź ilosc goncow pononwie")
        run=True
    else:
        run=False

dane=[] #w formie (posx,posy), generujemy wspolrzedne korzystajac z klasy w petli for 
for i in range(n):
    bishop=Bishop("bishop",random.randint(1,100),random.randint(1,100))     #1,100 z tresci zadania
    dane.append((bishop.posx,bishop.posy))
print(dane)
'''

test_1=[(3,6),(7,4),(3,1)]  #zadne sie nie szachuja, https://lichess.org/editor/B7/8/6B1/8/8/8/5B2/8_w_-_-_0_1?color=white
test_2=[(3,6),(6,3),(3,1)]  #dokladnie dwa sie szachuja, https://lichess.org/editor/8/2B5/5B2/8/8/2B5/8/8_w_-_-_0_1?color=white
test_3=[(3,6),(6,3),(5,4)]  #wiecej niz dwa sie szachuja, https://lichess.org/editor/8/8/5B2/4B3/8/2B5/8/8_w_-_-_0_1?color=white

check(test_2)


