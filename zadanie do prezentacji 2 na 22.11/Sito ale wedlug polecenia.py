'''
Zadanie 2.
Proszę napisać program, który metodą sita Eratostenesa wyznaczy liczby pierwsze mniejsze od N (wczytywane).
Należy obsłużyć wyjątek wczytania liczby, która nie jest naturalna i podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych,
przy założeniu, że dzielimy większą liczbę przez mniejszą.
'''

import math

def sito(n):
    pierwsze=[]
    ile_liczb = 0
    liczby = [True] * (n)   #ustawiamy wartość logiczną wszyskitch indeksów w liście na  True
    for i in range(2, int(math.ceil(math.sqrt(n)))):    #sprawdzanie do pierwiastka danego zakresu jest optymalne, bo nie wyjdziemy poza zakres "n"
        if liczby[i]:
            for j in range(i*i, n, i):  #zaczynamy od wielokrotności i*i, bo np. 2*1 nie opłaca się (od razu sprawdzone), np. 3*1, 3*2 (sprawdzone wcześniej) nie opłaca się. Opłaca się zacząć sprawdzanie od 2*2, później od razu 3*3 itd.
                liczby[j]=False #wszystkie wielokrotności i ustawiamy na False

    for i in range(2, n):
        if liczby[i]:           #kiedy jest pierwsza to ...
            pierwsze.append(i)  #chcemy dodawać tylko wartości logiczne True, czyli liczby pierwsze
            ile_liczb+=1
    print("Liczby pierwsze w zakresie od 2 do " +str(n)+ " to : " +str(pierwsze), end='\n')
    print("Tyle jest liczb pierwszych w tym zakresie: " + str(ile_liczb))
    # c.d. podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych, przy założeniu, że dzielimy większą liczbę przez mniejszą

    for k in range(0, ile_liczb-1):
        a = pierwsze[k+1] // pierwsze[k]    #dzięki "//" dostajemy część całkowitą
        b = pierwsze[k+1] % pierwsze[k]     #dostajemy resztę
        print("Dzielenie "+str(pierwsze[k+1])+ " przez "+str(pierwsze[k])+" daje iloraz całkowity "+str(a),"oraz resztę " +str(b))

print("Program metodą sita Eratostenesa wyznaczy liczby pierwsze mniejsze od n (gdzie n to liczba wprowadzona przez użytkownika).")
run=True
while run:
    n = input("Proszę podać liczbę naturalną większą lub równą 2: ")
    try:
        value=int(n)
    except ValueError:
        print("Podana wartośc nie jest liczbą naturalna! Proszę podać liczbę ponownie! ")
    else:
        n=int(n)
        if n<2:
            print("Podana liczba nie jest naturalna albo jest mniejsza od 2. Proszę podać liczbę ponownie! ")
        elif n==2:
            print("Liczba 2 jest najmniejszą liczbą pierwszą. ")
            run=False
        else:
            run=False
            sito(n)

'''
PRZYPADKI TESTOWE
1. Przy podaniu n= 108: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 101 103 107
2. http://liczbypierwsze.pl/pierwsze.htm --> liczby pierwsze w danym zakresie
Do 10 000 powinno byc ich 1229 
3. W zakresie do 1 000 000 powinno byc ich 78 498. Co sie stało z konsolą?
'''


