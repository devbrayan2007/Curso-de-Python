nome_aluno = str(input("Informe o nome do aluno: "))
print("=" * 20)

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
print(f'A média do aluno {nome_aluno} foi de {media:.1f}')

