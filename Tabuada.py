numero = int(input('Qual o múmero da tabuada?'))
print('Imprimindo uma contagem da tabuada de', numero)
for contador in range(1, 11, 1):
    print(contador, 'x', numero, '=', contador * numero)