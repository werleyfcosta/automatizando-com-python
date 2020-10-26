import time

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException

(r'C:\Users\werley.f.costa\desktop\chromedriver.exe')


def autenticacao():

    try:
        analista = 'Werley Ferreira da Silva Costa'
        driver = webdriver.Chrome(r'C:\Users\corte\Desktop\chromedriver.exe') 
        driver.get('Link do portal da empresa')
        time.sleep(2)
        driver.find_element_by_xpath('//a[@class="set-login-type-link"]').click()
        time.sleep(2)
        user_box = driver.find_element_by_id('username')
        user_box.send_keys('meuuser.a.c') #Coloca o teu ID aqui.
        time.sleep(1)
        driver.find_element_by_xpath('//button[@class="btn btn-lg btn-primary btn-block"]').click()
        time.sleep(3)
        email_box = driver.find_element_by_id('i0116')
        email_box.send_keys('email@outlook.com') #Coloca o teu email aqui
        time.sleep(2)
        driver.find_element_by_xpath('//input[@class="btn btn-block btn-primary"]').click()
        time.sleep(7)
        pass_box = driver.find_element_by_id('passwordInput')
        pass_box.send_keys('mypasswordarehere') #Coloca a tua senha aqui
        time.sleep(1)
        driver.find_element_by_xpath('//span[@class="submit"]').click()
        time.sleep(25)
        driver.find_element_by_xpath('//*[@id="vipSkipBtn"]').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
        time.sleep(5)
        print ('\nAtualmente o _Reset Senha está fixado em 97 - Full XPath')
        xpath = input('Defina o valor do XPath dos templates de abertura do chamado:\n\n1. Valor permanece igual\n2. Valor aumentou\n3. Valor diminuiu\n\nOpcao: ')

        if xpath == 1:
            xpath == 0
        elif xpath == 2:
            xpath = int(input('\nInforme quando do XPath aumentou: '))
            print (' ')
        elif xpath == 3:
            xpath = int(input('Informe quando do XPath diminuiu(Informar valor negativo contendo '-' ): '))  
            print (' ')

           

        menu(driver, analista, xpath)

    except:

        print(' ______________________________________________')

        print('|                                              |')

        print('|   Ocorreu uma falha durante a autenticacao   |')

        print('|______________________________________________|')

        autenticacao()

 

def resetsenha(usuario, localidade, driver, analista, xpath):

 

    try:      
        
        cont = 0
        while 1 > cont:   
            driver.get('Link do portal da empresa')
            time.sleep(1)
            driver.get('Link do portal da empresa')
            time.sleep(3)             

            casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')
            time.sleep(1)
            casa1 = casa.get_attribute('value')       
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('01. Informações acesso home')
            time.sleep(3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[1]/a[1]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)
            time.sleep(3)
            driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('O usuário entrou em contato com problemas no Citrix. O mesmo foi informado de que o Citrix se encontrava em manutenção e que deveria aguardar a normalização.')
            time.sleep(4)       
            driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()
            time.sleep(5)
            cont += 1
            print('Numeraçao do chamado é: %s' %casa1)
            print('--------------------------------------')
        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

   

def desbloqusuario(usuario, localidade, driver, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(3)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Desbloqueio do Usuário no AD')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[94]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Usuário solicita reset de senha.\n\nLogin de acesso: %s\nLocalidade: %s' %(usuario, localidade))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

       

def sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(3)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Desbloqueio de Sessão Totvs')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[93]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Usuário solicita desbloqueio da base Pandurata Alimentos.\n\nLogin de acesso: %s\nLocalidade: %s' %(usuario, localidade))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

       

 

 

def criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(3)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Criação/Reativação de FUSER')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[91]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Motivo da solicitação: %s.\n\nUsuario FUSER: %s\nEmpresa: %s\nTempo de uso: %s dias' %(motivcria, userfuser, empsol, tempfuser))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

       

        

def mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(3)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Mapeamento de impressora')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[95]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Motivo da solicitação: %s.\n\nUsuario FUSER: %s\nEmpresa: %s\nTempo de uso: %s dias' %(motivcria, userfuser, empsol, tempfuser))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

       

        

def mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(4)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Mapeamento de Pasta de Rede')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[96]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Motivo da solicitação: %s.\n\nUsuario FUSER: %s\nEmpresa: %s\nTempo de uso: %s dias' %(motivcria, userfuser, empsol, tempfuser))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)       

        

 

def sessaocitrix(usuario, localidade, driver, analista, xpath):

    try:

        driver.get('Link do portal da empresa')

        time.sleep(1)

        driver.get('Link do portal da empresa')

        time.sleep(3)

        casa = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[1]/div[1]/div[1]/div[2]/input[1]')

        time.sleep(1)

        casa1 = casa.get_attribute('value')       

        time.sleep(3)

        driver.find_element_by_xpath('/html/body/div[3]/div/button[1]').click()

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="overflowTemplateSearch"]').send_keys('_Derrubar Usuário no Citrix Studio')

        time.sleep(2)

        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div/div/ul/li[92]').click()   

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.caller_id"]').send_keys(usuario)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').click()

        time.sleep(2)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.location"]').send_keys(localidade)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="sys_display.incident.assigned_to"]').send_keys(analista)

        time.sleep(3)

        driver.find_element_by_xpath('//*[@id="incident.description"]').send_keys('Usuário solicita reset de senha.\n\nLogin de acesso: %s\nLocalidade: %s' %(usuario, localidade))

        time.sleep(4)       

        driver.find_element_by_xpath('/html/body/div[1]/span/span/nav/div/div[2]/span[1]/span[2]/span/button[1]').click()

        time.sleep(5)

        print('Numeraçao do chamado é: %s' %casa1)

        print('--------------------------------------')

        menu(driver, analista, xpath)

    except:

        print('Falha ao encontrar Botão...')

        menu(driver, analista, xpath)

 

 

def menu(driver, analista, xpath):     

    opcoes = input('Opções de abertura de chamados:\n\n1. Reset de senha\n2. Desbloqueio de usuário\n3. Desbloqueio de Sessão do TOTVS\n4. Criação/Renovação de usuários FUSER\n5. Mapeamento de impressora\n6. Mapeamento de pasta na rede\n7. Desbloqueio de sessão Citrix\n\nOpcao: ')

    print('--------------------------------------')

   

# Chamado de reset de senha

# Chamado de reset de senha

# Chamado de reset de senha

# Chamado de reset de senha

  

    if opcoes == '1':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - Matriz Escritório'

            resetsenha(usuario, localidade, driver, analista, xpath)

       

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            resetsenha(usuario, localidade, driver, analista, xpath)

 

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'           

            resetsenha(usuario, localidade, driver, analista, xpath)

 

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            resetsenha(usuario, localidade, driver, analista, xpath)

               

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            resetsenha(usuario, localidade, driver, analista, xpath)

           

 

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            resetsenha(usuario, localidade, driver, analista, xpath)

          

 

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            resetsenha(usuario, localidade, driver, analista, xpath)

           

 

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            resetsenha(usuario, localidade, driver, analista, xpath)

           

 

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            resetsenha(usuario, localidade, driver, analista, xpath)

           

 

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            resetsenha(usuario, localidade, driver, analista, xpath)

           

 

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            resetsenha(usuario, localidade, driver, analista, xpath)

                            

 

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            resetsenha(usuario, localidade, driver, analista, xpath)

 

 

# Chamado Desbloqueio de usuário           

# Chamado Desbloqueio de usuário

# Chamado Desbloqueio de usuário

# Chamado Desbloqueio de usuário

 

           

    elif opcoes == '2':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - Matriz Escritório'

            desbloqusuario(usuario, localidade, driver, analista, xpath)

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            desbloqusuario(usuario, localidade, driver, analista, xpath)

 

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'           

            desbloqusuario(usuario, localidade, driver, analista, xpath)

 

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            desbloqusuario(usuario, localidade, driver, analista, xpath)

               

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            desbloqusuario(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            desbloqusuario(usuario, localidade, driver, analista, xpath)          

 

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            desbloqusuario(usuario, localidade, driver, analista, xpath)          

 

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            desbloqusuario(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            desbloqusuario(usuario, localidade, driver, analista, xpath)          

 

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            desbloqusuario(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            desbloqusuario(usuario, localidade, driver, analista, xpath)                            

 

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            desbloqusuario(usuario, localidade, driver, analista, xpath)

           

            

# Chamado Desbloqueio de Sessão TOTVS           

# Chamado Desbloqueio de Sessão TOTVS

# Chamado Desbloqueio de Sessão TOTVS

# Chamado Desbloqueio de Sessão TOTVS

       

    

    elif opcoes == '3':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - CD Ceará'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)              

                

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            emptotvs = input('Selecione a base do TOTVS.\n\n1. Minha Empresa\n2. Pandurata Varejo\n\nOpcao: ')

            if emptotvs == '1':

                emptotvs = 'Minha Empresa'

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

            if emptotvs == '2':

                emptotvs = 'Pandurata Varejo'           

                sessaototvs(usuario, localidade, driver, emptotvs, analista, xpath)

               

        

# Chamado Criação/Reativação de FUSER       

# Chamado Criação/Reativação de FUSER

# Chamado Criação/Reativação de FUSER

# Chamado Criação/Reativação de FUSER     

        

        

        

    elif opcoes == '4':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - CD Ceará'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                      

                

                

        

        

        

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                

        

        

        

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                    

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

               

        

        

        

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)               

                

        

        

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            userfuser = input('Digite o usuário da rede FUSER: ')

            print('--------------------------------------')

            motivcria = input('Selecione a base do TOTVS.\n\n1. Criação de usuario\n2. Reativacao de usuario\n\nOpcao: ')

            print('--------------------------------------')

            if motivcria == '1':

                motivcria = 'Criação de novo acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

                   

            if motivcria == '2':

                motivcria = 'Reativação de acesso na rede FUSER'

                empsol = input('Selecione a empresa:\n\n1. Bauducco\n2. Terceiro\n\nOpcao: ')

                if empsol == '1':

                    empsol = 'Bauducco'

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)                   

                elif empsol == '2':

                    print('--------------------------------------')

                    empsol = input('Digite o nome da empresa terceira\n\n Empresa: ')

                    print('--------------------------------------')

                    tempfuser = input('Digite o tempo de duracao do usuario(Forma numérica): ')

                    print('--------------------------------------')

                    criarfuser(usuario, localidade, driver, userfuser, motivcria, empsol, tempfuser, analista, xpath)

 

#Mapeamento de impressora

#Mapeamento de impressora

#Mapeamento de impressora

#Mapeamento de impressora

 

 

    elif opcoes == '5':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - CD Ceará'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath) 

                

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')                

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

                

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

               

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            srvrimpre = input('Digite o nome do Servidor: ')

            nameimpre = input('Digite o nome da impressora: ')               

            mapimpre(usuario, localidade, driver, srvrimpre, nameimpre, analista, xpath)

                   

  

# Mapeamento de pasta de rede

# Mapeamento de pasta de rede

# Mapeamento de pasta de rede

# Mapeamento de pasta de rede

 

 

    elif opcoes == '6':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - CD Ceará'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

                

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            srvrpasta = input('Digite o nome do Servidor: ')

            namepasta = input('Digite o nome da pasta: ')               

            mappasta(usuario, localidade, driver, srvrpasta, namepasta, analista, xpath) 

            

            

# Desbloqueio sessão citrix

# Desbloqueio sessão citrix

# Desbloqueio sessão citrix

# Desbloqueio sessão citrix

 

 

    elif opcoes == '7':

        usuario = input('Digite o nome do usuário: ')

        print('--------------------------------------')

        localidade = input('Digite a localidade:\n\n1. Minha Empresa - CD Ceará\n2. Minha Empresa - CD Rio Grande do Sul\n3. Minha Empresa - CD GLP\n4. Minha Empresa - CD Rio Largo\n5. Minha Empresa - CD Extrema\n6. Minha Empresa - CD Olaria\n7. Minha Empresa - CD Pernanbuco\n8. Minha Empresa - Matriz Escritório\n9. Minha Empresa - Fabrica Bonsucesso\n10. Minha Empresa - Fabrica Endres\n11. Minha Empresa - Fabrica Extrema\n12. Minha Empresa - Fabrica Rua Argentina\n\nOpcao: ')

        print('--------------------------------------')

        if localidade == '1':

            localidade = 'Minha Empresa - Matriz Escritório'

            sessaocitrix(usuario, localidade, driver, analista, xpath)

           

        if localidade == '2':

            localidade = 'Minha Empresa - CD Rio Grande do Sul'

            sessaocitrix(usuario, localidade, driver, analista, xpath)

 

        if localidade == '3':

            localidade = 'Minha Empresa - CD GLP'           

            sessaocitrix(usuario, localidade, driver, analista, xpath)

 

        if localidade == '4':

            localidade = 'Minha Empresa - CD Rio Largo'

            sessaocitrix(usuario, localidade, driver, analista, xpath)

               

        if localidade == '5':

            localidade = 'Minha Empresa - CD Extrema'

            sessaocitrix(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '6':

            localidade = 'Minha Empresa - CD Olaria'

            sessaocitrix(usuario, localidade, driver, analista, xpath)          

 

        if localidade == '7':

            localidade = 'Minha Empresa - CD Pernanbuco'

            sessaocitrix(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '8':

            localidade = 'Minha Empresa - Matriz Escritório'

            sessaocitrix(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '9':

            localidade = 'Minha Empresa - Fabrica Bonsucesso'

            sessaocitrix(usuario, localidade, driver, analista, xpath)          

 

        if localidade == '10':

            localidade = 'Minha Empresa - Fabrica Endres'

            sessaocitrix(usuario, localidade, driver, analista, xpath)           

 

        if localidade == '11':

            localidade = 'Minha Empresa - Fabrica Extrema'

            sessaocitrix(usuario, localidade, driver, analista, xpath)                             

 

        if localidade == '12':

            localidade = 'Minha Empresa - Fabrica Rua Argentina'

            sessaocitrix(usuario, localidade, driver, analista, xpath)          

      

                

autenticacao()