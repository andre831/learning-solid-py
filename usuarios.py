from sistema_cadastro import SistemaCadastral as sis 
class User(sis):

    def reconhecer_user(self, user: any):
        user.reconhecido_user(self)


class Cliente_Externo:

    def reconhecido_user(self):
        print('Cliente Externo reconhecido')

class Funcionario:

    def reconhecido_user(self):
        print('Funcionario reconhecido')  

class Funcionario_Executivo(Funcionario):
    
    def __init__(self) :
        super().__init__()

    def reconhecido_user(self):
        print('Funcionario(Funcionario Executivo) reconhecido') 


