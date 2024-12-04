import os
palavra = "azul"
palavrasPermitidas = 'abcdefghijklmnopqrstuvwxyz'

# Variável para armazenar as letras acertadas
letras_acertadas = ['*'] * len(palavra)
numero_tentativas = 0

while True:
    tentativas = input("Digite uma letra: ").lower()
    numero_tentativas += 1

    
    if tentativas == '':
        print("Você digitou campos vazios.")
        continue
    if len(tentativas) > 1:
        print("DIGITE APENAS UMA LETRA")
        continue
    if tentativas not in palavrasPermitidas:
        print("DIGITE APENAS LETRAS VÁLIDAS!")
        continue
    # Verificando se a letra está na palavra
    if tentativas in palavra:
        for i in range(len(palavra)):
            if palavra[i] == tentativas:
                letras_acertadas[i] = tentativas

    # Exibe a palavra com as letras descobertas
    print("Palavra:", ''.join(letras_acertadas))

    # Se todas as letras forem descobertas, o jogo acabou
    if '*' not in letras_acertadas:
        os.system('clear')
        print("Parabéns, você descobriu a palavra!")
        print(f'Você tentou {numero_tentativas}x para descobrir')
        letras_acertadas = ''
        numero_tentativas = 0
