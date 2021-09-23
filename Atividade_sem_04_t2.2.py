quadrado = float(input(""))
area = quadrado * quadrado
perimetro = quadrado + quadrado + quadrado + quadrado
area_a = format(area,'.4f')
perimetro_b = format(perimetro,'.4f')
area_b = "{:>10}"
perimetro_c = "{:>10}"
print(area_b.format(area_a))
print(perimetro_c.format(perimetro_b))

