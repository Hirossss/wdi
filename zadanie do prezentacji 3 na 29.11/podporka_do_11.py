'''
Oto jak wygląa nasza lista po tym jak ją importujemy z pliku tabelka_trygonometryczna.txt
Schemat: 'funkcja(kat)' , 'wartosc'
'''

def kalkulator_trygo():     #zmiany w txt będą wprowadzane do tablicy
    with open("C:\\Users\\Nikodem\\Desktop\\tabelka_trygonometryczna.txt" , "r") as f:      #otworzyc z opcja, r - czyli read
        tab = [k.strip() for k in f.readlines()]
        tab = [i.split('=') for i in tab]
    print(tab)
kalkulator_trygo()