import time
from selenium import webdriver
from multiprocessing.connection import wait
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://euronetpakistan.com/careers/current-opportunities/")
driver.maximize_window()

fn=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[2]/div[1]/span/input')
fn.send_keys("SHAHZAIB ANSARI")
time.sleep(5)
print("NAME ENTERED SUCCESSFULLY")


pn=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[2]/div[2]/span/input')
pn.send_keys("WASEEM AHMED ANSARI")
driver.implicitly_wait(5)
print("FATHERS NAME ENTERED SUCCESSFULLY")


ed=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[3]/div[1]/span/input')
ed.send_keys("ansarishahzaib567@gmail.com")
driver.implicitly_wait(5)
print("EMAIL ENTERED SUCCESSFULLY")


nic=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[3]/div[2]/span/input')
nic.send_keys("42101-1234567-1")
driver.implicitly_wait(5)
print("NIC NUMBER ENTERED SUCCESSFULLY")


ph=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[4]/div[1]/span/input')
ph.send_keys("03211234567")
driver.implicitly_wait(5)
print("MOBILE NUMBER ENTERED SUCCESSFULLY")


ps=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[4]/div[2]/span/input')
ps.send_keys("SOFTWARE QUALITY ENGINEERING")
driver.implicitly_wait(5)
print("POSITION ENTERED SUCCESSFULLY")



gn=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/div[5]/div[1]/span/span/span[1]/label/input')
gn.click()

time.sleep(5)


rs=driver.find_element_by_xpath('//*[@id="wpcf7-f376-p366-o1"]/form/p/input[2]')
rs.click()

time.sleep(5)



driver.execute_script("window.open('about:blank', 'tab2');")
driver.switch_to_window('tab2')
driver.get("https://cyber.net.pk/")
print("CYBERNET WEBSITE OPEN A DIFFERENT TAB SUCCESSFULLY")



driver.execute_script("window.open('about:blank','tab3');")
driver.switch_to_window('tab3')
driver.get("http://www.laksol.com/")
print("LAKSON BUSINESS SOLUTION WEBSITE OPEN A DIFFERENT TAB SUCCESSFULLY")




driver.execute_script("window.open( 'https://cyber.net.pk/','about:blank', 'tab2');")
driver.switch_to_window('tab2','driver.window_handles[0]')
driver.get("https://cyber.net.pk/")
print("CYBERNET WEBSITE OPEN A NEW TAB SUCCESSFULLY")




driver.execute_script("window.open( 'http://www.laksol.com/','about:blank', 'tab3');")
driver.switch_to_window('tab3','driver.window_handles[1]')
driver.get("http://www.laksol.com/")
print("CYBERNET WEBSITE OPEN A NEW TAB SUCCESSFULLY")



time.sleep(20)
driver.close()
