import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GiftCardPin():
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.rslt = []
    
    def findSsgPin(self, id, password):
        session = requests.Session()

        self.driver.get(url=f'https://member.ssg.com/m/member/login.ssg')  # 주소 이동
        inpId = self.driver.find_element(By.ID, "inp_id")
        inpPw = self.driver.find_element(By.ID, "inp_pw")
        loginBtn = self.driver.find_element(By.ID, "loginBtn")

        inpId.clear()
        inpId.send_keys(id)
        inpPw.clear()
        inpPw.send_keys(password)
        loginBtn.click()
        sleep(1)


        for cookie in self.driver.get_cookies():
            session.cookies.update({cookie['name']: cookie['value']})

        response = session.get(f'https://pay.ssg.com/myssg/orderInfo.ssg?viewType=Ssg')
        soup = BeautifulSoup(response.text, 'html.parser')
        # Array.from(document.querySelectorAll('.tx_state')).filter(e=> e.innerText.search('사용가능') == 0).length
        txStates = soup.select('.tx_state')
        availCnt = 0
        # for txState in txStates:
            # availCnt += 1 if txState.getText().find('사용완료') != -1 else 0
        print(availCnt)

        pinSeqEls = soup.select('.codr_btn_ssgcon.codr-tooltip')

        for idx, pinSeqEl in enumerate(pinSeqEls):
            pinSeq = pinSeqEl['data-ord-msg-seq']
            pinResponse = session.get(f'https://pay.ssg.com/m/ecpn/ecpnInfo.ssg?sysDivCd=10&encOrdMsgSeq='+pinSeq)
            pinSoup = BeautifulSoup(pinResponse.text, 'html.parser')
            print(pinSoup.select_one('#barcodeNumber').getText().strip())
            print(pinSoup.select_one('.mnodr_unit_brd').getText().strip())
            print(txStates[idx].getText().replace('\n','').replace('\r','').replace('\t','').replace('\xa0',''))
            print(idx)
            self.rslt.append({'pin' : pinSoup.select_one('#barcodeNumber').getText().strip(),
                              'title' : pinSoup.select_one('.mnodr_unit_brd').getText().strip(),
                              'status' : txStates[idx].getText().replace('\n','').replace('\r','').replace('\t','').replace('\xa0','')})
            # if idx == availCnt -1:
            #     break
            if idx > 19:
                break
        print(self.rslt)
        return self;

    def result(self):
        return self.rslt