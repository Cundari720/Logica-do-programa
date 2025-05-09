#constantes com as cotações de hoje
EURO = 6.3492
DOLLAR = 5.81
YUAN = 0.8039
print('' 30)
real = float(input('digite o valor em real R$ para converter:'))
print('' 30)
em_euro = real / EURO
em_dolar = real / DOLLAR
em_yuan = real / YUAN
print(f'R$ {real} são {em_euro:.2f} euros')
print(f'R$ {real} são {em_dolar:.2f} dolares')
print(f'R$ {real} são {em_yuan:.2f} yuans')