# selenium으로부터 webdriver 모듈을 불러온다.

# 웹 브라우저와 연동을 위해
from selenium import webdriver
# Chrome 객체의 인자로 넣기 위해
from selenium.webdriver.chrome.service import Service
# 사용 중인 Chrome version과의 싱크를 맞추기 위해
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

# Selenium을 활용하여 조작하기 위해서 driver 객체 생성
# 위 명령을 통해 웹 브라우저를 실행하고 파이썬과 연동할 수 있음
# .get(url)을 활용해 요청을 보낼 수 있음

# 브라우저를 안 띄우는 headless 옵션
options = Options()
options.add_argument("headless")
options.add_argument("disable-gpu")

url = "https://www.hongik.ac.kr/kr/education/notice-undergrad.do?mode=list&srCategoryId=&srStartDt=&srEndDt=&srSearchKey=article_title&srSearchVal="

with webdriver.Chrome(service=Service(ChromeDriverManager().install())) as driver:
    driver.get(url)
    
    # 셀레니움 동작작
    for page in range(4, 6):

        # 공지사항 리스트 출력
        for x in range(1, 11):
            list_xpath = f'//*[@id="cms-content"]/div/div/div[2]/div[2]/table/tbody/tr[{x}]/td[2]/div/a'
            source = driver.find_element(By.XPATH, list_xpath)
            print(source.text)
            print(source.get_attribute("href"))
        # 페이지 이동    
        page_xpath = f'//*[@id="cms-content"]/div/div/div[2]/div[3]/div/ul/li[{page}]/a'
        clickable = driver.find_element(By.XPATH, page_xpath)
        ActionChains(driver) \
            .click(clickable) \
            .perform()
        print(f'페이지 : {page-3} \n')
        
        


    
    






