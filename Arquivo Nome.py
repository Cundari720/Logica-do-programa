nome = input('Digite um nome')
qnt = int(input('digite a quantidade de repetições'))
arq = input('digite o nome do arquivo para gerar?')

nome += '\n'
listas_nome = (nome * qnt)
print(listas_nome)
with open(arq, 'w') as arquivo:
    arquivo.write(listas_nome)