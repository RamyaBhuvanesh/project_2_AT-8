import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from self import self
import pytest

"""
test-13
     1.login
     2.Tax Exemptions details
     3.save
     3.direct deposit details
     4.fill details
     5.save

"""
@pytest.fixture()
def setUP():
        global driver
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)

        # xpath to username
        username = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(3)

        # xpath to password
        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(3)

        # xpath to login button
        submit = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(5)

def test_orangeHRM(setUP):
        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(2)

        add_button = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chan")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        save_data = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(7)
        print("succesfully saved")

        TaxExemptions = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').click()
        time.sleep(3)

        Status = driver.find_element(By.XPATH, '//label[text()="Status"]/following::div[4]').click()
        time.sleep(3)

        Status_1 = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Married"]').click()
        time.sleep(3)

        Exemptions = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input').send_keys("9")
        time.sleep(3)

        state = driver.find_element(By.XPATH, '//label[text()="State"]/following::div[4]').click()
        time.sleep(3)

        state = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="American Samoa"]').click()
        time.sleep(3)

        Exemptions = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input').send_keys("7")
        time.sleep(3)

        Unemployment_State = driver.find_element(By.XPATH, '//label[text()="Unemployment State"]/following::div[4]').click()
        time.sleep(3)

        Unemployment_State_1 = driver.find_element(By.XPATH, '  //div[@role="listbox"]//span[text()="American Samoa"]').click()
        time.sleep(3)

        WorkState = driver.find_element(By.XPATH, '//label[text()="Work State"]/following::div[4]').click()
        time.sleep(3)

        WorkState_1 = driver.find_element(By.XPATH, ' //div[@role="listbox"]//span[text()="Armed Forces Canada"]').click()
        time.sleep(3)

        enter_save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)

def teardown():
        driver.close()
        driver.quite()




