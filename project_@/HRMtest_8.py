import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.common.keys import Keys

"""


test-8
     1.login (half completed)--->dropdown
     2.dependancy details
     3.add
     4.details
     5.save

"""


class username_1():
    def name_password(self):
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        user_name = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(3)
        print("user name is correct")

        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(5)
        print("password is correct")

        login = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(3)

        add_button = driver.find_element(By.XPATH,  '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chan")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH,'//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        save_data = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)
        print("succesfully saved")

        dependents_contact = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a').click()
        time.sleep(3)

        add_button1 = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--text"][1]').click()
        time.sleep(3)

        name_contact = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('ramya')
        time.sleep(3)

        specify_contact = driver.find_element(By.XPATH, '//label[text()="Relationship"]/following::div[3]/div[1]').click()
        time.sleep(3)

        sp = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Other"]').click()
        time.sleep(3)

        specify = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys("wife")
        time.sleep(3)


        dob = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input').send_keys('2001-10-20')

        enter_save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)




a=username_1()
a.name_password()
