'''
Zadanie 11
Wykorzystując funkcje, proszę napisać program, który będzie kalkulatorem dla funkcji trygonometrycznych: sin(), cos(), tg(), ctg().
Wartości tych funkcji powinne być zapisane i odczytywane z pliku na potrzeby wykonywanych obliczeń. Należy uwzględnić następujące wartości:
0, 30, 45, 60, 90, 180, 360.
'''

def kalkulator_trygo():     #zmiany w txt będą wprowadzane do tablicy
    with open("C:\\Users\\Nikodem\\Desktop\\tabelka_trygonometryczna.txt" , "r") as f:      #otworzyc z opcja, r - czyli read
        tab = [k.strip() for k in f.readlines()]
        tab = [i.split('=') for i in tab]
    return tab

def kontynuacja():          #definicja potrzebna gdyby uzytkownik chcial kontynuowac
    while(1):               #petla odbywa sie dopoki nie strigerruje sie brake/return/exit statement
        pytanie = input("Czy chce Pan/Pani wprowadzic nowe dane? Proszę wprowadzić T albo N. ")
        if pytanie =="T" or pytanie =="t":
            return True
        if pytanie =="N" or pytanie =="n":
            return exit("Dziękuję za użycie kalkulatora. ")
        else:
            print("Proszę sprobowac jeszcze raz")

wartosci=kalkulator_trygo()

run=True
mozliwe_katy=[0, 30, 45, 60, 90, 180, 360]
operatory=["+","-","*","/"]
i=0     #rozdzielamy petle while na dwa przejscia
while(run):
    if i%2==0:
        funkcja=str(input("Proszę podać funkcję trygonometryczną: "))
        kat=int(input("Proszę podać kąt funkcji: 0, 30, ,45, 60, 90, 180, 360. Albo kąty przesunięte o okres danej funkcji. "))
        if funkcja=="sin":
            while (kat<0 or kat>360):
                if kat>360:
                    kat=kat-360
                if kat<0:
                    kat=kat+360
            if kat not in mozliwe_katy:
                print("Kat nie nalezy do zbioru. ")
                continue
        elif funkcja=="cos":
            while (kat<0 or kat>360):
                if kat>360:
                    kat=kat-360
                if kat<0:
                    kat=kat+360
            if kat not in mozliwe_katy:
                print("Kat nie nalezy do zbioru. ")
                continue
        elif funkcja=="tg":
            if kat==90 or kat==270:
                print("Podano zły kąt proszę wprowadzić, ponownie. ")
                continue  # tu moze tez byc exit, ale continue jest fajniejsze bo mozemy znowu wpisac dana funkcje trygo
            else:
                while (kat<0 or kat>360):
                    if kat>360:
                        kat=kat-180
                    if kat<0:
                        kat=kat+180
                if kat not in mozliwe_katy:
                    print("Kat nie nalezy do zbioru. ")
                    continue
        elif funkcja=="ctg":
            if kat==0 or kat==180:
                print("Podano zły kąt proszę wprowadzić, ponownie. ")
                continue  # tu moze tez byc exit, ale continue jest fajniejsze bo mozemy znowu wpisac dana funkcje trygo
            else:
                while (kat<0 or kat>360):
                    if kat>360:
                        kat=kat-180
                    if kat<0:
                        kat=kat+180
                if kat not in mozliwe_katy:
                    print("Kat nie nalezy do zbioru. ")
                    continue
        else:
            print("Źle podano nazwę funkcji")
            continue

    funkcjaFinal = f'{funkcja}({kat})'
    for x in wartosci:
        if funkcjaFinal in x:
            wartosc = float(x[1])
            if i==0:
                wynik=wartosc
            else:
                if operator not in operatory:
                    exit("Podano zły operator")
                if operator=="+":
                    wynik=wynik+wartosc
                if operator=="-":
                    wynik=wynik-wartosc
                if operator=="/":
                    wynik=wynik/wartosc
                if operator=="*":
                    wynik=wynik*wartosc
                print(wynik)
                run = kontynuacja()
            i=i+1
    else:
        operatory=["+", "-", "*", "/"]
        while(1):
            operator=input("Prosze podac operator dzialania: ")
            try:
                if operator not in operatory:
                    raise ValueError
            except ValueError:
                operator = input("Prosze podac operator dzialania: ")
            else:
                break
        i=i+1


'''
PRZYPADKI TESTOWE I WYJASNIENIA:
1. Wyglad listy po imporcie z pliku jest pokazany w pliku podporka_do_11.py.
2. Przykładowe dzialanie przyblizone kalkulatorem internetowym:
[(sin720 + cos360)*tg45 - ctg90+sin(-270)]/cos(60) = 4 
3. Co się stanie gdy użyjemy, tg90, ctg180?
4. Co się stanie gdy okaże się, że kąt po obróbce nie należy do puli tych, ktore obslugujemy? Np. sin(680)=sin(320)
5. Co jesli zle wprowadzimy operator? Sprawdzić np. input: 'krowa', '++'  Albo gdy wprowadzimy złą nazwę funkcji.
'''
