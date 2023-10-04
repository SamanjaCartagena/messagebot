from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver = webdriver.Chrome()

driver.get("https://linkedin.com")
driver.maximize_window()

time.sleep(2)

username=driver.find_element(By.ID,"session_key")
password = driver.find_element(By.ID,"session_password")
time.sleep(2)
username.send_keys("cart.samanja09@gmail.com")
password.send_keys("Sam#Carta32")
submit=driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(10)
driver.get("https://www.linkedin.com/search/results/people/?keywords=real%20estate&origin=SWITCH_SEARCH_VERTICAL&sid=xpF")
time.sleep(10)
all_buttons= driver.find_elements(By.TAG_NAME,"button")
messages=[btn for btn in all_buttons if btn.text =='Message']
for i in range(0,len(messages)):
   messages[i].click()
   time.sleep(5)
   try:
     subject=driver.find_element(By.XPATH,"//input[@name='subject']")

     if subject.is_displayed():
       subject.send_keys('Hi')
       time.sleep(10)
       main_div  = driver.find_element(By.CLASS_NAME,"msg-form__contenteditable")
       main_div.click()
       main_div.send_keys('Hello there, I have built a bot and I am testing it. Sorry if I bothered you. This is automated and not Samanja')
       time.sleep(10)
       send_button=driver.find_element(By.CLASS_NAME,"msg-form__send-button") 
       send_button.click() 
       time.sleep(5)  
       close=driver.find_element(By.XPATH,"//button//li-icon[@type='close']//*[name()='svg']//*[name()='path' and contains(@d,'M14 3.41L9')]").click()
   except :  
    close=driver.find_element(By.XPATH,"//button//li-icon[@type='close']//*[name()='svg']//*[name()='path' and contains(@d,'M14 3.41L9')]").click()
    print('None')
   time.sleep(10)

time.sleep(5)
driver.quit()
print('Automation compplete')