import numpy as np
import random
ile_wierszy=int(input("Prosze podac ilosc wierszy dla macierzy: "))
ile_kolumn=int(input("Prosze podac ilosc kolumn: "))

a=np.random.randint(9, size=(ile_wierszy,ile_kolumn))
b=np.random.randint(9, size=(ile_wierszy,ile_kolumn))

c1=a+b
c2=a-b
print("Pierwsza wygenerowana macierz to: ")
print(a)
print("Druga wygenerowana macierz to: ")
print(b)

print("Wynik dodawania maciery to: ")
print(c1)
print("Wynik odejmowania maciery to: ")
print(c2)

