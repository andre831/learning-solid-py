from time import sleep

class SistemaCadastral:

    def cadastro(self, nome: str, cpf: str) -> None:
        if self.__verificar_dados(nome, cpf):
             self.__armazernar_usuario(nome, cpf)
        else:
            self.__indicar_erro()


    def __verificar_dados(self, nome: str, cpf: str) -> bool:
        if isinstance(nome, str) and isinstance(cpf, str):
           return True
        else:
            return False
    
    def __armazernar_usuario(self, nome: str, cpf: str) -> None:
        print('acessando o banco de dados...')
        print(' ' * 20)
        print('NOME USUÁRIO:  {}, CPF:  {}'.format(nome, cpf))
        sleep(2)
        print(' ' * 20)
        print('Reconhecimento de cadastro concluído')
    
    def __indicar_erro(self) -> None:
        print('dados inválidos!')