import sqlite3
from time import sleep
from prettytable import PrettyTable

arquivo_db = "bylearn.db"

conexao = None
sql_buscar_alunos = 'SELECT * FROM Aluno;'

def exibirAlunos():
    print('Exibindo...')
    sleep(1)
    cursor.execute(sql_buscar_alunos)
    alunos = cursor.fetchall()
    x = PrettyTable()
    x.field_names = (["Nome", "ID"])
    for aluno in alunos:
        x.add_row([aluno[0], aluno[1]])
        # print(f'Nome: {aluno[0]} | ID: {aluno[1]}')
    print(x)
    sleep(2)

def addAlunos(nome, id):
    print('Adicionando...')
    sleep(1)
    sql_add_aluno = f'INSERT INTO Aluno(nome, id) VALUES("{nome}", "{id}")'
    cursor.execute(sql_add_aluno)
    sleep(2)

def removeAluno(id):
    print('Removendo...')
    sleep(1)
    sql_remover_alunos = f'DELETE FROM Aluno WHERE id = "{id}"'
    cursor.execute(sql_remover_alunos)
    sleep(2)

try:
    conexao = sqlite3.connect(arquivo_db)
    cursor = conexao.cursor()
    print('-'*40)
    print("Deu certo! Estamos usando o sqlite na versão:", sqlite3.version)
    print('Seja bem vindo!')
    cursor.execute('CREATE TABLE IF NOT EXISTS Aluno(nome INTEGER, id INTEGER);')
    opcao = ''
    print('-'*40)
    while opcao != 4:
        opcao = int(input('Qual operação deseja realizar?\n1- Adcionar aluno\n2- Remover aluno\n3- Exibir alunos\n4- Sair\n> '))
        if opcao == 1:    
            print('-'*30)
            nome = input('Insira nome do aluno: ')
            id = input('Insira id do aluno: ')
            addAlunos(nome, id)
            print('-'*30)
        elif opcao == 2:
            print('-'*30)
            id = input('Informe a id do aluno que deseja remover: ')
            removeAluno(id)
            print('-'*30)
        elif opcao == 3:
            print('-'*30)
            exibirAlunos()
            print('-'*30)
        elif opcao == 4:
            print('Saindo...')
            sleep(1)
            break
        else:
            print('-'*30)
            print('Resposta inválida, tente novamente.')
            print('-'*30)

except sqlite3.Error as e:
    print('Ops... Deu um erro: ',e)
finally:
    if conexao:
        conexao.commit()
        conexao.close()
