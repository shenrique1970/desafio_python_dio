# menu de opções
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# iniciando variáveis
saldo = 0    # Saldo inicial
limite = 500    # Limite do saques
extrato = ""    # Extrato
numero_saques = 0    # Contador de saques
LIMITE_SAQUES = 3    # Limite máximo de saques

def formatar_valor(valor):
    # valor em reais
    return f"R$ {valor:.2f}"

def validar_valor(valor_input):
    # somente numeros positivos
    valor_input = valor_input.replace('.', '').replace(',', '.')
    if valor_input.isdigit() or (valor_input.replace('.', '', 1).isdigit() and valor_input.count('.') < 2):
        return float(valor_input)
    return None

def deposito(saldo, extrato):
    # deposito e regra
    valor_input = input("Informe o valor do depósito: ")
    valor = validar_valor(valor_input)

    if valor is not None and valor > 0:
        saldo += valor
        extrato += f"Depósito: {formatar_valor(valor)}\n"
        print(f"Depósito realizado com sucesso! Novo saldo: {formatar_valor(saldo)}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(saldo, extrato, numero_saques):
    # saque e regra
    valor_input = input("Informe o valor do saque: ")
    valor = validar_valor(valor_input)

    # se não é None
    if valor is not None:
        # se excede o saldo
        excedeu_saldo = valor > saldo
        # se excede o limite
        excedeu_limite = valor > limite
        # se chega ao máximo de saques
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        # erro se o saldo for insuficiente
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        # erro de limite
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        # erro se atingido limite de saque
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        # maior que zero
        elif valor > 0:
            # Atualiza o saldo
            saldo -= valor  
            # Adiciona o saque ao extrato
            extrato += f"Saque: {formatar_valor(valor)}\n" 
            # Incrementa o contador de saques 
            numero_saques += 1  
            # sucesso
            print(f"Saque realizado com sucesso! Saldo restante: {formatar_valor(saldo)}")
        else:
            # erro se o valor informado for inválido
            print("Operação falhou! O valor informado é inválido.")
    else:
        # erro se o valor informado não for um número válido
        print("Operação falhou! O valor informado não é um número válido.")

    # Retorna o saldo, extrato e número de saques atualizados
    return saldo, extrato, numero_saques

# logica do menu
while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = deposito(saldo, extrato)

    elif opcao == "s":
        saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques)

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: {formatar_valor(saldo)}")
        print("==========================================")

    elif opcao == "q":
        print("Saindo...")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")