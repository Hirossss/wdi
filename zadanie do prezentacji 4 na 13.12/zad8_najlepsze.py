import random
import math

#a,b,c przyjmuje jako koordynaty czyli (x,x)

def distance(a, b):
    return round(math.sqrt(pow(a[0] - b[0],2) + pow(a[1] - b[1],2)), 2)

def area(a, b, c):  # pole trójkąta
    return round(abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0),3)

def is_eq_triangle(a,b,c):
    if distance(a,b) == distance(b,c) and distance(b,c) == distance(a,c) and distance(c,a) == distance(a,b):
        return True
    else:
        return False

def nopoints(a, b, c, dane):  # czy w trójkącie nie ma punktów
    for i in dane:
        if i != a and i != b and i != c:    #tu chyba jest problem
            if area(a, b, c) == area(a, b, i) + area(a, c, i) + area(b, c, i):# pole trójkąta = suma pól trójkątów jeżeli jest równa to punkt jest wewnątrz
                return False
            else:
                return True


def eq_triangles(dane):  #final programu, zwracamy False albo True
    for i in dane:
        for j in dane:
            for k in dane:
                if is_eq_triangle(i, j, k):  # sprawdzenie czy trojkat jest rownoboczny
                    if nopoints(i, j, k, dane):
                        return True
    return False

def generate_dane(n):       # nie wchodzimy na razie do tej funkcji
    dane = []
    for i in range(n):
        dane.append((random.randint(0, 100), random.randint(0, 100)))
    return dane

data: float = [(1,1),(4,-2),(-0.1,-3.1),(0,0)] #nie powinno byc dla (1,-1) True, jak naprawic, tak samo dla (1,0.5), zalezy to od rounda przy distance!!
a=eq_triangles(data)
print(a)

#sprawdzic (1,-1.67) i (1,-1.68) i (1,-0.25)







'''
SPOSTRZEŻENIA I UWAGI:
1. Nie istnieje trojkat rownoboczny na samych współrzędnych całkowitych,
więc tutaj mamy pierwszą słabość programu gdy dobieramy współrzędne całkowite. Muszę dokonać zaokrąglenia co znowu mocno
utrudnia znalezienie takiego trójkąta.
2. Nawet jeśli znajdziemy gotowca, to musimy takowy wynik zaokrąglić, wynika to z właściwości pierwiastka z liczby niewymiernej.
3. Najciekawszym i najważniejszym punktem programu jest sprawdzanie czy punkt leży wewnątrz trójkąta??
'''


