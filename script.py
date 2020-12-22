import os
import fnmatch
import time

def encontra(items):
    cont = 0
    print('')
    items = items #str(input('Procurar arquivo: '))
    print('')
    opcoes = []
    a = 0
    while a < 5 :
        
        for root, dirs, files in os.walk("."):                    
            try:
                while cont < len(files):      
                                    
                    danosse = files[cont]
                    cont += 1                     
                    if items in danosse:                
                        opcoes.append(danosse)                    
                        if cont == len(files):
                            #print('passei de finim')
                            a = 55   
                    elif cont == len(files):
                        print('passei de rasp')            
                        a = 55
            except:
                pass                
                                                                   
    if len(opcoes) > 0:
        #print(opcoes)        
        return opcoes
    else:
        print('Nenhum arquivo encontrado.')
        opcoes = ['nada']
        return opcoes
        '''
        decision1 = int(input('1. Realizar nova consulta\n2. Sair\nOpção: '))
        if decision1 == 1:
            encontra()
        else:
            print('Encerrando script...')
            time.sleep(5)'''
            
               
def seleciona(opcoes):
    cont = 1   
    if len(opcoes) > 1:
        print('Foram encontrados alguns arquivos com a informação passada.\nSelecione o arquivo que deseja fazer upload')
        for i in opcoes:            
            print('%s. %s'%(cont, i))
            cont += 1
        decision2 = int(input('Opção: '))
        dateaa = opcoes[decision2-1]
        print(opcoes[decision2-1])    
        return dateaa
    
    else:        
        dateaa = opcoes[0]
        print(dateaa)
        return dateaa
    
