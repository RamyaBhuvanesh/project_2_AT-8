import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


"""
test-5 
     1. login
     2. fill out the personal details
     3. save
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
        login_button_xpath = '//button[@type="submit"]'
        login = driver.find_element(By.XPATH, login_button_xpath)
        login.click()
        time.sleep(5)

def test_orangeHRM(setUP):

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(3)

        add_button = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chan")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        # photo_xpath = '//button[@class="oxd-icon-button employee-image-action"]'
        # photo = driver.find_element(By.XPATH, photo_xpath)
        # photo.send_keys("C:/Users/ramya/OneDrive/Pictures/Screenshots")
        # photo.click()
        # time.sleep(2)

        create_login_details = driver.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
        time.sleep(2)

        create = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys('Ramyab')
        time.sleep(2)

        password = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys('Ramya123@')
        time.sleep(2)

        confirm_password = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys('Ramya123@')
        time.sleep(2)

        save_data = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)

        print("succesfully saved")

        open = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a').click()
        time.sleep(4)

        # #xpath for Nickname
        # Nickname_xpath='//label[text()="Nickname"]/following::div[1]/input'
        # Nickname=driver.find_element(By.XPATH,Nickname_xpath).send_keys("puppy")
        # time.sleep(4)

        OtherID = driver.find_element(By.XPATH, '//label[text()="Other Id"]/following::div[1]/input').send_keys("568790")
        time.sleep(4)

        # xpath for DL
        # DL_xpath='//label[text()="Driver's License Number"]/following::div[1]/input'
        # DL=driver.find_element(By.XPATH,DL_xpath).send_keys("158615")
        # time.sleep(4)

        date = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input').send_keys("2009-10-09")
        time.sleep(4)

        SSN = driver.find_element(By.XPATH, '//label[text()="SSN Number"]/following::div[1]/input').send_keys("9876")
        time.sleep(4)

        SIN = driver.find_element(By.XPATH, '//label[text()="SIN Number"]/following::div[1]/input').send_keys("567867")
        time.sleep(3)

        # xpath for Nationality
        #  Nationality_xpath=''
        # Nationality=driver.find_element(By.XPATH,Nationality_xpath).send_keys("Indian")
        #  time.sleep(3)
        #   na_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
        #   na = driver.find_element(By.XPATH, na_xpath)
        #   na.send_keys("India")
        #   na.click()
        #   time.sleep(4)
        #
        #   #xpath for Martial status
        #   Martial_xpath='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
        #   Martial=driver.find_element(By.XPATH,Martial_xpath).send_keys("Married")
        #   time.sleep(2)

        DOB = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input').send_keys("1999-05-20")
        time.sleep(3)

        Gender = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span').click()
        time.sleep(3)

        # blood_group_xpath ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
        # blood_group = driver.find_element(By.XPATH, blood_group_xpath).send_keys('B+')
        # time.sleep(3)

        Save = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button').click()
        time.sleep(5)



def teardown_():

         driver.close()
