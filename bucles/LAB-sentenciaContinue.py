#Crear un devorador de vocales


user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for letra in user_word:
    if letra in "AEIOU":
        continue
    print(letra)