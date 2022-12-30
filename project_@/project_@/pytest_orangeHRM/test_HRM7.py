import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
test-7
     1.login
     2.emergency contact details
     3.add
     4.details
     5.save
     
"""
@pytest.fixture()
def setUP():
        global driver
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        driver.maximize_window()

        user_name_xpath = '//input[@name="username"]'
        user_name = driver.find_element(By.XPATH, user_name_xpath).send_keys("Admin")
        time.sleep(3)
        print("user name is correct")

        password_credential = '//input[@name="password"]'
        password = driver.find_element(By.XPATH, password_credential).send_keys("admin123")
        time.sleep(5)
        print("password is correct")

        login = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

def test_orangeHRM(setUP):
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

        save_data = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)
        print("succesfully saved")

        emergency_contact = driver.find_element(By.XPATH ,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a').click()
        time.sleep(3)

        add_button1 = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--text"][1]').click()
        time.sleep(3)

        name_contact = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys('ramya')
        time.sleep(3)

        name_contact = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys('Married')
        time.sleep(3)

        enter_telephone = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input').send_keys('044 20876876')
        time.sleep(3)

        enter_mobile = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input').send_keys('9876543214')
        time.sleep(3)

        enter_work = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys('8987543245')
        time.sleep(3)

        enter_save = driver.find_element(By.XPATH, '//button[@type="submit"][1]').click()
        time.sleep(3)




def teardown():
        driver.close()
        driver.quite()