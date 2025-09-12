import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class AutoresRepository:
    def __init__(self):
        self.host = os.getenv("host")
        self.usuario = os.getenv("usuario")
        self.senha = os.getenv("senha")
        self.banco = os.getenv("banco")

    def conectar(self):
        conexao = mysql.connector.connect(
            host=self.host,
            user=self.usuario,
            password=self.senha,
            database=self.banco
        )
        return conexao
    
    def listarAutores(self):
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute("SELECT id, nome FROM autores")

            registros = cursor.fetchall()
            cursor.close()
            conexao.close()

            return registros
    
    def inserirAutor(self, autores):
        conexao = self.conectar()
        cursor = conexao.cursor()
        
        registros = []
        for autor in autores:
            cursor.execute("INSERT INTO autores (nome) VALUES (%s);", (autor,))
            registros.append(cursor.lastrowid)
        conexao.commit()

        cursor.close()
        conexao.close()
        return registros
        
    def listarPorNome(self, autores):
        conexao = self.conectar()
        cursor = conexao.cursor()

        registros = []
        for autor in autores:
            cursor.execute("SELECT id FROM autores WHERE nome = %s", (autor,))
            registro = cursor.fetchone()
            if registro:
                registros.append(registro[0])

        cursor.close()
        conexao.close()
        if registros:
             return registros
        else:
             return None

