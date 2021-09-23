preco = float(input(""))
desconto = float(input(""))
desconto_i= desconto / 100
aumento = preco * desconto_i
aumento_b = preco + aumento
desconto_a = preco - aumento
aumento_a = format(aumento_b,'.2f')
desconto_b = format(desconto_a,'.2f')
print(aumento_a)
print(desconto_b)                 
