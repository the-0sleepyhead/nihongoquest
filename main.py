


service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
URL = "http://www.studykanji.net/kanjilist/"
driver.get("http://www.studykanji.net/kanjilist/")

body = driver.find_element(By.TAG_NAME, "body")
kanji_list = driver.find_elements(By.CLASS_NAME, "kanji-detail")
for kanji in kanji_list:
    print(f"{kanji.text}")
    a = kanji.find_element(By.TAG_NAME, "a") 
    a.click()
    time.sleep(0.1)
    print(driver.find_element(By.ID, "kanji-detail-window").text)
    time.sleep(0.1)
    driver.find_element(By.ID, "kanji-detail-close").click()



driver.quit()

