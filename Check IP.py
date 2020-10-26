yourip = input('Digite o ip que você deseja')

teste = (yourip[:3])
teste = teste.replace (".","")
teste = int(teste)

if (type(teste) is int):
    print('Esse número é inteiro %i' %teste)
else:
    print('Operação inválida')

