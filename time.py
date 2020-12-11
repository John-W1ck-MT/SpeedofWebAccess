import pycurl
import time,os,datetime
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.chrome.options import Options
from io import BytesIO

idpurl='http://mail.decathlon.com'
chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver) # 模拟打开浏览器
# driver.set_window_position(400,300)
driver.set_window_size(400,600)
# driver.get(idpurl)  # 打开网址
js='window.open("http://mail.decathlon.com");'
driver.execute_script(js)
driver.switch_to_window(driver.window_handles[1])
starttime = datetime.datetime.now()
Wait(driver, 60).until(EC.presence_of_element_located((By.ID, "header")))
endtime =datetime.datetime.now()
consumetime=(endtime-starttime)*1000
if consumetime.days < 59000:
# print ("打开"+"网页时间为",consumetime.seconds,"ms")
	with open('idp-speed'+'.txt',"w") as f:
	                    f.write('%d' % consumetime.seconds)
else:
	with open('idp-speed'+'.txt',"w") as f:
	                    f.write('999999')
try:
	elem_user = driver.find_element_by_id("username")  
	elem_user.send_keys("z11jxu")
	time.sleep(1)  
	elem_pwd = driver.find_element_by_id("password")  
	elem_pwd.send_keys("")  #profile密码
	elem_pwd.send_keys(Keys.RETURN)
# time.sleep(5)
# elem_pwd.send_keys(Keys.RETURN)
    # driver.close()
except:
	with open(idpurl+'.txt',"w") as f:
                    f.write('0')

starttime = datetime.datetime.now()
js='window.open("https://support.decathlon.net/saw/sacm?AUTH=SAML&TENANTID=299152652");'
driver.execute_script(js)
driver.switch_to_window(driver.window_handles[2])
Wait(driver, 60).until(EC.presence_of_element_located((By.ID, "mainView")))
endtime =datetime.datetime.now()
consumetime=(endtime-starttime)*1000
if consumetime.days < 59000:
# print ("打开"+"网页时间为",consumetime.seconds,"ms")
	with open('support.decathlon-speed'+'.txt',"w") as f:
	                    f.write('%d' % consumetime.seconds)
else:
	with open('support.decathlon-speed'+'.txt',"w") as f:
	                    f.write('999999')

