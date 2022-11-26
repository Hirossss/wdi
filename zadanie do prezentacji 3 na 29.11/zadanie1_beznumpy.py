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

wiersze=int(input("Prosze podac ilosc wierszy: "))
kolumny=int(input("Prosze podac ilosc kolumn: "))
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
print(mat1)
mat2= tworzenieMacierzy(wiersze,kolumny,liczbyLosowe2)
print(mat2)

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
PRZYPADKI TESTOWE I WYJASNIENIA:

'''




