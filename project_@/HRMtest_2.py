from selenium import webdriver
from selenium.webdriver.common.by import By
import time

"""
 
 test-2
   drop_down
 1. admin
 2. user management
          users(op)
 3. system users
       cond:1 admin
              enabled
       cond:2 ESS
              disabled
              search
"""

class username_1():
    def name_password(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)

        username=driver.find_element(By.XPATH,'//input[@name="username"]').send_keys("Admin")
        time.sleep(3)

        password=driver.find_element(By.XPATH,'//input[@name="password"]').send_keys("admin123")
        time.sleep(3)

        submit=driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)

        admin=driver.find_element(By.XPATH,'//a[@href="/web/index.php/admin/viewAdminModule"]').click()
        time.sleep(4)

        usermanagement=driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]').click()
        time.sleep(4)

        users=driver.find_element(By.XPATH,'//a[@href="#"]').click()
        time.sleep(3)

        userrole=driver.find_element(By.XPATH,'//label[text()="User Role"]/following::div[3]').click()
        time.sleep(3)

        drpadmin=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Admin"]').click()
        time.sleep(3)

        status=driver.find_element(By.XPATH,'//label[text()="Status"]/following::div[3]').click()
        time.sleep(3)

        drpenabled=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Enabled"]').click()
        time.sleep(3)

        userrole = driver.find_element(By.XPATH, '//label[text()="User Role"]/following::div[3]').click()
        time.sleep(3)

        ESS=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="ESS"]').click()
        time.sleep(3)
        status = driver.find_element(By.XPATH, '//label[text()="Status"]/following::div[3]').click()
        time.sleep(3)

        drpdisabled=driver.find_element(By.XPATH,'//div[@role="listbox"]//span[text()="Disabled"]').click()
        time.sleep(3)

a=username_1()
a.name_password()