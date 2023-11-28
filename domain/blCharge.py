import requests
from bs4 import BeautifulSoup
from scraping import createDriver
from selenium.webdriver.common.by import By
from time import sleep

driver = createDriver()
driver.get(url=f'https://www.booknlife.com/auth/login/')  # 주소 이동

sleep(10)
capchar = driver.find_element(By.CSS_SELECTOR, "#__next > div.Layout_wrapper__PwD36 > div.LoginView_login_container__h2V9E > div > div > div.LoginView_login_inp__5wveu > div > div.LoginView_login_btn__ee85v > div > div > div > div > div > div > iframe")
sleep(3)
capchar.click()
inpId = driver.find_element(By.CSS_SELECTOR, '#__next > div.Layout_wrapper__PwD36 > div.LoginView_login_container__h2V9E > div > div > div.LoginView_login_inp__5wveu > div > div.LoginView_inp_box__1SbWI > div.LoginView_in_inp__CRWj5 > span:nth-child(2) > input[type=text]')
sleep(3)
inpPw = driver.find_element(By.CSS_SELECTOR, "#__next > div.Layout_wrapper__PwD36 > div.LoginView_login_container__h2V9E > div > div > div.LoginView_login_inp__5wveu > div > div.LoginView_inp_box__1SbWI > div.LoginView_in_pw___ZvCg > span:nth-child(2) > input[type=password]")
sleep(3)
inpId.send_keys('')
inpPw.send_keys('')
