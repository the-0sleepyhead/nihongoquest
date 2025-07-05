from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)


# Get kanji from studykanji.net 
def get_kanji():
    URL = "http://www.studykanji.net/kanjilist/"
    driver.get("http://www.studykanji.net/kanjilist/")

    kanji_list = driver.find_elements(By.CLASS_NAME, "kanji-detail")
    for element in kanji_list:
        kanji = element.text
        # Parsing kanji detail
        a = element.find_element(By.TAG_NAME, "a") 
        a.click()
        time.sleep(0.1)
        modal = driver.find_element(By.ID, "kanji-detail-window").text
        time.sleep(0.1)
        driver.find_element(By.ID, "kanji-detail-close").click()

    