
EXERCICIO_EXECUTAR = 12
_PULA_LINHA = '\n'
#----------------------------------------------------------------
# AULA 01 - VARIAVEIS E TIPOS DE VARIAVEIS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 1:
    pass
#----------------------------------------------------------------
# AULA 02 - ENTRADAS E SAÍDAS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 2:
    pass

#----------------------------------------------------------------
# AULA 03 - CONVERSAO DE DADOS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 3:
    pass

#----------------------------------------------------------------
# AULA 04 - OPERADORES ARITIMÉTICOS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 4:
    pass

#----------------------------------------------------------------
# AULA 05 - EXERCÍCIO 01 DE MÉDIA
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 5:
    # Escreva um programa onde o úsuário digite duas notas e ele mostre a média das duas notas

    #TODO: Resolver Exercicio 

    #>>> nota1 = 5
    #>>> nota2 = 7
    #media = 6

    nota1 = float(input('Digite a nota 1: '))
    nota2 = float(input('Digite a nota 2: '))

    media = ((nota1 + nota2)/2)

    print(media)
#----------------------------------------------------------------
# AULA 06 - OPERADORES RELACIONAIS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 6:

    OPERADORES_RELACIONAIS = """

    > MAIOR
    < MENOR
    == COMPARAÇÃO DE IGUAL
    != DIFERENTE
    <= MENOR OU IGUAL Á
    >= MAIO OU IGUAL Á


    """

    A = 2               # tipo int
    B = 2.0             # tipo float

    print (A == B)      # vai reconhecer ? 

#----------------------------------------------------------------
# AULA 07 - OPERADORES LÓGICOS
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 7:
    
    OPERADORES_LOGICOS = """

    AND = RETORNA TRUE SE TODAS AS CONDIÇÕES FOREM TRUE
    OR = RETORNA TRUE SE ALGUMA CONDIÇÃO FOR TRUE
    NOT = INVERTE O SINAL DE TRUE PARA NOT E VICE VERSA

    """
    print (OPERADORES_LOGICOS)
#----------------------------------------------------------------
# AULA 08 - ESTRUTURA DE DECISÃO
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 8:
    
    ESTRUTURA_DE_DECISAO = """

    IF -> LÓGICA

    ELIF --> LÓGICA

    ELSE -> NÃO ACEITA LÓGICA

    SEQUENCIA 

    -> VERIFICAR A LOGICA DE IF SE A LOGICA FOR FALSE TENTA A PROXIMA (ELIF) SE A LOGICA FOR NAO TENTA A PROXIMA (ELIF), 
    SEMPRE QUE NÃO TIVERMOS ELIF ELA PULA E EXECUTA ELSE DESDE QUE VOCE A TENHA.

    """
#----------------------------------------------------------------
# AULA 09 - EXERCÍCIO 02 DE MÉDIA 
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 9:
    # Receba 4 notas de um aluno e exiba se ele foi aprovado (nota maior qou igual que 6)
    # se ele ficou de recuperação (nota maior ou igual a 4) ou se ele foi 
    # reprovado (nota menor do que 4)

    # ENTRADA DE NOTAS
    nota1 = float(input('Digite a nota 01: '))
    nota2 = float(input('Digite a nota 02: '))
    nota3 = float(input('Digite a nota 03: '))
    nota4 = float(input('Digite a nota 04: '))
    
    # PROCESSAMENTO
    media = (nota1 + nota2 + nota3 + nota4) / 4
    
    if media >= 6:
        situacao = ", PARABÉNS você está aprovado..."
    
    elif media >= 4:
        situacao = ", você está em recuperação ..."
        
    else:
        situacao = " , você está em reprovado ..."
        
    # SAÍDA
    print (f' A sua média é {media}{situacao}!')
    
#----------------------------------------------------------------
# AULA 10 - EXERCÍCIO MAIOR NÚMERO
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 10:
    # Receba 3 numeros inteiros e exiba o maior deles
    
    # ENTRADA
    num1 = int(input('Digite o numero 01: '))
    num2 = int(input('Digite o numero 02: '))
    num3 = int(input('Digite o numero 03: '))
    
    # PROCESSAMENTO
    maiorNumero = max(num1, num2, num3)
    
    # SAÍDA
    print(f'O maior numero digitado foi o numero {maiorNumero}! ')
    
#----------------------------------------------------------------
# AULA 11 - EXERCÍCIO DE POSITIVO E NEGATIVO
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 11:
    
    # ENTRADA
    num1 = int(input('Digite o numero inteiro: '))
    
    # PROCESSAMENTO
    if num1 >= 0 :
        sinal = 'Positivo'
    else:
        sinal = 'Negativo'
        
    # SAÍDA
    print(f'O número  digitado foi {num1}, e ele é {sinal}! ')
    
#----------------------------------------------------------------
# AULA 12 - EXERCÍCIO M MASCULINO, F FEMININO 
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 12:
    # Receba M para masculino e F para feminino e retorne na tela
    
    # ENTRADA
    sexo = input('Digite o Sexo [F,M] !: ')

    # PROCESSAMENTO
    if sexo == 'f' or sexo == 'F':
        sexo = 'Feminino'
    
    elif sexo == 'm' or sexo == 'M':
        sexo = 'Masculino'
        
    else:
        
        sexo = 'indefinido'
        
        
    # SAÍDA
    print (f'O sexo digitado é {sexo}')
    
#----------------------------------------------------------------
# AULA 41 - LIST COMPREHENSION
#----------------------------------------------------------------
if EXERCICIO_EXECUTAR == 41:
    
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    # EXEMPLO 01
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA COMPREHENSION X NORMAL" + _PULA_LINHA)
    # Programação funcional
    X = [i for i in range(0,10)]
    
    # Programação normal
    y = []
    for i in range(0,10):
        y.append(i)
    
    print (X)
    print (y)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    # EXEMPLO 02
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA COMPREHENSION" + _PULA_LINHA)
    X = [10 for i in range(0,10)]
    print (X)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    # EXEMPLO 03
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA COM INPUT" + _PULA_LINHA)
    X = [input('Digite um nome: ') for i in range(0,3)]
    print (X)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    #EXEMPLO DE LISTA BI-DIMENSIONAL
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA BI-DIMENSIONAL" + _PULA_LINHA)
    X = [[input('Digite um numero: ') for j in range(0,2)] for i in range(0,2)]
    print (X)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    # EXEMPLO DE LISTA TRI-DIMENSIONAL
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA TRI-DIMENSIONAL" + _PULA_LINHA)
    X = [[[input('Digite um numero: ') for k in range(0,2)] for j in range(0,2)] for i in range(0,2)]
    print (X)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    
    # EXEMPLO DE LISTA COM CONDICIONAL IF 
    #----------------------------------------------------------------
    print("EXEMPLO DE LISTA COM CONDICIONAL IF" + _PULA_LINHA)
    X = [i for i in range(0,10) if i > 4]
    print (X)
    print('----------------------------------------------------------------' + _PULA_LINHA + _PULA_LINHA)
    


    
#=============================FIM================================
