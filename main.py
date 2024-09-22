import os
#sfsjfs
def menu(): 
    print("""
======= SISTEMA BANCÁRIO BÁSICO =======
| [1] - Depositar                     |
| [2] - Sacar                         |
| [3] - Extrato                       |
| [4] - Sair                          |
=======================================
""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#Função para depósito de Saldo
def depositar(valorDepositado): 
    global saldo
    global extrato
    if valorDepositado > 0:
        saldo+=valorDepositado 
        print(f"\nO valor de {valorDepositado} R$ foi adicionado com sucesso na conta")
        extrato += f"Depósito: R$ {valorDepositado:.2f}\n"
    else:
        print("\nApenas valores positivos devem ser insderidos no Depósito")

def sacar(valorSacar):
    global numero_saques
    global saldo
    global numero_saques
    global limite
    global extrato
    global LIMITE_SAQUES
    if numero_saques < LIMITE_SAQUES:
        if saldo >= valorSacar and valorSacar<=limite:
            saldo-= valorSacar
            numero_saques += 1
            print(f"\nO valor de {valorSacar} R$ foi sacado com sucesso na sua conta")
            extrato += f"Saque: R$ {valorSacar:.2f}\n"
        elif saldo< valorSacar:
            print("\nSaldo da conta é insuficiente")
        else:
            print("\nValor a ser sacado é superior ao limite máximo de 500 R$")
    else:
        print("\nVocê excedeu o limite diário de saques")

while True:
    menu()
    opcao = int(input("Digite a opção: "))

    os.system("cls")

    if opcao == 1:
        print("\n-------DEPÓSITO-------")
        valorDeposito=float(input("\nInforme o valor a ser depositado na conta: "))
        depositar(valorDeposito)
    elif opcao == 2:
        print("\n-------SAQUE--------")
        valorSacar=float(input("\nInforme o valor a ser sacado da conta: "))
        sacar(valorSacar)
    elif opcao == 3:
        print("\n-------EXTRATO------")
        print("\nO seu extrato")
        if not extrato:
            print("\nNão há movimentação na conta!")
        else:
            print(f"\n{extrato}")
            print(f"\nO saldo total da sua conta é: {saldo} R$")

    elif opcao == 4:
        break

    else:
        print("\nOpção digitada é inválida!, Por favor digite a operação adequada")
    

