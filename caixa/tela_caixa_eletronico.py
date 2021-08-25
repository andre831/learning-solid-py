from abc import ABC, abstractclassmethod

class Tela_caixa_eletronico(ABC):

    @abstractclassmethod
    def depositar(self, valor) -> None:
        pass

    @abstractclassmethod
    def sacar(self, valor) -> None:
        pass