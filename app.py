from time import sleep
from sistema_cadastro import SistemaCadastral
from usuarios import  Cliente_Externo, Funcionario, Gerente
from caixa_eletronico import Caixa_eletronico
from conta_poupanca import Conta_poupanca
from conta_corrente import Conta_corrente

print('Bem-Vindo ao Banco PDM')

option = 0
option_caixa_eletronico = 0
option_conta_poupanca = 0

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
        option_caixa_eletronico = int(input(''' [1] Conta Poupança --- [2] Conta Corrente 
        Resposta: '''))

        if option_caixa_eletronico == 1:
            print(' ' * 20)
            print('Olá, esta é a sua conta poupança')
            option_conta_poupanca = int(input('''Qual operação você deseja realizar:
        [1] Deposito
        [2] Saque
        Resposta: '''))

