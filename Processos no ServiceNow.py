import time
from selenium import webdriver
import sys


print("email e transferencia de ramal")
driver = webdriver.Chrome(executable_path=r'C:\users\chromedriver.exe') #this is my path, I haven't worked out how to make the path relative to the script yet




driver.get('Portal do ServiceNow')
time.sleep(2)




id_box = driver.find_element_by_id('sso_selector_id')
id_box.send_keys('''My user''')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="loginPage"]/table/tbody/tr[3]/td[3]/button').click()
time.sleep(5)
login = driver.find_element_by_xpath('//*[@id="i0116"]')
time.sleep(1)
login.send_keys('''Minha email''')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('''minha senha''')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()

time.sleep(20)

try:
    
    try:
        driver.find_element_by_xpath('//*[@id="vipSkipBtn"]').click()            
    except:
        time.sleep(30)
    time.sleep(7)
    driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
    time.sleep(5)

    driver.get('Portal do ServiceNow')
    time.sleep(8)

    driver.find_element_by_xpath('//*[@id="s2id_sp_formfield_pan_mailbox_req_type"]/a/span[2]/b').click()
    time.sleep(3)
    

    driver.find_element_by_xpath('//*[@id="select2-result-label-18"]').click()
    time.sleep(2)
    


    driver.find_element_by_xpath('//*[@id="s2id_sp_formfield_pan_mailbox_type"]/a/span[2]/b').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="select2-result-label-24"]').click()
    time.sleep(1)
    
    
    teste = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/sp-page-row[3]/div/div/span/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[3]/div/div/div[2]/div/span/textarea')
    time.sleep(1)
    teste.click()
    time.sleep(1)
    teste.send_keys("atribuir licenca para ", sys.argv[2])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sc_cat_item"]/div[1]/div[2]/div/div[1]/div[3]/button')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="sc_cat_item"]/div[1]/div[2]/div/div[1]/div[3]/button').click()
    time.sleep(15)

    
    tree = driver.find_element_by_xpath('//*[@id="xdcd2ae50db0973043181d36fdf961977"]/div/div/div[1]/div/h2')
    time.sleep(3)
    teco = tree.text
    
    print(tree.text)

    driver.get('Portal do ServiceNow')

    alo = driver.find_element_by_xpath('/html/body/div[1]/div[1]/span/div/div[6]/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/a')
    time.sleep(1)
    alo.click()
    time.sleep(6)
    eram = driver.find_element_by_xpath('//*[@id="sys_display.sc_task.assignment_group"]')
    time.sleep(1)
    eram.clear()

    time.sleep(1)

    eram.send_keys('Workplace-Office 365')
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="sysverb_update"]').click()

    time.sleep(4)
       

    driver.get('Portal do ServiceNow')
    
    time.sleep(7)
    

    aloo = driver.find_element_by_xpath('//*[@id="sys_display.sc_task.request_item"]')
    time.sleep(1)
    aloo.click()
    time.sleep(1)
    aloo.send_keys(teco)
    time.sleep(1)

    alo5 = driver.find_element_by_xpath('//*[@id="sc_task.short_description"]')
    time.sleep(1)
    alo5.click()
    time.sleep(1)
    alo5.send_keys('licenca atribuida - ', sys.argv[1] ,' - ', sys.argv[2])
    time.sleep(2)
    alo6 = driver.find_element_by_xpath('//*[@id="sysverb_insert"]')
    time.sleep(1)
    alo6.click()
    time.sleep(5)
    
    

    driver.get('Portal do ServiceNow')
    time.sleep(8)

    driver.find_element_by_xpath('//*[@id="s2id_sp_formfield_pan_mailbox_req_type"]/a/span[2]/b').click()
    time.sleep(3)
    

    driver.find_element_by_xpath('//*[@id="select2-result-label-18"]').click()
    time.sleep(2)
    


    driver.find_element_by_xpath('//*[@id="s2id_sp_formfield_pan_mailbox_type"]/a/span[2]/b').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="select2-result-label-24"]').click()
    time.sleep(1)
    
    
    teste = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/sp-page-row[3]/div/div/span/div/div/div[1]/div[1]/div/div[2]/form/div/sp-variable-layout/fieldset[3]/div/div/div[2]/div/span/textarea')
    time.sleep(1)
    teste.click()
    time.sleep(1)
    teste.send_keys("transferir ramal ", sys.argv[3] , " para ", sys.argv[2] , " ...de acordo do superior na tarefa ", sys.argv[1])
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="sc_cat_item"]/div[1]/div[2]/div/div[1]/div[3]/button')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="sc_cat_item"]/div[1]/div[2]/div/div[1]/div[3]/button').click()
    time.sleep(15)

    
    tree = driver.find_element_by_xpath('//*[@id="xdcd2ae50db0973043181d36fdf961977"]/div/div/div[1]/div/h2')
    time.sleep(3)
    teco2 = tree.text
    
    print(tree.text)

    driver.get('Portal do ServiceNow')
    
    alo = driver.find_element_by_xpath('/html/body/div[1]/div[1]/span/div/div[6]/table/tbody/tr/td/div/table/tbody/tr[1]/td[3]/a')
    time.sleep(1)
    alo.click()
    time.sleep(6)
    eram = driver.find_element_by_xpath('//*[@id="sys_display.sc_task.assignment_group"]')
    time.sleep(1)
    eram.clear()

    time.sleep(1)

    eram.send_keys('Bauducco - Telefonia Fixa')
    time.sleep(1)

    driver.find_element_by_xpath('//*[@id="sysverb_update"]').click()

    time.sleep(6)
    
    driver.get("https://accentureplc.service-now.com/nav_to.do?uri=%2F$sn_global_search_results.do%3Fsysparm_search%3D"+sys.argv[1])
    time.sleep(20)
    driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="gsft_main"]'))
    time.sleep(3)
    try:
        azure = driver.find_element_by_xpath('//*[@id="tarefas_tarefas-de-catalogo"]/section[1]/h1/a')
        time.sleep(2)
    except:
        azure = driver.find_element_by_xpath('/html/body/div/div/div/section/div/section/section/section[1]/h1/a')
        time.sleep(2)

    azure.click()
    time.sleep(20)

    azure2 = driver.find_element_by_xpath('/html/body/div[2]/form/span[1]/span/div[5]/div[2]/div/div[5]/table/tbody/tr/td/div[1]/div/div/div/div[1]/div/div/div[1]/div/div/div/textarea')
    time.sleep(4)

    azure2.send_keys("office - "+teco , " , transferencia de ramal - "+teco2 , " - "+sys.argv[2])
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="sysverb_update"]').click()



except:
    time.sleep(2)
