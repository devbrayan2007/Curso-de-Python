largura = float(input("Largura da parede ( m ): "))
altura = float(input("Altura da parede ( m ): "))

area = largura * altura
quantidadeTinta = area * 2

print(f"Área total: {area:.2f}")
print(f'Quantidade de tinta que será usada: {quantidadeTinta}')
