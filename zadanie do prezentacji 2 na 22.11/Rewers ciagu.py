'''
Proszę napisać program, który wypełnia N-elementową listę trzycyfrowymi liczbami pseudolosowymi
a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w liście,
dla którego w liście występuje również rewers tego ciągu.
'''
import random
import math

def ciagi(n):   #wyszukuje jak dlugi jest najdluzszy rewers podciagu w liście
    lista=[]
    '''
    Poniższa część programu przygotowuje listę tak jak to mniej więcęj wygląda w przykładzie polecenia. 
    Jest to zabieg kosmetyczny, sprawia że częściej znajdujemy rewersy ciągów. 
    '''
    for i in range(0, n-1):
        lista.append(random.randint(100,999))   #mozna sie bawic tym rangem i de facto to od niego zalezy czy znajdziemy te rewersy
    suma=0
    for k in range(0, n-1):
        napis = str(lista[k])
        dlugosc = len(napis)
        suma=dlugosc+suma
    if suma % 3 == 1:
        lista.append(random.randint(10,99)) #dodajemy dwucfyrowa
    elif suma % 3 == 2:
        lista.append(random.randint(1, 9))  #dodajemy jednocyfrową

    print(lista)
    '''
    GŁÓWNA CZĘŚĆ ROZWIĄZANIA ZACZYNA SIĘ OD TEGO KROKU 
    '''
    lista_odwrocona=lista.copy()    #tworzymy kopie listy i ja odwracamy by ulatwic szukanie rewersu
    lista_odwrocona.reverse()
    #print(lista_odwrocona)

    '''
    POSZUKIWANA REWERSU
    '''
    temp=0
    maksimum=0
    for i in range(len(lista)):                                 # indeks poczatkowy pierwotnej
        for ii in range(n-1, i, -1):                            # indeks koncowy pierwotnej
            for j in range(len(lista_odwrocona)):               # indeks poczatkowy zreversowanej
                for jj in range(n-1, j, -1):                    # indeks koncowy zreversowanej
                    if lista[i:ii]==lista_odwrocona[j:jj]:      # jeśli się pokryją to ..., może być palindromem
                        temp=(len(lista[i:ii]))
                        if temp>maksimum:                       # znajdujemy największy rewers
                            maksimum=temp
    print("Dlugosc szukanego ciagu to " +str(maksimum))

print("Proszę podać liczbę naturalną n, a program wygeneruje listę wypełniona trzycyfrowymi liczbami pseudolosowymi o podanej długości n, \n a następnie wyszuka najdłuższy rewers spójnego ciągu w liście.  ")
run=True
while run:
    n= input("Proszę podać długość listy: ")
    try:
        value=int(n)
    except ValueError:
        print("Proszę ponownie wprowadzić liczbę")
    else:
        n=int(n)
        ciagi(n)
        run=False

'''
PRZYPADKI TESTOWE
1. Gdy wykonamy zadanie zgodnie z poleceniem czyli range(100, 999) to jest bardzo mała szansa, że znajdziemy rewers.
Można modyfikować ten range do mniejszych liczb by zwiększyć szansę wystąpienia rewersu.
2. Program traktuje palindrom czyli np, 121 jako rewers sam do siebie! 
3. Mam przygotowany przykład z treści zadania w kolejnym programie.
'''