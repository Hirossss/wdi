'''
Zadanie 11.
Napisz 2 rekurencyjne funkcje do obsługi list.
Pierwsza powinna sprawdzić maksymalny element w liście,
a druga powinna umożliwiać obliczanie sumy elementów listy.
'''

import random

def generate_dane(n):                               #funkcja wypłeniająca listę losowymi liczbami
    n=n+1
    dane = []
    for i in range(n):
        dane.append(random.randint(0, 10))
    print(dane)
    return dane

def suma_rekurencyjnie(tab):                        #suma elementow w liscie rekurencyjnie
    if len(tab)==0:                                 #musimy ustawic warunek "wyjscia z funcji" zeby rekurencja nie trwala w nieskonczonosc
        return 0
    return tab[0] + suma_rekurencyjnie(tab[1:])     #pierwszy element + pierwszy element oraz dalsze pierwsze elementy

def max_rekurencyjny(tab):                          #maksymalny element listy rekurencyjnie
    if len(tab)==0:
        return None
    if len(tab)==1:
        return tab[0]
    else:
        m=max_rekurencyjny(tab[1:])
        #print(m)                            #zapetlamy sie w rekurencji, wywolujemy kolejne m az do ostatniego elementu w liscie
        #print(tab)
        return m if m > tab[0] else tab[0]

a=suma_rekurencyjnie(generate_dane(5))
print("Suma to: "+str(a))

b=max_rekurencyjny(generate_dane(5))
print("Maks to: "+str(b))

'''
WYJAŚNIENIE I PRZYPADKI:
1. Pobawić się randintem i zobaczyć co się dzieje przy dużych liczbach?
2. Przy wyjasnianiu maxa zahashowac reszte, odhashowac "print m" i "print tab", pokazac na przykladach jak dziala zad_cz2_11_podporka.
3. Do rekurencji jest podporka z linkiem do stacka oraz zdjeciem by ulatwic zrozumienie.
'''