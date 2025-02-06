questions = [
    {
        'Pergunta': "Quanto é 2 + 2?",
        'Opções': [10, 4, 6, 2],
        'Resposta': 4,
    },

    {
        'Pergunta': "Quanto é 3 x 3?",
        'Opções': [9, 5, 0, 3],
        'Resposta': 9,
    },

    {
        'Pergunta': "Quanto é 10 / 2?",
        'Opções': [5, 2.4, 1, 7],
        'Resposta': 2,
    }
]

cont = 0
contLoss = 0


while True:
    # PERGUNTA 1
    print(questions[0]['Pergunta'])
    for option in questions[0]['Opções']:
        print(option) 
    optionUser = float(input("Qual é a opção correta? "))
    if optionUser == questions[0]['Resposta']:
        print("Parabéns! Você acertou!!!")
        cont += 1
    else:
        print(f"RESPOSTA ERRADA! A resposta correta é {questions[0]['Resposta']}")
        contLoss += 1
        continue
    
    print()

    # PERGUNTA 2
    print(questions[1]['Pergunta'])
    for option in questions[1]['Opções']:
        print(option)
    optionUser = float(input("Qual é a opção correta?"))
    if optionUser == questions[1]['Resposta']:
        print("Parabéns! Você acertou!!!")
        cont += 1
    else:
        print(f"RESPOSTA ERRADA! A resposta correta é {questions[1]['Resposta']}")
        contLoss += 1
        continue

    print()
    
    # PERGUNTA 3
    print(questions[2]['Pergunta'])
    for option in questions[2]['Opções']:
        print(option)
    optionUser = float(input("Qual é a opção correta?"))
    if optionUser == questions[1]['Resposta']:
        print("Parabéns! Você acertou!!!")
        cont += 1
    else:
        print(f"RESPOSTA ERRADA! A resposta correta é {questions[2]['Resposta']}")
        contLoss += 1
        break


print("ESTATÍSTICAS")
print("=== === === === === === ===")
print(f"Você acertou {cont} de {len(questions)} perguntas.")
print(f'Você errou {contLoss} vez(es).')
print("=== === === === === === ===")
