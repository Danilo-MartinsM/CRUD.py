from livrosRepository import LivrosRepository
from livrosAutoresRepository import LivrosAutoresRepository
from autoresRepository import AutoresRepository


def inserir():
    repositorio = LivrosRepository()
    while True:
        nome = input('Nome: ').strip().title()
        if nome:
            break
        print("O nome não pode ficar vazio. Tente novamente.")

    genero = input('Gênero: ').strip().title()
    autores = input('Autor(es) (Separe por vírgula se houver mais de um): ').strip().title()

    autores = autores.split(', ')

    id_livro = repositorio.inserir(nome, genero, autores)

    print(f"Livro '{nome}' inserido com ID {id_livro}.")

def listar_livros():
    repositorio = LivrosRepository()
    livros = repositorio.listarLivros()

    print("ID\tNome\tGênero")
    for livro in livros:
        id, nome, genero = livro
        print(f'{id}\t{nome}\t{genero}')
    return

def alterar():
    repositorio = LivrosRepository()
    id = int(input("ID do livro para alterar: "))
    livro = repositorio.listarPorId(id)
    
    if not livro:
        print("Livro não encontrado.")
        return
    
    id, nome_atual, genero_atual = livro
    
    novo_nome = input(f"Nome [{nome_atual}]: ").strip()
    if novo_nome == "":
        novo_nome = nome_atual
    
    novo_genero = input(f"Gênero [{genero_atual}]: ").strip()
    if novo_genero == "":
        novo_genero = genero_atual

    total_afetados = repositorio.alterar(novo_nome, novo_genero,id)
    print(f"{total_afetados} registro(s) alterado(s).")

def apagar():
    repositorio = LivrosRepository()
    repositorio_livros_autores = LivrosAutoresRepository()
    id = int(input("ID do livro para apagar: ")).strip()
    livro = repositorio.listarPorId(id)

    if not livro:
        print("Livro não encontrado.")
        return
    
    _, nome, _ = livro

    confirmacao = input(f"Tem certeza que quer apagar o livro '{nome}'? (digite 'sim' para confirmar): ").strip().lower()
    if confirmacao != 'sim':
        print("Operação cancelada.")
        return
    
    total_afetados = repositorio_livros_autores.apagarLivrosAutores(id)
    total_afetados = repositorio.apagar(id)

    if total_afetados > 0:
        print(f"Livro '{nome}' apagado com sucesso.")
    else:
        print("Erro ao apagar o livro.")


def listar_por_nome():
    repositorio = LivrosRepository()
    nome = input('Nome: ').strip()
    livro = repositorio.listarPorNome(nome)

    print("ID\tNome\tGênero")
    if livro:
        id, nome, genero = livro
        print(f"{id}\t{nome}\t{genero}")
    else:
        print("Livro não encontrado.")
    return

def listar_por_id():
    repositorio = LivrosRepository()
    id = input('ID: ').strip()
    livro = repositorio.listarPorId(id)

    print("ID\tNome\tGênero")
    if livro:
        id, nome, genero = livro
        print(f"{id}\t{nome}\t{genero}")
    else:
        print("Livro não encontrado.")
    return

def listar_livros_autores():
    repositorio = LivrosAutoresRepository()
    livros_autores = repositorio.listarLivrosAutores()
    
    print("Id\tLivro\tGênero\tAutor(es)")
    for id, nome, genero, autor in livros_autores:
        print(f"{id}\t{nome}\t{genero}\t{autor}")
    return

def listar_autores():
    repositorio = AutoresRepository()
    autores = repositorio.listarAutores()

    print("ID\tNome")
    for autor in autores:
        id, nome = autor
        print(f'{id}\t{nome}')
    return

def listar_por_genero():
    repositorio = LivrosRepository()
    generos = repositorio.listarGeneros()
    print("Gêneros disponíveis:")
    for genero in generos:
        genero = genero
        print(genero[0])
    genero = input('Digite o gênero: ').strip().lower()
    livros = repositorio.listarPorGenero(genero)

    print("ID\tNome\tGênero")
    for livro in livros:
        id, nome, genero = livro
        print(f'{id}\t{nome}\t{genero}')
    return


while True:
    print('1. Cadastrar livros')
    print('2. Listar livros')
    print('3. Alterar livros')
    print('4. Apagar livros')
    print('5. Listar livros por nome')
    print('6. Listar livros por id')
    print('7. Listar livros com autores')
    print('8. Listar autores')
    print('9. Listar por Gênero')
    print('0. Sair')
    opcao = int(input())
    if opcao == 1:
        inserir()
    elif opcao == 2:
        listar_livros()
    elif opcao == 3:
        listar_livros()
        alterar()
    elif opcao == 4:
        listar_livros()
        apagar()
    elif opcao == 5:
        listar_por_nome()
    elif opcao == 6:
        listar_por_id()
    elif opcao == 7:
        listar_livros_autores()
    elif opcao == 8:
        listar_autores()
    elif opcao == 9:
        listar_por_genero()
    elif opcao == 0:
        print('tchau')
        break