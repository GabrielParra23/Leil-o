from replit import clear
from logo import logo

print(logo)

dicionario_leilao = {}
fim = "sim"
while fim == "sim":
    pessoa = input("Digite seu nome: ")
    valor = int(input("Qual o valor que deseja adicionar R$ "))
    
    dicionario_leilao[pessoa] = valor
    
    fim = input("Mais alguem deseja disputar? \"Sim\" ou \"Não\"").lower()
    clear()


def vencedor():
    maior_valor = 0
    for key in dicionario_leilao:
        if dicionario_leilao[key] > maior_valor:
            maior_valor = dicionario_leilao[key]
            ganhador = key
    print(f"O Ganhador do leilão é {ganhador} com um valor de {dicionario_leilao[ganhador]}")
         

vencedor()      