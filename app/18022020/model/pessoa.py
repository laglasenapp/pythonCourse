class Pessoa:

    def __init__(self, nome, sobrenome, idade, sexo, id=None):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__idade = idade
        self.__sexo = sexo
        self.__id = id
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_sobrenome(self, sobrenome):
        self.__sobrenome = sobrenome

    def set_idade(self, idade):
        self.__idade = idade
    
    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome
    
    def get_sobrenome(self):
        return self.__sobrenome

    def get_idade(self):
        return self.__idade
    
    def get_sexo(self):
        return self.__sexo
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"{self.__id self.__nome} {self.__sobrenome} {self.__idade} {self.__sexo}"