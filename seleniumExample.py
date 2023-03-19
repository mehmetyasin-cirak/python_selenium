from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep
from selenium.webdriver.common.by import By

edgeDriver = webdriver.Chrome(EdgeChromiumDriverManager().install())
edgeDriver.maximize_window()
edgeDriver.get("https://www.google.com/")
sleep(5)
input = edgeDriver.find_element(By.NAME, "q")
input.send_keys("kodlamaio")
searchButton = edgeDriver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResult = edgeDriver.find_element(By.XPATH, "//*[@id='rso']/div[1]/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = edgeDriver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlamaio sitesinde şu anda {len(listOfCourses)} adet kurs var.")
# sleep(10)
while True:
    continue
