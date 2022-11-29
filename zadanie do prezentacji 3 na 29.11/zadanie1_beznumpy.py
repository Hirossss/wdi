'''
Zadanie 1.
Proszę napisać program wczytujący dwie macierze o ustalonych wymiarach mxn.
Dla wczytanych macierzy należy wykonać operacje: dodawania oraz odejmowania dwóch macierzy.
Wymiar macierzy powinien być definiowany przez użytkownika.
'''
import random
def tworzenieMacierzy(w, k, dane):
    mat = []
    for i in range(w):
        listaWierszy = []
        for j in range(k):
            listaWierszy.append(dane[w * i + j])#niestety nie uzywamy wszystkich liczb z "dane", ale ciezko to zrobic bardziej optymalnie
        mat.append(listaWierszy)
    return mat
run=True
while(run):
    wiersze=input("Prosze podac ilosc wierszy: ")
    kolumny=input("Prosze podac ilosc kolumn: ")
    try:
        x=int(wiersze)
        y=int(kolumny)
    except ValueError:
        print("Prosze podac parametry ponownie")
    else:
        run=False

wiersze=int(wiersze)
kolumny=int(kolumny)

if wiersze > kolumny:
    n=wiersze
elif kolumny > wiersze:
    n=kolumny
else:
    n=wiersze
liczbyLosowe1=[]
liczbyLosowe2=[]
for i in range(0, n*n):
    liczbyLosowe1.append(random.randint(0,9))
    liczbyLosowe2.append(random.randint(0, 9))

mat1= tworzenieMacierzy(wiersze,kolumny,liczbyLosowe1)
mat2= tworzenieMacierzy(wiersze,kolumny,liczbyLosowe2)

print("To jest pierwsza macierz. ")
for p in range(wiersze):
    print(mat1[p])
print("To jest druga macierz. ")
for l in range(wiersze):
    print(mat2[l])

wynik_dod=[[0]*kolumny for i in range(wiersze)] #wypelniamy dana liste zerem * ilos kolumn, powtarzamy dla n wierszy
wynik_odej=[[0]*kolumny for i in range(wiersze)]

for a in range(wiersze):
    for b in range(kolumny):
        wynik_dod[a][b]=mat1[a][b]+mat2[a][b]
        wynik_odej[a][b]=mat1[a][b]-mat2[a][b]

print("Wynik dodawania macierzy to macierz: ")
for k in range(wiersze):
    print(wynik_dod[k])
print("Wynik odejmowania macierzy to macierz: ")
for j in range(wiersze):
    print(wynik_odej[j])
'''
PRZYPADKI TESTOWE
1. Zabezpieczenie przed podaniem zlych parametrow.
'''




