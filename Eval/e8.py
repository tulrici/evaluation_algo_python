print("tri à bulle")

tab = [11, 34, 65, 904, 3, 5, 0, 211, 101, 13]
v = 0

for i in range(len(tab)):               #parcours du tableau

    for j in range(len(tab) - i - 1):   #parcours du tableau moins l'élement qu'on essaye de ranger moins les éléments déjà rangés
        if tab[j] > tab[j+1]:           #comparaison deux à deux (si le premier est supérieur, on échange leurs places)
            v = tab[j]                  #stockage dans une variable tempon pour permettre l'échange
            tab[j] = tab[j + 1]
            tab[j + 1] = v

print(f"Tableau trié : {tab}")