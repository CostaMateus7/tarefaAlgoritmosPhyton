print('Bem vindo ao sistema de controle de funcionários do Mateus Costa.')





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
      print('teste')
      break
    elif(select == 2):
      print(2)
      break
    elif(select==3):
      print(3)
      break
    elif(select == 4):
      print('Saiu')
      break
  except:
    continue
  