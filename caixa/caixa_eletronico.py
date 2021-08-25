from typing import Type
from tela_caixa_eletronico import Tela_caixa_eletronico
from conta_poupanca import Conta_poupanca
from conta_corrente import Conta_corrente


class Caixa_eletronico:

    def __init__(self, tela: Type[Tela_caixa_eletronico]) -> None:
        self.__tela = tela

    def depositar_valor(self, valor: any) -> None:
        self.__tela.depositar(valor)
    
    def sacar_valor(self, valor: any) -> None:
        self.__tela.sacar(valor)


usuario = Caixa_eletronico(Conta_corrente())
usuario.depositar_valor(200)