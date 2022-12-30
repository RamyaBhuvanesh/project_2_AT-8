import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from self import self

"""
test-12
     1.login
     2.salary details
     3.save
     3.direct deposit details
     4.fill details
     5.save
"""
class Successful_Employee_Login():
    def login_test():
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

        save_data = driver.find_element(By.XPATH,'//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)
        print("succesfully saved")

        salary = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').click()
        time.sleep(3)

        add_button1 = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button').click()
        time.sleep(3)

        Salary_Component = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input').send_keys("bank")
        time.sleep(3)

        Pay_Grade = driver.find_element(By.XPATH, '//label[text()="Pay Grade"]/following::div[4]').click()
        time.sleep(3)

        Pay_Grade_1= driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Grade 1"]').click()
        time.sleep(3)

        PayFrequency = driver.find_element(By.XPATH, '//label[text()="Pay Frequency"]/following::div[4]').click()
        time.sleep(3)

        PayFrequency_1 = driver.find_element(By.XPATH, '//div[@role="listbox"]//span[text()="Hourly"] ').click()
        time.sleep(3)

        currency = driver.find_element(By.XPATH, '//label[text()="Currency"]/following::div[4]').click()
        time.sleep(3)

        currency_1 = driver.find_element(By.XPATH, ' //div[@role="listbox"]//span[text()="United States Dollar"]').click()
        time.sleep(3)

        Amount = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input').send_keys('59000')
        time.sleep(3)

        Comments = driver.find_element(By.XPATH, '//textarea[@class="oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical"]').send_keys("succesfully updated")
        time.sleep(3)

        enter_save = driver.find_element(By.XPATH, '//button[@type="submit"]').click()
        time.sleep(2)


get_it = Successful_Employee_Login
get_it.login_test()
