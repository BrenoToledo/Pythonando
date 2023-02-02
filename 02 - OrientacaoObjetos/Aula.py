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
            
#----------------------------------------------------------------
# AULA 07 - CLS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 7:
    "Como Funciona o CLS e como ele ajuda os métodos estáticos"
    
    #EXEMPLO
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
            
        # IMPORTANTE : Podemos criar atributos de classe dentro dos métodos de classe
        # podemos pegar por exemplo o método de classe ANDAR e criar um atributo PERNAS. 
        """
        @classmethod
        def andar(cls):
            cls.pernas = 2 
            print('Estou Andando')
            
        """

        # Com isso, esse novo atributo será criado assim que usarmos esse método de classe
        
        """
        Pessoa.andar() # acessa o método de classe e graças ao CLS podemos criar o Atributo de classe
        print(Pessoa.pernas) # Acessando o atributo de classe
        >>> 2
        """

        # Podemos fazer o método de classe mudar um valor de atributo de classe já definido
        # Imagine que você quer mudar a raça depois de chamar a classe teste, então temos ...
        # o atributo de classe chamado raca na classe Pessoa, e vamos criar um método de classe chamado exame_sangue
        
        """
        @classmethod
        def exame_sangue(cls): # cls passa o estado da classe com todas informações
            cls.raca = 'A+' 
        """
        
        # Quando criarmos uma nova Pessoa, será atribuido automáticamente a raca 'Ser Humano'
        # mas depois que rodarmos o método exame_sangue, teremos a raca alterada para o resultado 
        # do exame de sangue por exemplo.
        
        """
        Pessoa.exame_sangue() 
        print(Pessoa.raca)
        >>> A+
        """
        
#----------------------------------------------------------------
# AULA 08 - class methods X static methods
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 8:
    """
    
    CLASS METHODS =================================================================
    
    É capaz de acessar e editar a classe que ele pertence, isso inclui ele fazer 
    edição em atributos de classe por exemplo ou chamar outro metodo de dentro dele
    
        EXEMPLO =================================================================
        
        class Carro(): 
        
            # ATRIBUTOS DE CLASSE
            
            PILOTO_AUTOMATICO = True
            CAMBIO_AUTOMATICO = True
            
            def acelerar(self):
                pass
            
            def frear(self):
                pass
            
            def velocimetro ()
            @classmethod
            def piloto_automatico(cls):
                if PILOTO_AUTOMATICO:        # Eu posso acessar Variaveis globais e editar se for @classmethod
                    cls.acelerar()           # Eu posso chamar outros métodos se for um @classmethod
                else: 
                    print('O carro não é automático !')

        
        FIM =================================================================
        
    
    STATIC METHODS =================================================================
    
    É incapaz de acessar e editar a classe que ele pertence, isso inclui ele fazer 
    edição em atributos de classe por exemplo ou chamar outro metodo de dentro dele, 
    ele é isolado e funciona para códigos utilitários
    

        
        EXEMPLO =================================================================
        
        class Carro(): 
        
            # ATRIBUTOS DE CLASSE
            PILOTO_AUTOMATICO = True
            CAMBIO_AUTOMATICO = True
            E_KM_HORA = True
            
            def acelerar(self):
                pass
            
            def frear(self):
                pass
            
            def velocidade(self):
                if E_KM_HORA:
                    calculo_km()
                else:
                    calculo_milhas(velocidade)
            @classmethod
            def piloto_automatico(cls):
                if PILOTO_AUTOMATICO:        # Eu posso acessar Variaveis globais e editar se for @classmethod
                    cls.acelerar(velocidade)           # Eu posso chamar outros métodos se for um @classmethod
                else: 
                    print('O carro não é automático !')
            
            # STATIC METHODS 
            
            @staticmethod
            def calculo_km(velocidade): # Não consegue interagir com a classe que pertence
                pass
            
            @staticmethod
            def calculo_milhas(velocidade): # Não consegue interagir com a classe que pertence
                pass
        FIM =================================================================
    
    """         
    
#----------------------------------------------------------------
# AULA 09 - Herança
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 9:
    
    """
    
    """
    
    class Vendedor:
        
        def falar