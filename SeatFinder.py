
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import smtplib
from email.message import EmailMessage
import getpass


while (True):


    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)

    path=input('Please enter driver path: ')
    browser = webdriver.Chrome(executable_path=path, chrome_options=chrome_options)

    browser.get('https://weblogin.asu.edu/cas/login')

    AsurteId=input('Please enter ASURITE ID: ')
    key=input('Please enter password: ')
    username=browser.find_element_by_name("username")
    username.send_keys(AsurteId)

    password=browser.find_element_by_name("password")
    password.send_keys(key)

    submit=browser.find_element_by_class_name("submit").click()



    time.sleep(5)
    browser.get("https://webapp4.asu.edu/catalog/")

    time.sleep(2)
    subject=browser.find_element_by_class_name("subjectEntry")
    className=input('Please enter class name: ')
    subject.send_keys(className)

    classNumberButton=browser.find_element_by_class_name("catalogNbr")
    classNumber=input('Please enter class number: ')
    classNumberButton.send_keys(classNumber)

    button=browser.find_element_by_id("go_and_search")
    button.click()

    time.sleep(2)

    profName=input('Please enter preferred Teacher: ')

    if browser.page_source.__contains__(profName) is True:

        email= input('Please enter email to be notified at: ')
        emailPassword=getpass.getpass('Please enter email password: ')

        msg=EmailMessage()
        msg.set_content("Seat Found!!!")



        mail= smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,emailPassword)
        mail.sendmail(email,email, msg.as_string())
        mail.close()
        browser.close()






    else:
        print (" No")



    time.sleep(900)







