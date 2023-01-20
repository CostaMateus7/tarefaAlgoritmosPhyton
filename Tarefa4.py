# MATEUS COSTA SANTOS
# APESAR DO FUNDO SER ESCURO, NÃO É UMA IMAGEM!!
# Caso queira ver o código no repositório, acesse https://github.com/CostaMateus7/tarefaAlgoritmosPhyton
# Eu evito comentar muito o código para manter uma boa prática de programação. Caso tenha dificuldade na leitura das variáveis e funções, favor passar um feedback para que eu possa melhorar nesse sentido. 


# Passo a passo
import json

print('Bem vindo ao sistema de controle de funcionários do Mateus Costa.')

Tabela = 'Lista de funcionários Txt'
lista = []
contador = 0

def cadastroFuncionario():
  while True:
    try:
      nome= input('Digite o nome do funcionário: ')
      setor= input('Digite o setor do funcionário: ').upper()
      salario = float(input('Digite o salário do funcionário: '))
      funcionario = {
        'id': contador,
        'nome': nome,
        'setor': setor,
        'salario': salario
      }
      lista.append(funcionario)
      listaTXT = lista[:]
    except:
      print('Erro ao abrir o arquivo')
    else:
      with open(Tabela, 'w') as convert_file: 
        convert_file.write(json.dumps(listaTXT))
      a = open(Tabela, 'at')
      return print('Cadastro realizado com sucesso!')
    finally:
      a.close()


def consultarFuncionarios():
  while True:
    print('-'*20, 'MENU CONSULTA', '-'*20)
    print('1- Listar todos os funcionários')
    print('2- Listar funcionários por ID')
    print('3- Listar funcionários por setor')
    print('4- Retornar')
    try:
      listar = int(input('Digite a opção desejada: '))
      if(listar == 1):
        listarArquivo(Tabela)
      elif(listar == 2):
        while True:
          try:
            identificador = int(input('Digite o Id do funcionário: '))
            listarArquivoId(Tabela, identificador)
            break
          except:
            print('Id Incorreto!')
            continue
      elif(listar == 3):
        while True:
          try:
            setor = input('Digite o setor: ').upper()
            listarArquivoSetor(Tabela, setor)
            break
          except:
            print('Setor Incorreto!')
            continue
      elif(listar == 4):
        break
      else:
        continue
    except:
      print('Código incorreto!')
      continue

def removerFuncionario(identificador):
  try:
    a = open(Tabela, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else: 
    listagem = a.read()
    listagem = json.loads(listagem)
    lista=[]
    for funcionario in listagem:
      id, nome, setor, salario = funcionario.values()
      if(identificador != id):
        func = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
      }
        lista.append(func)
        listaTXT = lista[:]
   
  finally:
    with open(Tabela, 'w') as convert_file: 
      convert_file.write(json.dumps(listaTXT))
    a = open(Tabela, 'at')
    a.close()
    return print('Registro deletado com sucesso!')


   


def listarArquivoSetor(NomeArquivo, setorFunc):
  try:
    a = open(NomeArquivo, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else: 
    listagem = a.read()
    listagem = json.loads(listagem)
    for funcionario in listagem:
      id, nome, setor, salario = funcionario.values()
      if(setorFunc == setor):
        print('-'*30)
        print('Id: ', id)
        print('Nome: ', nome)
        print('Setor: ', setor)
        print('Salário: ', salario)
        print('-'*30)
  finally:
    a.close()
    
def listarArquivoId(NomeArquivo, identificador):
  try:
    a = open(NomeArquivo, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else: 
    listagem = a.read()
    listagem = json.loads(listagem)
    for funcionario in listagem:
      id, nome, setor, salario = funcionario.values()
      if(identificador == id):
        print('-'*30)
        print('Id: ', id)
        print('Nome: ', nome)
        print('Setor: ', setor)
        print('Salário: ', salario)
        print('-'*30)
  finally:
    a.close()



def listarArquivo(NomeArquivo):
  try:
    a = open(NomeArquivo, 'rt')
  except:
    print('Erro ao ler o arquivo')
  else: 
    listagem = a.read()
    listagem = json.loads(listagem)
    for funcionario in listagem:
      id, nome, setor, salario = funcionario.values()
      print('-'*30)
      print('Id: ', id)
      print('Nome: ', nome)
      print('Setor: ', setor)
      print('Salário: ', salario)
      print('-'*30)
  finally:
    a.close()

def existeArquivo(nomeArquivo):
  try:
    a = open(nomeArquivo, 'rt')
    a.close()
  except FileNotFoundError:
    return False
  else:
    return True

def criarArquivo(NomeArquivo):
  try:
    a = open(NomeArquivo, 'wt+')
    a.close()
  except:
    print('Erro na criação do arquivo!')
  else:
    print('Arquivo {} foi criado com sucesso'.format(NomeArquivo))


if existeArquivo(Tabela):
  print('Arquivo localizado com sucesso!')
else: 
  print('Não existe arquivo!')
  criarArquivo(Tabela)


# PROJETO PRINCIPAL
while True:
  print('-'*20, 'MENU PRINCIPAL', '-'*20)
  print('1- Cadastrar funcionário')
  print('2- Consultar funcionário')
  print('3- Remover funcionário')
  print('4- Sair')
  try:
    select = int(input('Digite a opção deseja: '))
    if(select == 1):
      contador += 1
      cadastroFuncionario()
      continue
    elif(select == 2):
      consultarFuncionarios()
    elif(select==3):
      while True:
        try:
          id = int(input('Digite o número de identificação do funcionário: '))
          removerFuncionario(id)
          break
        except:
          print('Identificador inválido!')
          continue
    elif(select == 4):
      print('Encerrando o programa!')
      break
  except:
    print('Digite um número válido!')
    continue
  