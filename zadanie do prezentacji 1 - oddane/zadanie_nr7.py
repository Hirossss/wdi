def dzielenie(liczba):
    dzielniki=[]
    if liczba>0:
        for dzielnik in range(1,int(liczba/2)+1):   #sprawdzamy w zakresie do połowy liczby, bo dalej są wartości niecałkowite
            if liczba % dzielnik==0:
                dzielniki.append(dzielnik)          #dzielniki aplikujemy do listy, żeby wynik programu ładnie wyglądał
                dzielniki.append(dzielnik*-1)
        dzielniki.append(liczba)                    #uwzględniamy również samą liczbę, bo nie "przechodzi" ona przez petlę
        dzielniki.append(liczba*-1)
        dzielniki.sort()
        print(str(dzielniki))
    elif liczba<0:
        for dzielnik in range(int(liczba/2), 0):    #wszystkie dzieje sie analogicznie, ale istotna jest kolejność zakresów!
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
while(run):         #nieskończona pętla z instrukcją try, except, else, aby zoptymalizować użytkowanie programu
    x = input("Wprowadz swoją liczbę, a program wypisze jej całkowite dzielniki: ")
    try:
        val = int(x)    #sprawdzamy czy input jest liczbą całkowitą zgodnie z przeznaczeniem programu, zabezpieczamy się przed użyciem złej zmiennej
    except ValueError:
        print("Nie wprowadzono liczby całkowitej, proszę spróbować ponownie. ")  #run jest nadal True i użytkownik może ponownie wprowadzać wartości do x aż wprowadzi argument całkowity
    else:
        x=int(x)    #trzeba dorzucić typ int, bo funkcja dzielenie nie zadziała ze stringiem określonym w lini 26
        run=False   #nie chcemy, żeby pętla się dalej wykonywała
        dzielenie(x)    #wywołujemy funkcję i koniec
