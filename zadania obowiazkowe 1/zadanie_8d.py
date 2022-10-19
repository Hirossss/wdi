h = int(input("Podaj jak długa ma być twoja choinka: "))

if h<0:
    exit("Proszę podać liczbę całkowitą nieujemną")
elif h==0:
    exit("Wysokość twojej choinki jest równa 0")
else:
    print((h-1)*" "+"X")                                      #trzeba bylo odlaczyc ten i ponizszy wiersz zeby reszta dzialala wedlug petli
    print((h-2)*" "+"o**")
    for i in range(h-1):                                      #w tej calej petli przejscie dla i=0 nie odbywa sie w ogole (nie wiem jak to zaimplementowac wiec wymusilem to ifem
        if i%2==0 and i>1:
            print((h-(i+2))*" "+"*"*(i-1)+"o"+"*"*(i+3))
        elif i>0:
            print((h - (i + 2)) * " " + "*" * (i + 2) + "o" +"*"*(i))

    print((h-1)*" "+"U")










