# MATEUS COSTA SANTOS
# APESAR DO FUNDO SER ESCURO, NÃO É UMA IMAGEM!!
# Caso queira ver o código no repositório, acesse https://github.com/CostaMateus7/tarefaAlgoritmosPhyton
# Eu evito comentar muito o código para manter uma boa prática de programação. Caso tenha dificuldade na leitura das variáveis e funções, favor passar um feedback para que eu possa melhorar nesse sentido. 


print('-'*27, 'Bem vindo a sorveteria do Mateus Santos', '-'*26)
print('| Código |      Descrição       | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml)|')
print('|   TR   | Sabores Tradicionais |       R$6,00      |      R$10,00       |        R$18,00    |')
print('|   ES   |  Sabores Especiais   |       R$7,00      |      R$12,00       |        R$21,00    |')
print('|   PR   |   Sabores Premium    |       R$8,00      |      R$14,00       |        R$24,00    |')
print('-'*94)

pedidos = []
valor = 00
  
def sabor():
  while True:
    sabores = input('Digite o sabor desejado: ').upper()
    if(sabores == 'TR'):
      return sabores
      break
    elif(sabores=='ES'):
      return sabores
      break
    elif(sabores == 'PR'):
      return sabores
      break
    else:
      print('Sabor Incorreto!')
      continue

def total(tamanho, sabor):
  if(tamanho == 'P' and sabor == 'TR'):
    print('Você pediu um sorvete Tradicional tamanho P: R$6,00')
    return 6
  elif(tamanho == 'P' and sabor == 'ES'):
    print('Você pediu um sorvete Especial tamanho P: R$7,00')
    return 7
  elif(tamanho == 'P' and sabor == 'PR'):
    print('Você pediu um sorvete Premium tamanho P: R$8,00')
    return 8
  elif(tamanho == 'M' and sabor == 'TR'):
    print('Você pediu um sorvete Tradicional tamanho M: R$10,00')
    return 10
  elif(tamanho == 'M' and sabor == 'ES'):
    print('Você pediu um sorvete Especial tamanho M: R$12,00')
    return 12
  elif(tamanho == 'M' and sabor == 'PR'):
    print('Você pediu um sorvete Premium tamanho M: R$14,00')
    return 14
  elif(tamanho == 'G' and sabor == 'TR'):
    print('Você pediu um sorvete Tradicional tamanho G: R$18,00')
    return 18
  elif(tamanho == 'G' and sabor == 'ES'):
    print('Você pediu um sorvete Especial tamanho G: R$21,00')
    return 21
  elif(tamanho == 'G' and sabor == 'PR'):
    print('Você pediu um sorvete Premium tamanho G: R$24,00')
    return 24

def repetir():
  while True:
    continuar = input('Você deseja continuar? (S/N): ').upper()
    if(continuar == 'S'):
      return continuar
      break
    elif(continuar == 'N'):
      return continuar
      break
    else:
      continue

def somarTotaldePedidos(ListaPedidos):
  soma = 0
  for valor in ListaPedidos:
    soma+=valor
  return soma

# PROGRAMA PRINCIPAL

while True:
  resultado = 0
  tam = input('Digite o tamanho desejado (P, M, G): ')
  if(tam.upper() == 'P'):
    sabores =  sabor()
    resultado = total('P', sabores)
  elif(tam.upper() == 'M'): 
    sabores = sabor()
    resultado = total('M', sabores)
  elif(tam.upper() == 'G'):
    sabores = sabor()
    resultado = total('G', sabores)
  else:
    print('Tamanho Incorreto!')
    continue
  continuar = repetir()
  if(continuar == 'S'):
    pedidos.append(resultado)
    continue
  else:
    pedidos.append(resultado)
    finalizarTotal = somarTotaldePedidos(pedidos)
    print('Pedido finalizado!')
    print('Valor Total: {}'.format(finalizarTotal))
    break

  