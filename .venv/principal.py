menu = f"""

    #### BEM VINDO AO SISTEMA DO BANCO ###
    
    [d] - Depositar
    [s] - Sacar
    [e] - Extrato
    [q] - Sair

"""

saldo, limite, valor_saque_dia, contador_saque = 0.0, 500.0, 0.0, 0
LIMITES_SAQUE_DIARIO = 3
depositos_dia = []
saques_dia = []
dic_usuarios, dic_contas = {}, {}

def criar_usuario(nome, data_nascimento, cpf, logradouro, bairro, cidade, estado_sigla, dic_usuarios):
#Criar um dicionario para nome, com as chaves, nome, data_nascimento, cpf, endereco
    usuario = {"nome":nome, "data_nascimento":data_nascimento}
#Endereço é composto por logradouro, bairro, cidade / SIGLA estado
    endereco = {"logradouro":logradouro, "bairro":bairro, "cidade":cidade, "estado_sigla":estado_sigla}
#A chave do usuário deve ser o CPF
    usuario.update(endereco)
    lista_usuarios = dic_usuarios
    lista_usuarios[cpf] = usuario
#    print(lista_usuarios)

    return lista_usuarios


def conta_corrente(agencia, numero_da_conta, usuario):
    conta = input("Digite o número da conta:\n")
    agencia = "0001" + conta
    cpf_conta = input("Digite o CPF do titular da conta:\n")

    conta_usuario = {"conta":conta, "agencia":agencia, "cpf":cpf}
    return conta_usuario

def sacar(*, valor, saldo, contador, conjunto_saque):

    if (contador_saque < LIMITES_SAQUE_DIARIO):

        if (valor <= 500):
            contador += 1
            conjunto_saque.append(valor_saque)
            saldo -= valor

            print(f"""Saque realizado com sucesso, saldo atualizado.
saldo: {saldo}""")
        else:
            print(f"""Valor indisponível.
saldo: {saldo}""")

    else:
        print("Seu limite de saques já foi atingido por hoje.")

    return saldo, contador, conjunto_saque

def depositar(valor, saldo, extrato):

    saldo+= valor
    extrato.append(valor)
    return saldo, extrato

def extrato(saldo, /, *, depositos, saques):


    if len(depositos) > 0:
        print(f"Depositos do dia")
        for dep in depositos:
            print(f"R$ {dep}")

    if len(saques) > 0:
        print(f"Saques do dia")
        for saq in saques:
            print(f"R$ {saq}")

    print(f"Saldo: {saldo}")

############################ INICIO PROGRAMA ##########################

#nome, data_nascimento, cpf, logradouro, bairro, cidade, estado_sigla
nome = input("Digite seu nome:\n")
data_nascimento = input("Digite sua data de nascimento:\n")
cpf = nome
while not cpf.isdigit():
    cpf = input("Digite seu CPF, sem traço (-) ou ponto (.):\n")
    if not cpf.isdigit():
        print("Você digitou fora do formato desejado, por favor digite novamente.")

logradouro = input("Digite a rua onde mora:\n")
bairro = input("Digite o bairro do endereço:\n")
cidade = input("Digirte a cidade:\n")
estado_sigla = input("Digite a sigla do estado")

dic_usuarios = criar_usuario(nome, data_nascimento, cpf, logradouro, bairro, cidade, estado_sigla)


while True:

    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor que deseja depositar:\n"))
        resultado = depositar(valor_deposito, saldo, depositos_dia)
        saldo, depositos_dia = resultado

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar:\n"))
        resultado = sacar(valor=valor_saque, saldo=saldo, contador=contador_saque, conjunto_saque=saques_dia)
        saldo, contador_saque, saques_dia = resultado

    elif opcao == "e":
        extrato(saldo, depositos=depositos_dia, saques=saques_dia)

    elif opcao == "q":
        break

    else:
        print("Opção inválida")

