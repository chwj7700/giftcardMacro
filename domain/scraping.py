from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# import urllib3

import ssl
import chromedriver_autoinstaller
import undetected_chromedriver as uc
import os
import subprocess
import threading
from time import sleep
import psutil
def createDriver():
    # try:
        # 크롬드라이버 다운로드시 https ssl 인증서 문제 해결
        ssl._create_default_https_context = ssl._create_unverified_context
        path = chromedriver_autoinstaller.install()
        print(chromedriver_autoinstaller.get_chrome_version())
        print(path)

        # 크롬 스크래핑 옵션세팅
        service = ChromeService(ChromeDriverManager().install())  # 크롬 드라이버 최신 버전 설정
        # service = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # options = webdriver.ChromeOptions()
        options = Options()
        # options.add_experimental_option("debuggerAddress", "localhost:9222")
        options.add_experimental_option("detach", True)  # 브라우저 꺼짐 방지 옵션
        # chrome_driver = '/Applications/Google\ Chrome.app/Contents/MacOS/Google'
        # options.add_argument('--window-size=100,100') # 창 크기 설정
        
        # GUI를 제공하지않는 리눅스 서버에서의 환경 설정 (주석 해제시 웹브라우저 실행하지않고 백그라운드에서 스크래핑 처리)
        # options.add_argument('--headless') # 헤더 없애기
        # options.add_argument('--no-sandbox')
        # options.add_argument("--disable-gpu")
        # options.add_argument('--disable-dev-shm-usage') # /deb/shm 디렉토리를 사용하지 않는다는 의미이다. 이 디렉토리는 공유 메모리를 담당\
        
        driver = webdriver.Chrome(service=service, options=options)
        # os.system(terminal_command)

        # terminal_command = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"'
        # def target() :
        #     proc = subprocess.call(terminal_command, shell=True);
        #     # sleep(60)
        #     def destroyed(proc_pid):
        #         process = psutil.Process(proc_pid)
        #         for proc in process.children(recursive=True):
                #     proc.kill()
                # process.kill()
            # destroyed(proc.pid)
        # thread = threading.Thread(target=target)
        # thread.start()
        # thread.join(0)

        # driver = webdriver.Chrome(service=service, options=options)

        # driver = uc.Chrome(service=service, version_main=117, options = options)

        # driver = webdriver.Chrome(service=service, options=options)
        driver.script = driver.execute_script
        # driver.get("https://m.cultureland.co.kr/mmb/loginMain.do")
        
    # except:
    #     driver.close()
    #     return createDriver()
        return driver

# driver = createDriver()
# driver.get("https://m.cultureland.co.kr/mmb/loginMain.do")
