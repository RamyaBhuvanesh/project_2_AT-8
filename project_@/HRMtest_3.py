import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
test-3  
    new_employee_under_pim
    1. login
    2. pim
    3. add
    4. add details
    5.enabled radio button
    6.save
    

"""

class Successful_Employee_Login():
    def login_test():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
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

        add_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(3)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chandrasekaran")
        time.sleep(3)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        create_login_details = driver.find_element(By.XPATH, '//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
        time.sleep(2)

        create = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input').send_keys('Ramyachan')
        time.sleep(2)

        password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input').send_keys('Ramya123#')
        time.sleep(2)

        enable = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span').click()
        time.sleep(2)

        confirm_password = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input').send_keys('Ramya123#')
        time.sleep(2)

        save_data = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)
        print("succesfully saved")



get_it = Successful_Employee_Login
get_it.login_test()