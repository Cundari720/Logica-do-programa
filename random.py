import random

numero_secreto = random.randint(0,100)
palpite = 0
tentativas = 0

while palpite != numero_secreto:
    palpite = int(input("Adivinhe o número secreto: "))
    if palpite < numero_secreto:
        print("Palpite muito baixo!")
        tentativas += 1
    elif palpite > numero_secreto:
        print("Palpite muito alto!")
        tentativas += 1

print("Parabéns! Você adivinhou o número secreto em {} tentativas".format(tentativas))