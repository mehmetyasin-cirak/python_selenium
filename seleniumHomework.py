from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from selenium.webdriver.common.by import By

edgeDriver = webdriver.ChromiumEdge(EdgeChromiumDriverManager().install())
edgeDriver.get("https://www.saucedemo.com/")


class Test_Sauce:

    def check_username_password(self):
        inputUsername = edgeDriver.find_element(By.ID, "user-name")
        inputPassword = edgeDriver.find_element(By.ID, "password")
        loginButton = edgeDriver.find_element(By.ID, "login-button")
        inputUsername.send_keys(" ")
        inputPassword.send_keys(" ")
        loginButton.click()

        if inputPassword.send_keys(" ") and inputPassword.send_keys(" "):
            errorButton = edgeDriver.find_element(By.XPATH,
                                                  "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3/button")
            errorButton.click()
            errorMessage = edgeDriver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
            print(errorMessage.text)
            sleep(1)

        elif inputPassword.send_keys():
            print("Epic sadface: Password is required")

    def login_sauce(self):
        inputUsername = edgeDriver.find_element(By.ID, "user-name")
        inputPassword = edgeDriver.find_element(By.ID, "password")
        loginButton = edgeDriver.find_element(By.ID, "login-button")
        inputUsername.send_keys("locked_out_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        if inputUsername.send_keys() == "locked_out_user" and inputPassword == "secret_sauce":
            print("Epic sadface: Sorry, this user has been locked out.")

    def succes_login(self):
        inputUsername = edgeDriver.find_element(By.ID, "user-name")
        inputPassword = edgeDriver.find_element(By.ID, "password")
        loginButton = edgeDriver.find_element(By.ID, "login-button")
        inputUsername.send_keys("standart_user")
        inputPassword.send_keys("secret_sauce")
        loginButton.click()
        edgeDriver.get("/inventory.html")


test_sauce = Test_Sauce()
# test_sauce.check_username_password()
# test_sauce.login_sauce()
test_sauce.succes_login()
sleep(100)
