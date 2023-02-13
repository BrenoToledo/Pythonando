from controller import PessoaController
while True:
    decisao = int(input ('\n Digite 1 para salvar uma pessoa \n Digite 2 para ver a pessoa salva \n Digite 3 para SAIR : '))
    if decisao == 3:
        break
    if decisao == 1:
        nome = input(' \n Digite seu nome : ')
        idade = int(input(' \n Digite sua idade : '))
        cpf = input(' \n Digite seu cpf : ')
        if PessoaController.cadastrar(nome,idade,cpf):
            print(' \n Usuário cadastrado com sucesso : ')
        else:
            print(' \n Digite valores válidos!')