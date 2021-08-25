from typing import Type

class Pessoa:

    def andar(self):
        print('{} está andando')
    
    def cumprimentar(self):
        print('{} cumprimentou')
    
    def pegar_cartao(self):
        print('{} pegou o cartão')

class Funcionario(Pessoa):
    def __init__(self):
        super().__init__()

    def bater_ponto(self):
        print('Funcionári@ {} bateu ponto')

class Gerente(Funcionario):
    def __init__(self):
        super().__init__()

    def fazer_solicitacao(self):
        print('O Gerente fez uma solicitação')


class Clientes(Pessoa):
    def __init__(self):
        super().__init__()
      
    def sacar(self):
        Caixa_eletronico.sacar_valor()

class Camera:

    def observar(self, pessoa: Type[Pessoa]):
        pessoa.andar()



