import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self
from selenium.webdriver.common.keys import Keys

"""


test-6 
     1.login
     2. contact details
     3. save
     

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

        login = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(3)

        add_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chan")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        save_data_xpath = '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
        save_data = driver.find_element(By.XPATH, save_data_xpath).click()
        time.sleep(7)

        print("succesfully saved")

        enter_contact = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').click()
        time.sleep(3)

        enter_adressS1 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('br apartment')
        time.sleep(3)

        enter_adressS2 = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('newton road')
        time.sleep(3)

        enter_city = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input').send_keys('chennai')
        time.sleep(3)

        enter_state = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input').send_keys('Tamilnadu')
        time.sleep(3)

        enter_postal_code = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys('600093')
        time.sleep(3)

        # country_xpath = '//div[ @class="oxd-select-text oxd-select-text--active"]'
        # enter_country = driver.find_element(By.XPATH, country_xpath)
        # enter_country.send_keys('India')
        # time.sleep(3)

        enter_telephone = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys('044 20876876')
        time.sleep(3)

        enter_mobile = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys('9876543214')
        time.sleep(3)

        enter_work = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys('8987543245')
        time.sleep(3)

        enter_email = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input').send_keys("sample@gmail.com")
        time.sleep(3)

        enter_save = driver.find_element(By.XPATH, '//button[ @type="submit"]').click()
        time.sleep(3)









a=username_1()
a.name_password()
