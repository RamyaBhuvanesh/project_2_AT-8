import time
from selenium import webdriver
from selenium.webdriver.common.by import By

"""
test-4 
    1.login
    2.print all the heading
    
	Personal Details
	Contact Details
	Emergency Contacts
	Dependents
	Immigration
	Job
	Salary
	Tax Exemptions
	Report-to
	Qualifications
	Memberships
	

"""

class Successful_Employee_Login():
    def login_test():
        driver = webdriver.Chrome()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.maximize_window()
        time.sleep(2)

        user_name = driver.find_element(By.XPATH, '//input[@name="username"]').send_keys("Admin")
        time.sleep(2)
        print("user name is correct")

        password = driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("admin123")
        time.sleep(3)
        print("password is correct")

        login = driver.find_element(By.XPATH,'//button[@type="submit"]').click()
        time.sleep(5)

        enter_pim = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]').click()
        time.sleep(2)

        add_button = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary"]').click()
        time.sleep(2)

        first_name = driver.find_element(By.XPATH, '//input[@name="firstName"]').send_keys("Ramya")
        time.sleep(2)

        middle_name = driver.find_element(By.XPATH, '//input[@name="middleName"]').send_keys("Chandrasekaran")
        time.sleep(2)

        last_name = driver.find_element(By.XPATH, '//input[@name="lastName"]').send_keys("B")
        time.sleep(2)

        save_data = driver.find_element(By.XPATH, '//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]').click()
        time.sleep(7)

        open = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a').click()
        time.sleep(3)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH,  '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[10]/a').accessible_name)
        time.sleep(2)

        print(driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[11]/a').accessible_name)
        time.sleep(3)
        print("succesfully printed")




get_it = Successful_Employee_Login
get_it.login_test()