from selenium import webdriver
import time

path = "C:/Users/b/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://zzzscore.com/1to50/")

for i in range (1, 51): # 눌러야하는 버튼 50개 

        buttons = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]') # 모든 버튼을 xpath를 이용해 가져오기

        for value in buttons:
          if value.text == str(i): # div가 i와 같을 때 클릭하기
            value.click()
            print(str(i) + " 클릭")
            break
