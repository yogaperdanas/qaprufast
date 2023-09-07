from appium import webdriver 
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy


import time


desired_caps = {}

desired_caps['platformName'] = 'android'
desired_caps['deviceName'] ='Infinix HOT 11NFC'
desired_caps['appPackage'] = 'id.co.prudential.prufastapp.uat'
desired_caps['appActivity'] = 'id.co.prudential.prufastapp.uat.MainActivity'





driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

driver.implicitly_wait(1000)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@index='6']")
element.click()
time.sleep(1)

driver.implicitly_wait(320)
element = driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[260,822][821,952]']")
element.send_keys('Agen00000727')
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[260,1108][767,1237]']")
element.send_keys('Password09')
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[260,1364][821,1499]']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.Button[@bounds='[764,1203][969,1365]']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[122,1847][958,1982]']")
element.click()
time.sleep(1)

driver.implicitly_wait(320)
element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[553,351][764,597]']")
element.click() #esqs spaj
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[852,2088][1020,2208]']")
element.click() #tanda + di esqs spaj
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[480,2064][600,2184]']")
element.click() #tanda + ketika di klik +
time.sleep(1)

#tampilan 1
element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[561,1115][1044,1520]']")
element.click() 
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[36,2106][1044,2208]']")
element.click() 
time.sleep(1)

#tampilan 2
element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[36,1706][519,2045]']")
element.click() 
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[36,2106][1044,2208]']")
element.click() 
time.sleep(1)

#tampilan 3
element = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Tidak']")
element.click() 
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Tradisional']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Syariah']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[36,1787][519,2060]']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@bounds='[36,2106][1044,2208]']")
element.click()
time.sleep(1)

#halaman 4


element = driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[69,899][975,1021]']")
element.click()
element.send_keys('COBAA AUTOMATION')
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[476,1096][975,1218]']")
element.click()
element.send_keys('81542411293')
time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.EditText[@bounds='[69,1311][897,1370]']")
element.click()
time.sleep(1)

#jika menikah 
element = driver.find_element(By.XPATH, "//android.view.ViewGroup[@elementId='00000000-0000-1243-ffff-ffff0000034d']")
element.click()
time.sleep(1)

#tgl lahir
element = driver.find_element(By.XPATH, "//android.widget.TextView[@text='Tanggal Lahir']")
element.click()
time.sleep(1)

element = driver.find_element(By.XPATH, "//android:id/button1")
element.click()

time.sleep(1)

element = driver.find_element(By.XPATH, "//android.widget.Button[@text='Tanggal Lahir']")
element.click()
time.sleep(1)

