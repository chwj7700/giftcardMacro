# Request body를 선언할 때 Pydantic 모델을 사용
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import support as support
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class HmCharge():

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.rslt = []

    def login(self, id, password):
        self.driver.get(url=f'https://www.happymoney.co.kr/svc/login/login.hm') # 주소 이동

        self.driver.script("document.querySelector('#memberId').value='"+id+"'")
        self.driver.script("mtk.onKeyboard(document.querySelector('#memberPwd'))")

        self.lowerText = self.driver.script("return mtk.talkBackLowerText")
        self.upperText = self.driver.script("return mtk.talkBackLowerText.map(e=> String(e).toUpperCase())")
        self.specialText = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
                    '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '/', '?', ',', '<', '.', '>', '\'', '\"', '+', '-', '*', '/']
        self.dkis = self.driver.script("return transkey['memberPwd'].dki")

        for dki in self.dkis:
            self.lowerText.insert(int(dki), ' ')
            self.upperText.insert(int(dki), ' ')
            self.specialText.insert(int(dki), ' ')

        for idx, p in enumerate(password):
            if p in self.lowerText:
                self.driver.script("mtk.now.setKeyType('lower')")
                idx = self.lowerText.index(p)
            elif p in self.upperText:
                self.driver.script("mtk.now.setKeyType('upper')")
                idx = self.upperText.index(p)
            elif p in self.specialText:
                self.driver.script("mtk.now.setKeyType('special')")
                idx = self.specialText.index(p)

            self.driver.script("mtk.now.hidden.value += transkey_delimiter + mtk.getEncData('"+str(idx)+"')")
            self.driver.script("document.querySelector('#memberPwd').value='" + p + "'")
        self.driver.script("mtk.done(document.querySelector('#memberPwd'))")
        sleep(1)
        self.driver.script("login_Action.sendLogin()")

        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'service_1'))) # service_1이라는 class를 가진 element를 기다린다 (최대 3초)
        return self


    def charge(self, pins):
        self.driver.get(url=f'https://www.happymoney.co.kr/svc/cash/giftCardCharge.hm')

        self.inpTxts = self.driver.script("return document.querySelectorAll('.inpTxt')")

        for idx, inpTxt in enumerate(self.inpTxts):
            if idx >= len(pins) : break

            self.pin = pins[idx]
            self.inpTxtId = inpTxt.get_attribute('id')

            if self.driver.script("return typeof transkey['"+self.inpTxtId+"'] !== 'undefined'"):
                self.driver.script("mtk.onKeyboard(document.querySelector('#" + self.inpTxtId + "'))")
                for p in self.pin:
                    idx = str(self.driver.script("return transkey['"+self.inpTxtId+"'].talkBackNumberText.indexOf('" + p + "')"))
                    self.encrypted = self.driver.script("return mtk.getEncData('"+idx+"')")
                    self.delimiter = self.driver.script("return transkey_delimiter")
                    self.driver.script("mtk.now.hidden.value += '" + self.delimiter + self.encrypted + "'")
            self.driver.script("document.querySelector('#" + self.inpTxtId + "').value= '" + self.pin + "'")
        self.driver.script("mtk.done()")
        self.driver.script("mainMyBox_Action.myBoxClose()")

        # self.driver.find_element(By.ID, 'addTen').click()
        # self.driver.find_element(By.CLASS_NAME, 'btnCharge').click()
        self.driver.script("document.querySelector('#addTen').click()")
        self.driver.script("document.querySelector('.btnCharge').click()")
       
        WebDriverWait(self.driver, 3).until(EC.alert_is_present())
        self.alert = self.driver.switch_to.alert
        self.alert.accept()

        sleep(1)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'chargeDatail')))
        
        return self
    
    def result(self):
        self.chargeResults = self.driver.script("return Array.prototype.slice.call(document.querySelectorAll('tr')).map(e => e.innerText)")
        self.chargeResults.pop(0)
        
        for chargeResult in self.chargeResults:
            rowData = chargeResult.split('\t')
            self.rslt.append({'number': rowData[0],
                                'orderNumber': rowData[1],\
                                'pin': rowData[2] + '_' + rowData[3],\
                                'chargeResult': rowData[4],\
                                'amt': rowData[5]})
        return self.rslt
