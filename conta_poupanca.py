from tela_caixa_eletronico import Tela_Caixa_Eletronico

class Conta_poupanca(Tela_Caixa_Eletronico):
  
    def depositar(self, valor) -> None:
        print('Depositando {} na conta poupanca'.format(valor))

    
    def sacar(self, valor) -> None:
         print('Sacando {} na conta poupanca'.format(valor))