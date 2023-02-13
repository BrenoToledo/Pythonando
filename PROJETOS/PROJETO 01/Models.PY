from teste import JasonDB as db

# arquivos de tabelas


class Pessoa():
    
    def __init__(self,nome,sobrenome,data_nascimento,telefone,email,endereco):
        self.nome = nome
        self.sobrenome =sobrenome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
        
class Funcionario(Pessoa):
    
    def __init__(self,nome,sobrenome,data_nascimento,telefone,email,endereco,cargo,descricao_cargo):
        super().__init__(nome,sobrenome,data_nascimento,telefone,email,endereco)
        self.cargo = cargo
        self.descricao_cargo = descricao_cargo


class Cliente(Pessoa):
    
    def __init__(self, nome, sobrenome, data_nascimento, telefone, email, endereco):
        super().__init__(nome, sobrenome, data_nascimento, telefone, email, endereco)
        
class Forncedor(Pessoa):
    
    def __init__(self, nome, sobrenome, data_nascimento, telefone, email, endereco,cnpj_cpf,pessoa_fisica = True, nome_empresa = ""):
        super().__init__(nome, sobrenome, data_nascimento, telefone, email, endereco)
        self.cnpj_cpf = cnpj_cpf
        self.pessoa_fisica = pessoa_fisica
        self.nome_empresa = nome_empresa
        
class Categoria ():
    
    def __init__ (self,nome):
        self.nome = nome
        
class Produto ():
    
    def __init__ (self,nome_produto,peso,unidade_medida,fornecedor,categoria):
        self.nome_produto = nome_produto
        self.peso =peso
        self.unidade_medida = unidade_medida
        self.fornecedor = fornecedor
        self.categoria = categoria
        
        # CRIAR DATABASE E SALVAR
        
        
        
        self.nome_produto = nome_produto
        self.peso =peso
        self.unidade_medida = unidade_medida
        self.fornecedor = fornecedor
        self.categoria = categoria
f1 = Funcionario('Breno','toledo','07/03/1996','breh_toledo@hotmail.com','Rua Celso Machado de Araujos','Alameda Angatuba, 65', 'Electric', 'Tomar choques elétricos')
#print(f1)

c1 = Categoria("Carne")
p1 =  Produto("Patinho","150","kilo",f1,c1)

#print(dir(p1.categoria))
print(p1.__dict__)
print("---------------------------------")

db("teste", ["teste 01", "teste 02", "teste 03", "teste 04"])._get_dict(p1)

