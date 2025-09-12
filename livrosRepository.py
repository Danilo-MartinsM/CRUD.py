import os
import mysql.connector
from autoresRepository import AutoresRepository
from livrosAutoresRepository import LivrosAutoresRepository
from dotenv import load_dotenv

load_dotenv()

class LivrosRepository:
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
    
    def inserir(self, nome, genero, autores):
        repositorio = AutoresRepository()
        repositorio_livros_autores = LivrosAutoresRepository()

        conexao = self.conectar()
        cursor = conexao.cursor()

        id_autores = repositorio.listarPorNome(autores)

        if not id_autores:
            id_autores = repositorio.inserirAutor(autores)
            
        cursor.execute("INSERT INTO livros (nome, genero) VALUES (%s, %s)", (nome, genero))
        conexao.commit()
        id_livro = cursor.lastrowid

        repositorio_livros_autores.inserirLivroAutor(id_livro, id_autores)

        cursor.close()
        conexao.close()

        return id_livro

    def listarLivros(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, genero FROM livros")

        registros = cursor.fetchall()
        cursor.close()
        conexao.close()

        return registros

    def alterar(self, nome, genero, id):
        conexao = self.conectar()

        cursor = conexao.cursor()

        sql = "UPDATE livros SET nome=%s, genero=%s WHERE id=%s"
        valores = (nome, genero, id)
        cursor.execute(sql, valores)

        conexao.commit()
        total_afetados = cursor.rowcount
        
        cursor.close()
        conexao.close()

        return total_afetados
    
    def apagar(self, id):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM livros WHERE id = %s", (id,))
        conexao.commit()

        cursor.close()
        conexao.close()
        return cursor.rowcount
    
    def listarPorNome(self, nome):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros WHERE nome = %s", (nome,))

        registro = cursor.fetchone()
        cursor.close()
        conexao.close()

        return registro

    def listarPorId(self, id):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT * FROM livros WHERE id = %s", [id])

        registro = cursor.fetchone()
        cursor.close()
        conexao.close()

        return registro
    
    def listarGeneros(self):
            conexao = self.conectar()
            cursor = conexao.cursor()

            cursor.execute("SELECT DISTINCT genero FROM livros")

            registros = cursor.fetchall()
            cursor.close()
            conexao.close()

            return registros
    
    def listarPorGenero(self, genero):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT id, nome, genero FROM livros WHERE genero = %s", (genero,))

        registros = cursor.fetchall()
        cursor.close()
        conexao.close()

        return registros
    
        