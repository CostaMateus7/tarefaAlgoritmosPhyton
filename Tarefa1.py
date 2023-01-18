
# MATEUS COSTA SANTOS
# APESAR DO FUNDO SER ESCURO, NÃO É UMA IMAGEM!!
# Caso queira ver o código no repositório, acesse https://github.com/CostaMateus7/tarefaAlgoritmosPhyton
# Eu evito comentar muito o código para manter uma boa prática de programação. Caso tenha dificuldade na leitura das variáveis e funções, favor passar um feedback para que eu possa melhorar nesse sentido. 

import math

nome = input('Escreva seu nome: ')
print('Bem vindo a loja do Mateus, {}!'.format(nome))

productPrice = input('Digite o valor do produto: ')

if not productPrice.isnumeric() or float(productPrice) < 0:
    print('Valor de produto inválido!')
else:
  productQuant = input('Escreva a quantidade de produtos: ')
  if productQuant.isdigit() and int(productQuant) > 0 :
    productQuant = int(productQuant)
    productPrice = float(productPrice)
    freteFactor = math.floor(math.log10(max(1, abs(productQuant-1))))
    subTotal = productPrice * productQuant
    total = subTotal + 30 * 2 ** (freteFactor)
    print('O valor sem o frete foi: R${}'.format(subTotal))
    print('O valor com o frete foi: R${}'.format(total))
  else:
    print('Quantidade de produto inválido!')
