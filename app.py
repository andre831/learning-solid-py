from time import sleep
from sistema_cadastro import SistemaCadastral
from usuarios import  Cliente_Externo, Funcionario, Gerente
from caixa_eletronico import Caixa_eletronico
from conta_poupanca import Conta_poupanca
from conta_corrente import Conta_corrente

print('Bem-Vindo ao Banco PDM')

option = 0
option_conta = 0
option_conta_poupanca = 0
option_conta_corrente= 0

while option <= 1:
   
    option = int(input('''Antes de tudo. identifique-se:  
    
    [1]Cliente
    [2]Funcionário 
    
    Resposta:'''))

    if option == 1:
        print('Okay, por favor passe para o sistema de cadastro')
        sleep(1)

        sis = SistemaCadastral()
        sis.cadastrar(
            nome = input('Infome seu nome:'),
            cpf  = input('Infome seu cpf:')
        )

        Cliente_Externo.reconhecido_user('')
        print(' ' * 20)
        print('Okay, agora você pode utilizar o caixa eletrônico')
        option_conta = int(input(''' [1] Conta Poupança --- [2] Conta Corrente 
        Resposta: '''))

        if option_conta == 1 :

            print(' ' * 20)
            print('Olá, esta é a sua conta poupança')

            option_conta_poupanca = int(input('''Qual operação você deseja realizar:
            [1] Deposito
            [2] Saque
            Resposta: '''))

            if option_conta_poupanca == 1:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_poupanca())
                acao.depositar_valor(valor = input('Digite o valor: '))
            
            elif option_conta_poupanca == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_poupanca())
                acao.sacar_valor(valor = input('Digite o valor: '))
                
        elif option_conta == 2 :

            print(' ' * 20)
            print('Olá, esta é a sua conta corrente')
            
            option_conta_poupanca = int(input('''Qual operação você deseja realizar:
            [1] Deposito
            [2] Saque
            Resposta: '''))

            if option_conta_poupanca == 1:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.depositar_valor(valor = input('Digite o valor: '))
            
            elif option_conta_poupanca == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.sacar_valor(valor = input('Digite o valor: '))
