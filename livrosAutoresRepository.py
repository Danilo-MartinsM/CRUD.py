import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class LivrosAutoresRepository:
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
    
    def listarLivrosAutores(self):
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute("""
                SELECT l.id, l.nome, l.genero, GROUP_CONCAT(a.nome SEPARATOR ', ') autores
                        FROM livros l
                        join livros_tem_autores lta on l.id = lta.id_livro
                        join autores a on lta.id_autor = a.id
                        GROUP BY l.id, l.nome, l.genero
            """)

            registros = cursor.fetchall()
            cursor.close()
            conexao.close()

            return registros
    
    def inserirLivroAutor(self, id_livro, id_autores):
        conexao = self.conectar()
        cursor = conexao.cursor()

        for id_autor in id_autores:
            cursor.execute("INSERT INTO livros_tem_autores (id_livro, id_autor) VALUES (%s, %s)", (id_livro, id_autor))
        conexao.commit()
        
        cursor.close()
        conexao.close()

    def apagarLivrosAutores(self, id_livro):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros_tem_autores WHERE id_livro = %s", (id_livro,))
        conexao.commit()

        cursor.close()
        conexao.close()