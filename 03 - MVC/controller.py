from dal import PessoaDal
from model import Pessoa


class PessoaController: 
    
    # VERIFICAÇÃO DO CPF
    @classmethod
    def cadastrar(cls, nome, idade: int, cpf):
        if (len(nome) < 2):
            print(' O nome é menor do que 2 Digitos!')
            return False
        if (idade < 0 ):
            print(' A idade é menor que 0')
            return False
        if (idade > 200):
            print(' A idade é maior que 200')
            return False
        if (len(cpf) != 11):
            print (' O cpf não contem 11 Digitos')
            return False
        else:
            try:
                print(' \n Abrindo Comunicação com BD')
                PessoaDal.salvar(Pessoa(nome,idade,cpf))
                return True
            except Exception as e: 
                print(e)
                return False


