'''
Proszę napisać program, który wypełnia N-elementową listę trzycyfrowymi liczbami pseudolosowymi
a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w liście,
dla którego w liście występuje również rewers tego ciągu.
'''
import random
import math

def ciagi(n):   #wyszukuje jak dlugi jest najdluzszy rewers podciagu w liście
    lista=[]
    for i in range(0, n-1):
        lista.append(random.randint(1,15))
    suma=0
    for k in range(0, n-1):   #chcemy miec pewnosc, ze beda liczby trzycyfrowe w liscie
        napis = str(lista[k])
        dlugosc = len(napis)
        suma=dlugosc+suma
    if suma % 3 == 1:
        lista.append(random.randint(10,15)) #dodajemy dwucfyrowa
    elif suma % 3 == 2:
        lista.append(random.randint(1, 9))  #dodajemy jednocyfrową

    print(lista)
    lista_odwrocona=lista.copy()    #tworzymy kopie listy i ja odwracamy by ulatwic szukanie rewersu
    lista_odwrocona.reverse()
    print(lista_odwrocona)
    ##print(lista_odwrocona)

    temp=0
    maksimum=0
    for i in range(len(lista)):
        for ii in range(n-1, i, -1):
            for j in range(len(lista_odwrocona)):
                for jj in range(n-1, j, -1):
                    if lista[i:ii]==lista_odwrocona[j:jj]:
                        temp=(len(lista[i:ii]))
                        if temp>maksimum:
                            maksimum=temp
    print("Dlugosc szukanego ciagu to " +str(maksimum))

print("Proszę podać liczbę naturalną n, a program wygeneruje listę wypełniona trzycyfrowymi liczbami pseudolosowymi o podanej długości n. ")
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