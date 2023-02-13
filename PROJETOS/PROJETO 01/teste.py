import os
import json

class JasonDB():

    def __init__(self, nome_database: str , atributos: list):
        
        self.nome_database = nome_database
        self.atributos = atributos
        self.arquivo = f'DATABASE\ {self.nome_database.title()}.json'
        self.diretorio = f'DATABASE'
        
        # Verifica se existe a pasta DATABASE e se não existir vamos criar para criar 
        
        if not self._verifica_existe_arquivo():         # Verifica se não existe o arquivo .JSON
            if self._verifica_existe_diretorio():       # Se não existir, verifica se existe a pasta DATABASE
                self._criar_arquivo()                   # Se Existir cria apenas o arquivo
            else:
                self._criar_diretorios()                # Se não existir, cria a pata DATABASE
                self._criar_arquivo()                   # Cria o arquivo .JSON

    def gravar(self, objeto: dict):
        try:
            with open(self.arquivo, 'a') as arq:
                json.dump(objeto, arq)
                return True
        except:
            return False
    
    def ler(self):
        try:
            with open(self.arquivo, 'r') as arq:
                return json.load(arq)
        except:
            return []
    
    def apagar(self):
        try:
            os.remove(self.arquivo)
            return True
        except:
            return False 
    
    # UTILITARIOS
    
    def _get_dict(self, objeto: dict):
        
        for indexador in objeto.__dict__:
            print (f'{indexador.keys} : {indexador.values}')
        
        
    def _verifica_existe_arquivo(self, arquivo = ""  ) -> bool:
        
        if arquivo == "" :
            arquivo = self.arquivo
            
        return os.path.exists(arquivo)
    
    def _criar_arquivo(self, arquivo = "" ) -> bool:

        if arquivo == "" :
            arquivo = self.arquivo
            
        try:
            f = open(arquivo, 'w')
            f.close()
            return True
        
        except:
            
            return False
        
    def _verifica_existe_diretorio(self, diretorio = "") -> bool:
        
        if diretorio == "" :
            diretorio = self.diretorio
            
        return os.path.exists(diretorio)
    
    def _criar_diretorios(self, diretorio = "") -> bool:
        
        if diretorio == "" :
            diretorio = self.diretorio
            
        try:
            os.mkdir(diretorio)
            return True
        except:
            return False
        
BD = JasonDB( 'breno Toledo',['Orcamento','Teste'])

base = dict()
base = {'nome': 'Breno', 'idade': '20'}
BD.gravar(base)
print(BD.ler())