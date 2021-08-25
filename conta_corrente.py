from tela_caixa_eletronico import Tela_Caixa_Eletronico

class Conta_corrente(Tela_Caixa_Eletronico):
  
    def depositar(self, valor) -> None:
        print('Depositando {} na conta corrente'.format(valor))

    
    def sacar(self, valor) -> None:
         print('Sacando {} na conta corrente'.format(valor))