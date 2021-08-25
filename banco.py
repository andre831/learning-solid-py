from typing import Type
from caixa.caixa_eletronico import Caixa_eletronico
from caixa.conta_poupanca import Conta_poupanca
from caixa.conta_corrente import Conta_corrente

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
      
    def sacar(self, valor):
      caixa = Caixa_eletronico(Conta_poupanca())
      caixa.depositar_valor(200)

class Camera:

    def observar(self, pessoa: Type[Pessoa]):
        pessoa.andar()


andre = Clientes()
andre.sacar(200)
