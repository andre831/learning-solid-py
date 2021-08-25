from typing import Type
from tela_caixa_eletronico import Tela_Caixa_Eletronico
from conta_poupanca import Conta_poupanca
from conta_corrente import Conta_corrente


class Caixa_eletronico:

    def __init__(self, tela: Type[Tela_Caixa_Eletronico]) -> None:
        self.__tela = tela

    def depositar_valor(self, valor: any) -> None:
        self.__tela.depositar(valor)
        print(''*20)
        print('O valor de {} foi depositado !'.format(valor))
    
    def sacar_valor(self, valor: any) -> None:
        self.__tela.sacar(valor)
        print(''*20)
        print('O valor de {} foi sacado !'.format(valor))
