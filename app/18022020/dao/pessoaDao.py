from flask_mysqldb import MySQLdb
from model.pessoa import Pessoa

class PessoaDao:

    def __init__(self):
        self.__conexao = MySQLdb.connect(host="mysql.topskills.study", database="topskills01", user="topskills01", password="ts2019")
        self.__cursor = self.__conexao.cursor()

    def listar_todos(self):
        lista = []
        self.__cursor.execute("select * from 01_PN_PESSOA")
        for x in self.__cursor.fetchall():
            #print(f"ID: {x[0]} NOME:{x[1]} SOBRENOME:{x[2]} IDADE:{x[3]} SEXO:{x[4]}")
            p = Pessoa(x[1],x[2],x[3],x[4], x[0])
            lista.append(p)
        return lista

    def buscar_por_id(self, id):
        self.__cursor.execute(F"select * from topskills01.01_PN_PESSOA WHERE ID={id}")
        x = self.__cursor.fetchone()
        #print(f"ID: {x[0]} NOME:{x[1]} SOBRENOME:{x[2]} IDADE:{x[3]} SEXO:{x[4]}")
        return Pessoa(x[1],x[2],x[3],x[4], x[0])
    
    def inserir(self, pessoa:Pessoa):
        self.__cursor.execute(F"""
        INSERT INTO topskills01.01_PN_PESSOA (NOME, SOBRENOME, IDADE, SEXO)
        VALUES ({pessoa.get_nome()},{pessoa.get_sobrenome()},{pessoa.get_idade()},{pessoa.get_sexo()});""")
        self.__conexao.commit()

    def alterar(self, pessoa:Pessoa):
        self.__cursor.execute(F"""
        UPDATE 01_PN_PESSOA 
        SET NOME = {pessoa.get_nome()}, SOBRENOME = {pessoa.get_sobrenome()}, IDADE = {pessoa.get_idade()}, sexo={pessoa.get_sexo()}
        WHERE ID = {pessoa.get_id()}
        """)
        self.__conexao.commit()

    def deletar(self, id):
        self.__cursor.execute(F"""
        DELETE FROM 01_PN_PESSOA WHERE ID = {id}
        """)
        self.__conexao.commit()        


pessoaDao = PessoaDao()

pessoaDao.listar_todos()

pessoaDao.buscar_por_id(4)

pessoaDao.inserir('Teste','Teste2',1,'?')