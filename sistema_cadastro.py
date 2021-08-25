from time import sleep

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
             self.__armazernar_usuario(nome, idade)
        else:
            self.__indicar_erro()


    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
           return True
        else:
            return False
    
    def __armazernar_usuario(self, nome: str, idade: int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o Usuario {}, Idade {}'.format(nome, idade))
        sleep(2)
        print('Cadastro concluido')
    
    def __indicar_erro(self) -> None:
        print('dados invalidos!')