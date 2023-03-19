from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from selenium.webdriver.common.by import By


class Test_Sauce:
    def test_invalid_login(self):
        edgeDriver = webdriver.Chrome(EdgeChromiumDriverManager().install())
        edgeDriver.maximize_window()
        edgeDriver.get("https://www.saucedemo.com/")
        sleep(5)
        # en fazla 5 saniye olacak şekilde user-name id'li elementin görünmesini bekle
        usernameInput = edgeDriver.find_element(By.ID, "user-name")
        passwordInput = edgeDriver.find_element(By.ID, "password")
        sleep(2)
        usernameInput.send_keys("1")
        passwordInput.send_keys("1")
        sleep(2)
        loginBtn = edgeDriver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = edgeDriver.find_element(By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username and password do not match any user in this service"
        print(f"TEST SONUCU: {testResult}")


testClass = Test_Sauce()
testClass.test_invalid_login()
