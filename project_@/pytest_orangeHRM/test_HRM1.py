import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""

test-1 
   login
1. search
2. admin
3. search
     admin
     PIM
     Leave
     Time
     Recruitment
     My Info
     Performance
     Dashboard
     Dictory
     Maintenance
     Buzz

"""



@pytest.fixture()
def setUP():
        global driver
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(3)


def test_orangeHRM(setUP):
    # xpath to username
    username = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
    time.sleep(3)

    # xpath to password
    password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
    time.sleep(3)

    # xpath to login button
    submit = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
    time.sleep(5)

    # xpath to search box
    search_box = driver.find_element(By.XPATH, '//input[@class="oxd-input oxd-input--active"]')
    time.sleep(3)

    # import list method here
    search_list = ['Admin', 'Pim', 'Leave', 'Time', 'Recruitment', 'My info', 'Performance', 'Dashboard',
                   'Directory', 'Maintenance', 'Buzz']

    # Searching in uppercase
    for a in search_list:
        search_box.send_keys(a.upper())
        print(a.upper())
        time.sleep(2)

        # clearing the exiting text
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.BACKSPACE)

        # Searching in lower case
    for a in search_list:
        search_box.send_keys(a.lower())
        print(a.lower())
        time.sleep(2)

        # clearing the exiting text
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.BACKSPACE)
        time.sleep(3)

def teardown_class():

            driver.close()

