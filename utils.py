import psycopg2

def conectar():
    """
    Função para conectar ao servidor
    """
    try:
        connection = psycopg2.connect(
            host='',
            user='',
            password='',
            database=''
        )
        return connection
    except psycopg2.Error as e:
        print(f'Erro na conexão ao PosgreSQL Server: {e}')

def desconectar(connection):
    """ 
    Função para desconectar do servidor.
    """
    if connection:
        connection.close()


def listar():
    """
    Função para listar os produtos
    """
    connection = conectar()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall();
    #O retorno do resultado será passado como um lista
    if len(produtos) > 0:
        print('Listando produtos...')
        print('--------------------')
        for produto in produtos:
            print(f'ID: {produto[0]}')
            print(f'Produto: {produto[1]}')
            print(f'Preço: {produto[2]}')
            print(f'Estoque: {produto[3]}')
            print('--------------------')
    else:
        print('Não existem produtos cadastrados')

def inserir():
    """
    Função para inserir um produto
    """
    connection = conectar()
    cursor = connection.cursor()

    nome = input('Informe o nome do produto: ')
    preco = input('Informe o preço do produto: ')
    estoque = input('Informe a quantidade em estoque: ')
    sql = "INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)"
    dados = (nome, preco, estoque)
    cursor.execute(sql, dados)

    connection.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi inserido com sucesso')
    else:
        print('Não foi possível inserir')
    desconectar(connection)

def atualizar():
    """
    Função para atualizar um produto
    """
    connection = conectar()
    cursor = connection.cursor()
    codigo = int(input('Informe o código do produto: '))
    nome = input('Informe o novo nome do produto: ')
    preco = float(input('Informe o novo preço do produto: '))
    estoque = int(input('Informe a nova quantidade em estoque: '))
    sql = "UPDATE produtos SET nome=%s, preco=%s, estoque=%s WHERE id=%s"
    dados = (nome, preco, estoque, codigo)
    cursor.execute(sql, dados)
    connection.commit()

    if cursor.rowcount == 1:
        print(f'O produto {nome} foi atualizado com sucesso')
    else:
        print('Erro ao atualizar o produto')
    desconectar(connection)

def deletar():
    """
    Função para deletar um produto
    """
    connection = conectar()
    cursor = connection.cursor()

    codigo = int(input('Informe o código do produto: '))
    sql = (
        f'DELETE FROM produtos WHERE id={codigo}'
    )
    cursor.execute(sql)
    connection.commit()

    if cursor.rowcount == 1:
        print('Produto excluído com sucesso!')
    else:
        print(f'Erro ao excluir o produto com id = {codigo}')
    desconectar(connection)

def menu():
    """
    Função para gerar o menu inicial
    """
    print('=========Gerenciamento de Produtos==============')
    print('Selecione uma opção: ')
    print('1 - Listar produtos.')
    print('2 - Inserir produtos.')
    print('3 - Atualizar produto.')
    print('4 - Deletar produto.')
    opcao = int(input())
    if opcao in [1, 2, 3, 4]:
        if opcao == 1:
            listar()
        elif opcao == 2:
            inserir()
        elif opcao == 3:
            atualizar()
        elif opcao == 4:
            deletar()
        else:
            print('Opção inválida')
    else:
        print('Opção inválida')
