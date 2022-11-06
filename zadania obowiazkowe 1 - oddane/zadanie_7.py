x = int(input("Podaj liczbę całkowitą będącą jedną z granic zakresu: "))
y = int(input("Podaj liczbę całkowitą będącą drugą z granic zakresu: "))

if x>y:
    liczba_gorna=x
    liczba_dolna=y
elif x<y:
    liczba_gorna=y
    liczba_dolna=x
else:
    exit("Proszę podać dwie róźne liczby!")

srednia = int((liczba_gorna+liczba_dolna)/2)

if (liczba_gorna-liczba_dolna+1)>20:
    for a in range(3):
        print(str(srednia-(a+1)))
        print(str(srednia+(a+1)))

else:
    for i in range(liczba_gorna-liczba_dolna+1):
        print(liczba_dolna+i)






