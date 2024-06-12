print("Pair ou Impaire")
t = [27, 4, 666, 101, 211, 7, 3, 28, 9, 0]

for i in t:
    if i % 2 == 0:
        print(f"{i} est pair")
    else:
        print(f"{i} est impair")


while i <9:
    if t[i] % 2 == 0:
                print(f"{t[i]} est pair")
    else:
        print(f"{t[i]} est impair")
    i += 1



#     Pseudo-Code:

# DEBUT
# Soit un tableau t de 10 entiers

# Pour i allant de 0 à 9
# 	Si le reste de t[i] / 2 égal 0
# 		Alors afficher t[i] est pair
# 		Sinon afficher t[i] est impair
# fin Pour
# FIN



# DEBUT
# Soit un tableau t de 10 entiers

# Tant que i < 9
# 	Si le reste de t[i] / 2 égal 0
# 		Alors afficher t[i] est pair
# 		Sinon afficher t[i] est impair
# 	i = i + 1
# fin Tant que
# FIN