# CLOSURE E FUNÇÕES QUE RETORNAM OUTRAS FUNÇÕES


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


bom_dia = criar_saudacao("Bom dia")
boa_noite = criar_saudacao("Boa noite")

for nome in ["Brayan", "Pedro", "João"]:
    print(bom_dia(nome))
    print(boa_noite(nome))
