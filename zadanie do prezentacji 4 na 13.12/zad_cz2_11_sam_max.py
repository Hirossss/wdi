import random

def generate_dane(n):                               #funkcja wypłeniająca listę losowymi liczbami
    n=n+1
    dane = []
    for i in range(n):
        dane.append(random.randint(0, 10))
    print(dane)
    return dane

def max_rekurencyjny(tab):                          #maksymalny element listy rekurencyjnie
    if len(tab)==0:
        return None
    if len(tab)==1:
        return tab[0]
    else:
        m=max_rekurencyjny(tab[1:])
        print(m)                            #zapetlamy sie w rekurencji, wywolujemy kolejne m az do ostatniego elementu w liscie
        print(tab)
        return m if m > tab[0] else tab[0]

b=max_rekurencyjny(generate_dane(5))
print("Maks to: "+str(b))
