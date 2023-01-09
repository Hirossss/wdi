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
        return "Zadne gonce sie nie bija"
    if c==2:
        return "Dokladnie dwa gonce sie bija"
    if c>2:
        return "Bija sie ponad dwa gonce"
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
    bishop=Bishop("bishop",random.randint(1,8),random.randint(1,8))     #1,100 z tresci zadania
    dane.append((bishop.posx,bishop.posy))
print(dane)
'''

test_1=[(3,6),(7,4),(3,1)]  #zadne sie nie szachuja, https://lichess.org/editor/B7/8/6B1/8/8/8/5B2/8_w_-_-_0_1?color=white
test_2=[(3,6),(6,3),(3,1)]  #dokladnie dwa sie szachuja, https://lichess.org/editor/8/2B5/5B2/8/8/2B5/8/8_w_-_-_0_1?color=white
test_3=[(3,6),(6,3),(5,4)]  #wiecej niz dwa sie szachuja, https://lichess.org/editor/8/8/5B2/4B3/8/2B5/8/8_w_-_-_0_1?color=white

a=check(test_1)
print(a)
'''
TESTY
'''

#TESTY Z WYKORZYSTANIEM UNITTEST, wystarczy python szachy_do_testow.py
'''
import unittest
class TestCheck(unittest.TestCase):
    def test_czy_gonce_sie_nie_bija(self):
        data = [(3, 6), (7, 4), (3, 1)]
        result = check(data)
        self.assertEqual(result, "Zadne gonce sie nie bija")

    def test_czy_dwa_gonce_sie_atakuja(self):
        data = [(3, 6), (6, 3), (3, 1)]
        result = check(data)
        self.assertEqual(result, "Dokladnie dwa gonce sie bija")

    def test_czy_wiecej_niz_dwa_sie_atakuja(self):
        data = [(3, 6), (6, 3), (5, 4)]
        result = check(data)
        self.assertEqual(result, "Bija sie ponad dwa gonce")

if __name__ == '__main__':
    unittest.main()
'''

#TESTY Z WYKORZYSTANIEM PYTEST, wystarczy run albo pytest -rA szachy_do_testow.py
'''
def test_czy_gonce_sie_nie_bija():
    data = [(3,6),(7,4),(3,1)]
    result = check(data)
    assert result == "Zadne gonce sie nie bija"

def test_czy_dwa_gonce_sie_atakuja():
    data = [(3,6),(6,3),(3,1)]
    result = check(data)
    assert result == "Dokladnie dwa gonce sie bija"

def test_czy_wiecej_niz_dwa_sie_atakuja():
    data = [(3,6),(6,3),(5,4)]
    result = check(data)
    assert result == "Bija sie ponad dwa gonce"
'''

