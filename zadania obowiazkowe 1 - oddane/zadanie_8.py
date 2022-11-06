h = int(input("Podaj jak długa ma być twoja choinka: "))

if h<0:
    exit("Proszę podać liczbę całkowitą nieujemną")
elif h==0:
    exit("Wysokość twojej choinki jest równa 0")
else:
    for i in range(h):
        print((h-(i+1))*" "+(2*i+1)*"*")



