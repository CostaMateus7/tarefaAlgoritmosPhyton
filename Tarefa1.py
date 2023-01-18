
# MATEUS COSTA SANTOS
# APESAR DO FUNDO SER ESCURO, NÃO É UMA IMAGEM!!
# Caso queira ver o código no repositório, acesse https://github.com/CostaMateus7/tarefaAlgoritmosPhyton
# Eu evito comentar muito o código para manter uma boa prática de programação. Caso tenha dificuldade na leitura das variáveis e funções, favor passar um feedback para que eu possa melhorar nesse sentido. 


nome = input('Escreva seu nome: ')
print('Bem vindo a loja do Mateus, {}!'.format(nome))



while True:

  productPrice = float(input('Digite o valor do produto: '))
  if(productPrice<0):
    continue

  productQuant = float(input('Escreva a quantidade de produtos: '))

  if((productQuant % 2) == 0 or (productQuant + 1) % 2 == 0):
    
    if(0 <= productQuant < 11):
      subTotal = productPrice * productQuant
      total = subTotal + 30
      print('O valor sem o frete foi: R${}'.format(subTotal))
      print('O valor com o frete foi: R${}'.format(total))
      break
    elif(11 <= productQuant < 101):
      subTotal = productPrice * productQuant
      total = subTotal + 60
      print('O valor sem o frete foi: R${}'.format(subTotal))
      print('O valor com o frete foi: R${}'.format(total))
      break
    elif(101 <= productQuant < 1001):
      subTotal = productPrice * productQuant
      total = subTotal + 120
      print('O valor sem o frete foi: R${}'.format(subTotal))
      print('O valor com o frete foi: R${}'.format(total))
      break
    elif(productQuant >= 1001):
      subTotal = productPrice * productQuant
      total = subTotal + 240
      print('O valor sem o frete foi: R${}'.format(subTotal))
      print('O valor com o frete foi: R${}'.format(total))
      break
  else:
    print('Quantidade de produto inválido!')
    continue




