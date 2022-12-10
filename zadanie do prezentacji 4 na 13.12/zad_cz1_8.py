'''
Zadanie 8.
Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy struktury:
 dane = [(x1, y1), ( x2, y2), (x3, y3), ..., (xN, yN)]
Proszę napisać funkcję, która zwraca wartość True jeżeli w zbiorze istnieją 3 punkty wyznaczające trójkąt równoboczny,
wewnątrz którego nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie punktów.
'''

import random
import math

#a,b,c przyjmuje jako koordynaty czyli postac: (x,x)

def distance(a, b):
    return round(math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2)), 2)

def area(a, b, c):  # pole trójkąta
    return round(abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0),3)

def is_eq_triangle(a,b,c):  #czy trojakt rownoboczny?
    if distance(a,b) == distance(b,c) and distance(b,c) == distance(a,c) and distance(c,a) == distance(a,b):
        return True
    else:
        return False

def arepoints_inside(a, b, c, dane):  # czy w trójkącie sa punkty w srodku?
    for i in dane:
        if i != a and i != b and i != c:
            if area(a, b, c) == area(a, b, i) + area(a, c, i) + area(b, c, i):# pole trójkąta = suma pól trójkątów, jeżeli jest równa to punkt jest wewnątrz
                return False
            else:
                return True

def eq_triangles(dane):  #final programu, zwracamy True albo False, powiazanie wszystkich definicji
    for i in dane:
        for j in dane:
            for k in dane:
                if is_eq_triangle(i, j, k):  # sprawdzenie czy trojkat jest rownoboczny
                    if arepoints_inside(i, j, k, dane): #gdy sa takie punkty to sprawdzamy reszte danych --> def arepoints_inside
                        return True
    return False

def generate_dane(n):       #na razie nie uzywamy tej funkcji
    dane = []
    for i in range(n):
        dane.append((random.randint(0, 100), random.randint(0, 100)))
    return dane

data: float = [(1,1),(4,-2),(-0.1,-3.1),(1,-1.5)]
a=eq_triangles(data)
print(a)


'''
SPOSTRZEŻENIA I UWAGI:
1. Nie istnieje trojkat rownoboczny na samych współrzędnych całkowitych,
więc tutaj mamy pierwszą słabość programu gdy dobieramy współrzędne całkowite. Muszę dokonać zaokrąglenia co znowu mocno
utrudnia znalezienie takiego trójkąta. Pokazac to na przykladzie z def generate_dane
2. Nawet jeśli znajdziemy gotowca, to musimy takowy wynik zaokrąglić, wynika to z właściwości pierwiastka z liczby niewymiernej.
3. Najciekawszym i najważniejszym punktem programu jest sprawdzanie czy punkt leży wewnątrz trójkąta?
4. Sprawdzic program dla 4 wspolrzednej: (1,-1.68) i (1,-1.69), (1.8,0) i (1.9,0), (2,-2) i (2, -1.84) by pokazac niedokladnosc!
5. Mozna sie bawic zaokragleniami def area ale zawsze znajdziemy taki punkt ze program nie dziala precyzyjnie. 
'''


