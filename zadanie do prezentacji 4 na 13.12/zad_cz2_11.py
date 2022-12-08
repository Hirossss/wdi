import random

def generate_dane(n):
    n=n+1
    dane = []
    for i in range(n):
        dane.append(random.randint(-10, 100))
    print(dane)
    return dane

def suma_rekurencyjnie(tab):
    if len(tab)==0:
        return 0
    return tab[0] + suma_rekurencyjnie(tab[1:])     #na samym koncu, zwroc ostatni element (czyli aktualna sume) + 0

def max_rekurencyjny(tab):
    if len(tab)==0:
        return None
    if len(tab)==1:
        return tab[0]
    else:
        m=max_rekurencyjny(tab[1:])
        #print(m)                                    #zapetlamy sie w rekurencji, wywolujemy kolejne m az do ostatniego elementu w liscie
        #print(tab)
        return m if m > tab[0] else tab[0]

a=suma_rekurencyjnie(generate_dane(5))
print("Suma to: "+str(a))

b=max_rekurencyjny(generate_dane(5))
print("Maks to: "+str(b))