def dzielenie(liczba):
    dzielniki=[]
    if liczba>0:
        for dzielnik in range(1,int(liczba/2)+1):       #sprawdzamy  w zakresie do polowy liczby bo dalej sa warrtosci niecalkowite
            if liczba % dzielnik==0:
                dzielniki.append(dzielnik)
                dzielniki.append(dzielnik*-1)
        dzielniki.append(liczba)
        dzielniki.append(liczba*-1)
        dzielniki.sort()
        print(str(dzielniki))
    elif liczba<0:
        for dzielnik in range(int(liczba/2), 0):
            if liczba % dzielnik==0:
                dzielniki.append(dzielnik)
                dzielniki.append(dzielnik * -1)
        dzielniki.append(liczba)
        dzielniki.append(liczba*-1)
        dzielniki.sort()
        print(str(dzielniki))
    else:
        print("0 ma nieskończenie wiele dzielników")

run=True
while(run):
    x = input("Wprowadz swoją liczbę, a program wypisze jej całkowite dzielniki: ")
    try:
        val = int(x)
    except ValueError:
        print("Nie wprowadzono liczby całkowitej, proszę spróbować ponownie.  ")
    else:
        x=int(x)    #program wyrzucal definicje, bo traktowal x zdefiniowanego w lini 26 jako stringa
        run=False
        dzielenie(x)
