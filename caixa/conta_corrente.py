from tela_caixa_eletronico import Tela_caixa_eletronico

class Conta_corrente(Tela_caixa_eletronico):
  
    def depositar(self, valor) -> None:
        print('Depositando {} na conta corrente'.format(valor))

    
    def sacar(self, valor) -> None:
         print('Sacando {} na conta corrente'.format(valor))