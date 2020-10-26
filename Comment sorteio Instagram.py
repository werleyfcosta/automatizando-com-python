import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome(r'C:\Users\corte\Desktop\chromedriver.exe')

driver.get('https://www.instagram.com')
time.sleep(60)
driver.get('''link da publicação do sorteio''')
time.sleep(5)
x = 12
y = 1
z = 0
tempo_all = 0 

while x < 50:
    try:
        list= [
        '@nomes_usuario',
        '@nomes_usuario1',
        '@nomes_usuario2',
        '@nomes_usuario3',
        '@nomes_usuario4',
        '@nomes_usuario5',
        '@nomes_usuario6',
        '@nomes_usuario7',
        '@nomes_usuario8',
        '@nomes_usuario9',
        '@nomes_usuario10',
        '@nomes_usuario11',
        '@nomes_usuario12',
        '@nomes_usuario13',
        '@nomes_usuario14',
        '@nomes_usuario15',
        '@nomes_usuario16',
        '@nomes_usuario17',
        '@nomes_usuario18',
        '@nomes_usuario19',
        '@nomes_usuario20',
        '@nomes_usuario21',
        '@nomes_usuario22',
        '@nomes_usuario23',
        '@nomes_usuario24',
        '@nomes_usuario25',
        '@nomes_usuario26',
        '@nomes_usuario27',
        '@nomes_usuario28',
        '@nomes_usuario29',
        '@nomes_usuario30',
        '@nomes_usuario31',
        '@nomes_usuario32',
        '@nomes_usuario33',
        '@nomes_usuario34',
        '@nomes_usuario35',
        '@nomes_usuario36',
        '@nomes_usuario37',
        '@nomes_usuario38',
        '@nomes_usuario39',
        '@nomes_usuario40',
        '@nomes_usuario41',
        '@nomes_usuario42',
        '@nomes_usuario43',
        '@nomes_usuario44',
        '@nomes_usuario45',
        '@nomes_usuario46',
        '@nomes_usuario47',
        '@nomes_usuario48',
        '@nomes_usuario49',
        '@nomes_usuario50'        
        ]
        
        list1 = [62, 64, 68, 70, 75, 73, 80, 72, 81, 85, 65, 90, 83, 78, 92]
        list2 = [10, 12, 14, 15, 23, 27, 18, 21, 35, 25, 16, 13]
        
        
        sorteio_coment = random.choice(list1)
        sorteio_post = random.choice(list2)
        
        
        sorteio_c = int(sorteio_coment)
        sorteio_p = int(sorteio_post)
        
        print('Tempo do comentário: %s' %(sorteio_c))
        print('Tempo de envio do comentário: %s' %(sorteio_p))
        
        site = str(list[x])
        site1 = str(list[y])
        
        
        time.sleep(sorteio_c)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea').send_keys('Eu quero %s %s' %(site, site1))
        
        time.sleep(sorteio_p)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button').click()
                                        
        if y < 252:
            y += 1
        elif x <= 253:
            x += 1
            y = 0
        z += 1
        
        tempo_all += sorteio_c + sorteio_p
        print('Tempo total de execução até agora %s segundos em %s vezes' %(tempo_all, z))
        print("|______________________________________________________________|")
        
    except:
        print('tá dando errado')
        
        time.sleep(sorteio_c)
        driver.get('''link da publicação do sorteio''')
        
        tempo_all += sorteio_c + sorteio_p
        pass

    
    
