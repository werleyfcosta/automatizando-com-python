import time
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

time.sleep(25)
x = 0
cont = 0
 
while x <= 50:

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

        site = str(list[cont])
        driver.get('https://www.instagram.com/%s' %(site))
        time.sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button').click()
        
        time.sleep(4)
        x +=1 
        cont += 1
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/button').click()
        time.sleep(4)        
        x +=1 
        cont += 1
    except:       
        x +=1 
        cont += 1
