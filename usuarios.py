from sistema_cadastro import SistemaCadastral as sis 
class User(sis):

    def reconhecer_user(self, user: any):
        user.reconhecido_user(self)


class Cliente_Externo:

    def reconhecido_user(self):
        print('Cliente Externo: {} reconhecido')

class Funcionario:

    def reconhecido_user(self):
        print('Funcionario reconhecido')  

class Gerente(Funcionario):
    
    def __init__(self) :
        super().__init__()

    def reconhecido_user(self):
        print('Funcionario(Gerente) reconhecido') 


