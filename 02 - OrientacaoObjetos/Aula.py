EXERCICIO_EXECUTAR = 4



#----------------------------------------------------------------
# AULA 01 - Introdução ao POO
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 1:
    PARADIGMAS="""
    PARADIGMAS DE PROGRAMAÇÃO
    
        PARADIGMA PROCEDURAL
        
        PARADIGMA FUNCIONAL
        
        PARADIGMA ORIENTADO A OBJETOS
        
        Trabalha com objetos, também conhecidos como entidades ( Molde )
        e essas entidades tem 
        
             - ATRIBUTOS: Caracteristicas 
             
             - METODOS : Ações
    """
    
#----------------------------------------------------------------
# AULA 02 - Modelagem
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 2:
    modelagem="""
    
    """
    
    class Pessoas:
        def __init__(self, nome, idade, cpf): #DEFININDO OS ATRIBUTOS
            self.nome = nome
            self.idade = idade
            self.cpf = cpf
        
        def logar_sistema(self):                  #DEFININDO O METODO
            print('Estou logando no sistema')
            
    p1 = Pessoas('Breno', 26, 999999999999)
    
    p1.logar_sistema()
    print ()
    
#----------------------------------------------------------------
# AULA 03 - MÉTODO CONSTRUTOR
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 3:
    
    """ __init__ É chamado sempre que criamos uma nova Instancia """

    class Pessoas:
        def __init__(self):         #DEFININDO OS ATRIBUTOS
            pass
        
        def logar_sistema(self):    #DEFININDO O METODO
            print('Estou logando no sistema')
            
#----------------------------------------------------------------
# AULA 04 - SELF
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 4:
    
    """ O SELF fala que aqueles parametros ou metodos diz respeito aquela entidade """

    class Pessoa:
        def __init__(self,name ):         #DEFININDO OS ATRIBUTOS
            self.name = name
        
        def retorna_nome(self):
            return self.name
        
        def logar_sistema(self):    #DEFININDO O METODO
            print(f' {self.retorna_nome()} está logando no sistema') # Se tirar o Self não funciona
    
    p1 = Pessoa("Breno")
    
    p1.logar_sistema()
    
    
#----------------------------------------------------------------
# AULA 05 - ATRIBUTOS DE CLASSE
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 5:
    """
    
    ATRIBUTOS DE CLASSE: Pode ser acessado mesmo sem ter definido uma intância, exemplo:
    
        print(Pessoa.possui_olho)
        >>> True
    
    se tentar fazer o mesmo com o atributo de instancia terá um erro
        
        print(Pessoa.nome)
        >>> ERROR
        
    para não ter erro teria que criar a instancia priemiro para o self saber onde buscar.
    
        print(Pessoa(Breno', 26).nome)
        >>> 'Breno'
        
        
    Se for necessário criar 2 instancias, cada uma pode ser independente um do outro.
    
        p1 = Pessoa('Breno', 26)
        p2 = Pessoa('Joao', 21)
        
    O padrão é True por que foi definido assim na classe, mas podemos mudar
        p1.possui_olho = False
    
    Exibindo veremos a diferenca :
    
        print('p1.possui_olho')
        >>> False
        print('p2.possui_olho')
        >>> True
        
    podemos mudar TODAS INSTANCIAS de uma vez se definirmos um valor para a classe
    
        Pessoa.possui_olho = False
        
        print('p1.possui_olho')
        >>> False
        print('p2.possui_olho')
        >>> False
        
    """
    
    
    class Pessoa:
        
        # ATRIBUTOS DE CLASSE
        possui_olho = True
        possui_boca = True
        raca = "Ser Humano"
        
        #ATRIBUTOS DE INSTANCIA
        def __init__(self,nome, idade ):
            self.nome = nome
            self.idade = idade
            
        def retorna_nome(self):
            return self.name
        
        def logar_sistema(self):    #DEFININDO O METODO
            print(f' {self.retorna_nome()} está logando no sistema') # Se tirar o Self não funciona
    
    p1 = Pessoa("Breno",26)
    p2 = Pessoa("Joao",21)
    
    p1.possui_olho = False
    
    print(p1.possui_olho)
    print(p2.possui_olho)
    
    Pessoa.possui_olho = True
    
#----------------------------------------------------------------
# AULA 06 - METODOS DE CLASSE
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 6:
    """
        METODOS DE CLASSE: É definido pelo decorator antes do metodo
        
        @classmethod
        def metodo(cls):
            pass
            
        com isso, o metodo pode ser acessado sem instanciar um objeto
        
        class Pessoa:
            ...
            def andar(cls, velocidade):
                print('Estou Andando a {velocidade} m/s!')
                
        Pessoa.andar(10)
        >>> Eu estou andando a 10 m/s!
        
        E pode ser acessado após instanciar um objeto também
        
        p1 = Pessoa("Breno", 26)
        
        p1.andar(10)
        >>> Eu estou andando a 10 m/s!
        
    """
    
    class Pessoa:
        
        # ATRIBUTOS DE CLASSE
        possui_olho = True
        possui_boca = True
        raca = "Ser Humano"
        
        #ATRIBUTOS DE INSTANCIA
        def __init__(self,nome, idade ):
            self.nome = nome
            self.idade = idade
            
        def retorna_nome(self):
            return self.name
        
        def logar_sistema(self):    #DEFININDO O METODO
            print(f' {self.retorna_nome()} está logando no sistema') # Se tirar o Self não funciona
            
        #é definido pelo Decorator @classmethod
        @classmethod
        def andar():
            print('Estou Andando')