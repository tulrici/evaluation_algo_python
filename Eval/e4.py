print("Notes")

t = [11, 16.5, 8, 4, 16, 18,5, 3, 0, 10, 20]
n = int(0)
for i in t:
    if i >= 10:
        n += 1
print(f"{n} étudiants ont eu la moyenne")


# Pseudo-Code:

# DEBUT
# Soit un tableau t de 10 notes (réels)
# Soit n = 0 (entier)
# Pour i de 0 à 9
# 	Si t[i] est supérieur ou égal à 10 
# 		Alors nombre n égal n + 1
# Fin Pour

# afficher t étudiants ont eu la moyenne
# FIN