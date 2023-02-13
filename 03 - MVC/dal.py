from model import Pessoa
FILE = '03 - MVC/pessoas.txt '

class PessoaDal:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open(FILE, 'a') as arq:
            arq.write('\n' + pessoa.nome + " " + str(pessoa.idade) + " " + pessoa.cpf)
            
    @classmethod
    def ler(self):
        nome = 'caio'
        idade = 20
        cpf = 10234332
        return Pessoa(nome, idade, cpf)

