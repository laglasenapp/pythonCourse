class CalculadoraCientifica:

    __n1 = 0

    __n2 = 0

    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2

    def soma(self):
        return self.__n1 + self.__n2

    def subtracao(self):
        return self.__n1 - self.__n2

    def divisao(self):
        return self.__n1 / self.__n2

    def multiplicao(self):
        return self.__n1 * self.__n2
    
   