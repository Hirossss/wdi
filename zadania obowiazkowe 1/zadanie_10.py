import random
import math

def kontynuacja():          #definicja potrzebna gdyby uzytkownik chcial kontynuowac
    while(1):               #petla odbywa sie dopoki nie strigerruje sie brake/return/exit statement
        pytanie = input("Czy chce Pan/Pani wprowadzic nowe dane? Proszę wprowadzić T albo N. ")
        if pytanie =="T" or pytanie =="t":
            return True
        if pytanie =="N" or pytanie =="n":
            return False
        else:
            print("Proszę sprobowac jeszcze raz")

run = True  #kiedy program ma chodzic (kontynuacja)
while(run):
    print("Kalkulator wykonuje: + (dodawanie), - (odejmowanie), * (mnożenie), / (dzielenie), ^ (potegowanie), # (pierwiastkowanie), x (losowanie)")
    print("Bierze on pierwszą liczbę i wykonuje działania zaczynając od niej. ")
    pierwsza = int(input("Proszę podać pierwszą liczbę do działań. "))
    liczby=[]   #tu bedziemy przechowywac liczby wprowadzone przez uzytkownika
    wprowadzanie=True
    while(wprowadzanie):
        nowe_liczby=(input("Proszę podać kolejne liczby do działań, potwierdzając przyciskiem enter. Na koniec wprowadzić symbol operacji, która ma wykonać kalkualtor na liczbach i potwierdzić przyciskiem enter.  "))
        try:
            wartosc = int(nowe_liczby)
        except ValueError:  #wtedy gdy zostanie wprowadzony znak dzialania zamiast liczby do zbioru, to ...
            if (nowe_liczby == "+"):
                for i in liczby:
                    pierwsza=pierwsza+i
                print("Suma liczb to: "+str(pierwsza))
                pierwsza=0
                wprowadzanie = False #wyjscie z petli by moc ew. od nowa wpisac pierwsza liczbe do programu
                run = kontynuacja()
            elif (nowe_liczby == "-"):
                for i in liczby:
                    pierwsza=pierwsza-i
                print("Róznica liczb to: "+str(pierwsza))
                pierwsza=0
                wprowadzanie=False
                run = kontynuacja()
            elif (nowe_liczby == "*"):
                for i in liczby:
                    pierwsza=pierwsza*i
                print("Iloczyn liczb to: "+str(pierwsza))
                pierwsza=0
                wprowadzanie=False
                run = kontynuacja()
            elif (nowe_liczby == "#"):
                for i in liczby:
                    pierwsza=pow(pierwsza, 1/i)
                print("Pierwiastek liczb to: "+str(pierwsza))
                pierwsza=0
                wprowadzanie=False
                run = kontynuacja()
            elif (nowe_liczby == "^"):
                for i in liczby:
                    pierwsza=pow(pierwsza, i)
                print("Wynik potęgowania liczb to: "+str(pierwsza))
                pierwsza=0
                wprowadzanie=False
                run = kontynuacja()
            elif (nowe_liczby == "x"):
                for i in liczby:
                    print("Losową liczbą z przedziału od pierwszej liczby aż do "+str(i)+" jest: " +str(random.randint(pierwsza, i)))
                pierwsza=0
                wprowadzanie=False
                run = kontynuacja()
            else:
                print("Wprowadzono niepoprawny znak. ")     #wprowadzenie ma nadal wartosc logiczna true wiec petla wroci do pytania o liczbe
        else:
            liczby.append(int(nowe_liczby))







