print("Présence dans un tableau")
t= [14, 101, 211, 13, 25, 3, 10, 28, 101, 3]
n = int(input("Vueillez ecrire un entier "))
c = 0

for i in t:
    if i == n:
        c += 1
if c == 0:
    print(f"{n} n'est pas présent dans le tableau t")
else:
    print(f"{n} est présent {c} fois dans le tableau t")


#     DEBUT
# Soit un tableau de 10 entiers
# Saisir un entier n
# Soit c = 0

# Pour i allant de 0 à 9
# 	Si t[i] = n
# 		Alors c = c +1
# Fin Si
# Fin Pour

# Si c = 0
# 	Alors afficher n n’est pas dans présent dans le tableau t
# Sinon
# 	Afficher n est présent c fois dans le tableau t
# Fin Si
# FIN
