print("Elections")

p = float(input("Vueiller renseigner le pourcentage des voix obtenues "))
print(f"p = {p}%")

if p < 5:
    print("Candidat éliminé")
elif p < 50:
    print("Candidat qualifié au second tour")
else:
    print("candidat élu")



#Pseudo-Code:

# DEBUT
# saisir un nombre réel p
# afficher p

# Si p < 5
# 	Alors afficher candidat éliminé
# Sinon Si p < 50
# 	Alors afficher candidat qualifié pour le second tour
# Sinon afficher candidat élu
# Fin Si
# FIN
