import math
#trzeba zmienic zeby wyswietlalo liczby mniejsze od n (tak jest w tresci zadania) !!!
def sito(n):
    pierwsze=[]
    ile_liczb = 0
    liczby = [True] * (n+1)
    for i in range(2, int(math.ceil(math.sqrt(n)))):            #sprawdzanie dla przykladu 5*5 dla n = 10 wykroczy poza zakres wiec to nie ma sensu
        if liczby[i]:
            for j in range(i*i, n+1, i):                        #przeskakujemy o daną wielokrotność, zaczynajac od i*i (tak najbardziej się opłaca)
                liczby[j]=False

    for i in range(2, n+1):
        if liczby[i]:
            pierwsze.append(i)
            ile_liczb+=1
    print('Licbzy pierwsze w zakresie od 2 do ' +str(n)+ ' to : ' +str(pierwsze), end='\n')
    print("Tyle jest liczb pierwszych w tym zakresie: " + str(ile_liczb))
    # podać ilorazy całkowite i reszty kolejnych wyznaczonych liczb pierwszych, przy założeniu, że dzielimy większą liczbę przez mniejszą
    for k in range(0, ile_liczb-1):
        a = pierwsze[k+1] // pierwsze[k]
        b = pierwsze[k+1] % pierwsze[k]
        print("Dzielenie "+str(pierwsze[k+1])+ " przez "+str(pierwsze[k])+" daje iloraz całkowity "+str(a),"oraz resztę " +str(b))

print("Program służy do znajdywania liczb pierwszych w zakresie do liczby naturalnej podanej przez użytkownika.")
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
            print("Podana liczba nie jest naturalna albo jest mniejsza od 2! Proszę podać liczbę ponownie! ")
        else:
            run=False
            sito(n)


