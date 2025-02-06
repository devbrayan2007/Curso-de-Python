frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
        'Python foi criado por Guido van Rossum'

i = 0
qtd_letras_aparecida = 0
letra_apareceu_mais = ''
while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_letras_aparecida_atual = frase.count(letra_atual)
    
    if qtd_letras_aparecida < qtd_letras_aparecida_atual:
        qtd_letras_aparecida = qtd_letras_aparecida_atual
        letra_apareceu_mais = letra_atual
        
    i += 1
    
print(f'A letra que apareceu mais vezes foi o "{letra_apareceu_mais}" que apareceu {qtd_letras_aparecida}x')
