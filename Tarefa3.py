# MATEUS COSTA SANTOS
# APESAR DO FUNDO SER ESCURO, NÃO É UMA IMAGEM!!
# Caso queira ver o código no repositório, acesse https://github.com/CostaMateus7/tarefaAlgoritmosPhyton
# Eu evito comentar muito o código para manter uma boa prática de programação. Caso tenha dificuldade na leitura das variáveis e funções, favor passar um feedback para que eu possa melhorar nesse sentido. 

print('Seja bem vindo(a) ao Programa de Serviços de Limpeza do Mateus Costa!')

# FUNCTIONS
def tipoLimpeza():
  while True:
    print('-'*10, 'Menu 2 - Tipo de Limpeza.', '-'*10)
    print('B – Básica - Indicada para sujeiras semanais ou quinzenais')
    print('C – Completa - Indicada para sujeiras antigas e/ou não rotineiras')
    tipo = input('Qual será o tipo de limpeza?(B/C) ').upper()
    if(tipo == 'B'):
      return 1.00
    elif(tipo == 'C'):
      return 1.3
    else:
      print('Tipo de limpeza inválido!')
      continue

def adicional():
  listaAdicional = []
  somatorio = 0
  while True:
    print('-'*10, 'Menu 3 - Adicional', '-'*10)
    print('0- Não desejo mais nada (encerrar) 0,00')
    print('1- Passar 10 peças de roupas - R$10,00')
    print('2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00')
    print('3- Limpeza de 1 Geladeira/Freezer - R$ 20,00')
    add = input('Digite a opção desejada (0, 1, 2, 3): ')
    if(add == '0'):
      for total in listaAdicional:
        somatorio+=total
      return somatorio
    elif(add == '1'):
      listaAdicional.append(10)
      continue
    elif(add == '2'):
      listaAdicional.append(12)
      continue
    elif(add == '3'):
      listaAdicional.append(20)
      continue
    else:
      print('Código inválido!')
      continue
  
def metragemLimpeza():
  print('-'*10, 'Menu 1 - Metragem Limpeza.', '-'*10)
  while True:
    try:
      metragem = float(input('Informe a metragem da casa (em m²): '))
      if(metragem < 30 or metragem > 700):
        print('Não aceitamos metragem menor que 30m² ou maior que 700m²')
        continue
      elif(metragem > 30 and metragem <= 299):
        print('É necessário contratar 1 pessoa!')
        metragem = 60 + 0.3 * metragem 
        return metragem
      elif(metragem > 299 and metragem <= 699):
        print('É necessário contratar 2 pessoas!')
        metragem = 120 + 0.5 * metragem
    except:
      print('Adicional inválido!!')
      continue




# APLICAÇÃO PRINCIPAL:

while True:
    metragem = metragemLimpeza()
    tipo = tipoLimpeza()
    add = adicional()
    print('Total: R${} (metragem: {} * tipo: {} + adicional: {}) '.format(round((metragem * tipo + add), 2), metragem, tipo, add))
    break
 