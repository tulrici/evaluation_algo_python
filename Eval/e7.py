print("calculette")

#initialisation et demande premier nombre ou quit
inputValue = ""
inputValue2 = ""
inputValue = input("Entrer un nombre réel ou q pour quitter ")
if inputValue == "q":
    exit()
else:
    value1 = float(inputValue)

while True:
# reinitilisation
    inputValue1 = ""
    inputValue1Str = str(inputValue1)

    while inputValue1Str != '+' and inputValue1Str != '-' and inputValue1Str != '*' and inputValue1Str != '/' and 'q' :
# demande opération et test ou quit
        inputValue1 = str(input("Entrer une opération ( + , - , * , / ) ou q pour quitter "))
        inputValue1Str = str(inputValue1)

    if inputValue1 == "q":
        exit()
    else:
        op = inputValue1

    while True:
# demande deuxieme nombre ou quit
        inputValue2 = input("Entrer un nombre réel ou q pour quitter ")
        if inputValue2 == "q":
            exit()
        else:
            value2 = float(inputValue2)

        if op == "+":
            result = value1 + value2
        elif op == "-":
            result = value1 - value2
        elif op == "*":
            result = value1 * value2
        elif op == "/":
            if value2 == 0:
# test division par 0
                print("Vous allez en prison des maths parce qu'on divise pas par zéro quand est civilisé ")
                continue
            else:
                result = value1 / value2

        print(f"Resultat : {result}")
        value1 = result
        break
