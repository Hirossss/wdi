'''
Najpierw uzytkownik podaje swoje dwie liczby a program pozniej wykonuje na nich podstawowe dzialania
'''
print("Wprowadź dwie liczby a program wykona na nich podstawowe działania")
liczba1 = float(input("Podaj liczbę pierwszą: "))
liczba2 = float(input("Podaj liczbę drugą: "))

if liczba1<0 and liczba2<0:                                                    #zabezpieczenie przed użyciem dwoch liczb <0
    exit("Program nie działa gdy obie podane liczby są mniejsze od zera")
elif liczba1<0:                                                                 #zamiana liczby ujemnej na jej wartosc absolutna w razie potrzeby
    liczba1 = abs(liczba1)
    print("Podałeś liczbę nr 1 mniejszą od zera, więc program skorzysta z jej modułu do dalszych obliczeń")
elif liczba2<0:
    liczba2 = abs(liczba2)
    print("Podałeś liczbę nr 2 mniejszą od zera, więc program skorzysta z jej modułu do dalszych obliczeń")

suma = liczba1 + liczba2                                    #od tej linijki beda definiowane dzialania
print("Suma liczb to: " +str(suma))
roznica = liczba1 - liczba2
print("Roznica liczb to: " +str(roznica))
iloczyn = liczba1 * liczba2
print("Iloczyn liczb to: " +str(iloczyn))
if iloczyn == 10:                                           #specjalna instrukcja gdy iloczyn jest rowny 10
    print("Yay")
iloraz = liczba1/liczba2
print("Iloraz liczb to: " +str(iloraz))
kwadrat_liczb = pow(liczba1, 2) , pow(liczba2, 2)
print("Kwadraty kolejno liczby nr 1 i liczby nr 2 to: " +str(kwadrat_liczb))
pierwiastek_liczb = pow(liczba1, 1/2), pow(liczba2, 1/2)
print("Pierwiastek kolejno liczby nr 1 i liczby nr 2 to: "+str(pierwiastek_liczb))




