print("Min Max")

t= [14, 101, 211, 13, 25, 3, 10, 28, 101, 3]
min = t[1]
max = t[1]

for i in t:
    if i < min:
        min = i
    elif i > max:
        max = i
print(f"Le minimum est {min}, le maximum est {max}")


# DEBUT
# Soit t un tableau de 10 entiers
# Soit min = t[1]
# Soit max = t[1]

# Pour i de 0 à 9
# 		Si t[i] < min 
# Alors min = t[i]
# 		Sinon Si t[i] > max
# 			Alors max = t[i]
# 		Fin Si
# Fin Pour
# afficher Le minimum est min, le maximum est max
# FIN