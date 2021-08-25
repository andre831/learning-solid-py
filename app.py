from time import sleep
from sistema_cadastro import SistemaCadastral
from usuarios import  Cliente_Externo, Funcionario, Funcionario_Executivo
from caixa_eletronico import Caixa_eletronico
from conta_poupanca import Conta_poupanca
from conta_corrente import Conta_corrente

print('Bem-Vindo ao Banco PDM')

option = 0
option_conta = 0
option_conta_poupanca = 0
option_conta_corrente= 0
recomecar = 0

while option <= 1:
   
    option = int(input('''Antes de tudo. identifique-se:  
    
    [1]Cliente
    [2]Funcionário
    [3]Funcionário Executivo 
    
    Resposta:'''))

    if option == 1:
        print('Okay, por favor aguarde para o sistema verificar o seu cadastro')
        sleep(1)

        sis = SistemaCadastral()
        sis.cadastro(
            nome = input('Infome seu nome:'),
            cpf  = input('Infome seu cpf:')
        )

        Cliente_Externo.reconhecido_user('')
        print(' ' * 20)
        print('Okay, agora você pode utilizar o caixa eletrônico')
        option_conta = int(input(''' [1] Conta Poupança --- [2] Conta Corrente 
        Resposta: '''))

        if option_conta == 1: #Conta Poupança

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

                recomecar = int(input('''Voce deseja executar mais alguma acao: 
                [1] Sim
                [2] Não, sair'''))

                                 

            elif option_conta_poupanca == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_poupanca())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break
                
        elif option_conta == 2: #Conta Corrente

            print(' ' * 20)
            print('Olá, esta é a sua conta corrente')
            
            option_conta_corrente = int(input('''Qual operação você deseja realizar:
            [1] Deposito
            [2] Saque
            Resposta: '''))

            if option_conta_corrente == 1:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.depositar_valor(valor = input('Digite o valor: '))
                break
            
            elif option_conta_corrente == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break


    if option == 2:
        sleep(1)

        sis = SistemaCadastral()
        print(' ' * 20)
        sis.cadastro(
            nome = input('Infome seu nome:'),
            cpf  = input('Infome seu cpf:')
        )
        Funcionario.reconhecido_user('')
        print(' ' * 20)
        print('Olá funcionário, seja bem-vindo.')

        print('Qual conta você deseja acessar?')
        print(' '*20)
        option_conta = int(input(''' [1] Conta Poupança --- [2] Conta Corrente 
        Resposta: '''))

        if option_conta == 1: #Conta Poupança

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
                break

            elif option_conta_poupanca == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_poupanca())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break
                
        elif option_conta == 2: #Conta Corrente

            print(' ' * 20)
            print('Olá, esta é a sua conta corrente')
            
            option_conta_corrente = int(input('''Qual operação você deseja realizar:
            [1] Deposito
            [2] Saque
            Resposta: '''))

            if option_conta_corrente == 1:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.depositar_valor(valor = input('Digite o valor: '))
                break
            
            elif option_conta_corrente == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break
        
    if option == 3:
        sleep(1)

        sis = SistemaCadastral()
        print(' ' * 20)
        sis.cadastro(
            nome = input('Infome seu nome:'),
            cpf  = input('Infome seu cpf:')
        )
        Funcionario.reconhecido_user('')
        print(' ' * 20)
        print('Olá funcionário executivo, seja bem-vindo ao Banco PDM.')

        print('Qual conta você deseja acessar?')
        print(' '*20)
        option_conta = int(input(''' [1] Conta Poupança --- [2] Conta Corrente 
        Resposta: '''))

        if option_conta == 1: #Conta Poupança

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
                break

            elif option_conta_poupanca == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_poupanca())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break
                
        elif option_conta == 3: #Conta Corrente

            print(' ' * 20)
            print('Olá, esta é a sua conta corrente')
            
            option_conta_corrente = int(input('''Qual operação você deseja realizar:
            [1] Deposito
            [2] Saque
            Resposta: '''))

            if option_conta_corrente == 1:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.depositar_valor(valor = input('Digite o valor: '))
                break
            
            elif option_conta_corrente == 2:
                print('Ok!')
                print(' ' * 20)
                acao = Caixa_eletronico(Conta_corrente())
                acao.sacar_valor(valor = input('Digite o valor: '))
                break