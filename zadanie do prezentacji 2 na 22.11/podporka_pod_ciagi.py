tab=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
tabr=tab.copy()
tabr.reverse()

temp=0
maksimum=0
for i in range(len(tab)):
    for ii in range(15, i, -1):
        for j in range(len(tabr)):
            for jj in range(15, j, -1):
                if tab[i:ii]==tabr[j:jj]:
                    temp=(len(tab[i:ii]))
                    if temp>maksimum:
                        maksimum=temp
print("Dlugosc szukanego ciagu to " +str(maksimum))

'''
Tu chodzi nam o rewers do 9317.
Output powinien być == 4 !
'''