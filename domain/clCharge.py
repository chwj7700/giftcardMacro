# Request body를 선언할 때 Pydantic 모델을 사용
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import support as support
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytesseract import *
from time import sleep
import requests
from io import BytesIO
from PIL import Image
import numpy as np

import random

class ClCharge():

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.rslt = []

    def getDkis(self):
        # transkeyUuid = self.driver.script("return mtk.transkeyUuid")
        # allocationIndex = self.driver.script("return transkey.passwd.allocationIndex")
        # keyIndex = self.driver.script("return transkey.passwd.keyIndex")
        # params = {
        #     'op': 'getKey',
        #     'name': 'passwd',
        #     'keyType': 'lower',
        #     'keyboardType': 'qwertyMobile',
        #     'fieldType': 'password',
        #     'inputName': 'passwd',
        #     'parentKeyboard': 'false',
        #     'transkeyUuid': transkeyUuid,
        #     'exE2E': 'false',
        #     'TK_requestToken': '0',
        #     'allocationIndex': allocationIndex,
        #     'keyIndex': keyIndex
        # }
        url = self.driver.script("return document.querySelector('.dv_transkey_div2_2').style.backgroundImage.split('\"')[1]")
        print(url)
        response = requests.get(url)

        # Img open
        img = Image.open(BytesIO(response.content))
        img = img.resize((1100, 500))

        left, top, right, bottom = 30, 30, 70, 70
        result = []
        for i in range(0, 4):
            for j in range(0, 11):
                img_cropped = img.crop((left + (j*100), top + (i*100), right + (j*100), bottom + (i*100)))
                image_nparray = np.array(img_cropped).flatten().tolist()
                result.append(any(image_nparray))

        dkis = [i for i in range(len(result)) if result[i] == False]
        print(dkis)
        return dkis

    def login(self, id, password):
        # self.driver.get('https://accounts.hcaptcha.com/verify_email/5835d231-81a9-4e50-b047-b1bebb701306')
        # sleep(5)
        # self.driver.add_cookie({
        #     'name' : 'hc_accessibility',
        #     'value' : 'CRZmjeirqf0EbZriAMQSOxYupwGQFpXHexW9c5kDlZ0aiHRBrtZo2XRREKayLQVprys6w7zMu/CJn6P5nfuKCIfmpAeet30JhPXeE52EiA1Ta6z1z6hBkwLlhwnM0Ah2uWrKcAbsiN5lZuyyMWbso0bAKveAUHq62Q6YkxFan57uijxCE3+1XuSGKGpxVz39Gz4maXa3NFZWz9pe5+2jmFMez/4yOCwaMu0vwKPmWVROwn4yPktfAtr1qENEgBeAOsYIFic27EX/NJE/rhIuwLMxG2BEWJxRE335ePQE4/ppZPkoYqHx9bfigC6CJyWNRpaxD1OK/MU0v0ag6Nwr+61ueE7PykMFTLV13tdXdL/ELxikB19AtTItoWCKwr9s+gksWMKKgGiraCnJUM7rZP8AS6uKuTxGIr84LsM+4a2zJDvCB2LnGmZ6ucdt2RMRFOtUKMEMvMyPpnMpzTbkH1IX0SRJemaZD2JAqSY3NjPeO4dUPC/vKb0opJAyQfejizA8UcWOBdzdEmvY5RcaAKVe4+J9Pal7++A9dpADjZrhCiRdwvY+D7S6FrDCAjI4VuGsPIQ3E/IeFkPdzkEB1462bb6TNlaH93rV+TnhAG2wINoqPVwZ4Hhj7+9QJTvjEFTiE7khVHnzZ7gUm1deyPe94IvgS1gnaP6pOK/FKmnKsn7JN7LE0ixDghReXXoeG0EE2MbMmDip5cfuReekBoq5WQPL0bqMUrhYkr/KiJp8EoKfw3EzTGVv6xPCjgZNMHBxTS8DUHtCH74pSLWUB2WAAQPE67dsqEW/rpPbvK+rJiwLf7JvDo0osItHAl4d7QBsZ3lZecmHzuq/25LYM/nZun7LU4sD7bWeh1IqOk2C19b69aVF0s8UXyVeziDStHh4Z5sP7TVA4IR6o1T1FrF1TSADNqDCa1mSyIBUAKCBk0D6VCN0mwB0U2ogyXi31rFhg26m5u9Vv9PLeYxOZ2/XQOBrxrQbjkitgPJdQb5Zts+2gGNVdyO9wAQvnzF90Vi5Ap0f6ExSNiTtMOpWO+xEFzRa12Mq4RoFoVs3822gcknPWy3uo132IUl5Wa8hD+LNylM2HCf6jBl0Z+BzjzngYhBy9qYvVAeiQ6VsMBrYn20D'
        # })

        # self.driver.get('https://newassests.hcaptcha.com/')
        # # sleep(5)
        # self.driver.add_cookie({
        #     'name' : 'hc_accessibility',
        #     'value' : 'CRZmjeirqf0EbZriAMQSOxYupwGQFpXHexW9c5kDlZ0aiHRBrtZo2XRREKayLQVprys6w7zMu/CJn6P5nfuKCIfmpAeet30JhPXeE52EiA1Ta6z1z6hBkwLlhwnM0Ah2uWrKcAbsiN5lZuyyMWbso0bAKveAUHq62Q6YkxFan57uijxCE3+1XuSGKGpxVz39Gz4maXa3NFZWz9pe5+2jmFMez/4yOCwaMu0vwKPmWVROwn4yPktfAtr1qENEgBeAOsYIFic27EX/NJE/rhIuwLMxG2BEWJxRE335ePQE4/ppZPkoYqHx9bfigC6CJyWNRpaxD1OK/MU0v0ag6Nwr+61ueE7PykMFTLV13tdXdL/ELxikB19AtTItoWCKwr9s+gksWMKKgGiraCnJUM7rZP8AS6uKuTxGIr84LsM+4a2zJDvCB2LnGmZ6ucdt2RMRFOtUKMEMvMyPpnMpzTbkH1IX0SRJemaZD2JAqSY3NjPeO4dUPC/vKb0opJAyQfejizA8UcWOBdzdEmvY5RcaAKVe4+J9Pal7++A9dpADjZrhCiRdwvY+D7S6FrDCAjI4VuGsPIQ3E/IeFkPdzkEB1462bb6TNlaH93rV+TnhAG2wINoqPVwZ4Hhj7+9QJTvjEFTiE7khVHnzZ7gUm1deyPe94IvgS1gnaP6pOK/FKmnKsn7JN7LE0ixDghReXXoeG0EE2MbMmDip5cfuReekBoq5WQPL0bqMUrhYkr/KiJp8EoKfw3EzTGVv6xPCjgZNMHBxTS8DUHtCH74pSLWUB2WAAQPE67dsqEW/rpPbvK+rJiwLf7JvDo0osItHAl4d7QBsZ3lZecmHzuq/25LYM/nZun7LU4sD7bWeh1IqOk2C19b69aVF0s8UXyVeziDStHh4Z5sP7TVA4IR6o1T1FrF1TSADNqDCa1mSyIBUAKCBk0D6VCN0mwB0U2ogyXi31rFhg26m5u9Vv9PLeYxOZ2/XQOBrxrQbjkitgPJdQb5Zts+2gGNVdyO9wAQvnzF90Vi5Ap0f6ExSNiTtMOpWO+xEFzRa12Mq4RoFoVs3822gcknPWy3uo132IUl5Wa8hD+LNylM2HCf6jBl0Z+BzjzngYhBy9qYvVAeiQ6VsMBrYn20D'
        # })


        self.driver.get(url='https://m.cultureland.co.kr/mmb/loginMain.do')

        self.driver.script("document.querySelector('#txtUserId').value='"+id+"'")
        self.driver.script("mtk.onKeyboard(document.querySelector('#passwd'))")

        self.lowerText = self.driver.script("return mtk.talkBackLowerText")
        self.upperText = self.driver.script("return mtk.talkBackLowerText.map(e=> String(e).toUpperCase())")
        self.specialText = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
                    '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '\\', '|', ';', ':', '/', '?', ',', '<', '.', '>', '\'', '\"', '+', '-', '*', '/']
        self.dkis = self.getDkis()

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
            # sleep(random.random())
            self.driver.script("mtk.now.hidden.value += transkey_delimiter + mtk.getEncData('"+str(idx)+"')")
            self.driver.script("document.querySelector('#passwd').value+='" + p + "'")
        self.driver.script("mtk.done(document.querySelector('#passwd'))")
        self.driver.script("document.querySelector('#btnLogin').click()")
        sleep(10)
        # self.driver.switch_to.frame(2)
        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'service_1')))
        return self


    def charge(self, pins):
        self.driver.get(url=f'https://m.cultureland.co.kr/csh/cshGiftCard.do')
        self.driver.script("document.querySelector('#addForm').click()")

        self.inpTxts = self.driver.script("return document.querySelectorAll('.scr,.scrPwd')")
        print(self.inpTxts)
        for idx, inpTxt in enumerate(self.inpTxts):
            if idx >= len(pins) : break

            self.pin = pins[idx]
            self.inpTxtId = inpTxt.get_attribute('id')
            if(idx % 4 == 3):
                self.driver.script("mtk.onKeyboard(document.querySelector('#"+self.inpTxtId+"'))")
                imgUrl = self.driver.script("return document.querySelector('.dv_transkey_div2_2').style.backgroundImage.replace(/^url\(['\"](.+)['\"]\)/, '$1')")

                response = requests.get(imgUrl)

                # Img open
                img = Image.open(BytesIO(response.content))
                img = img.resize((500,455))
                # img.show()
                left, top, right, bottom = 0, 0, 125, 112
                keypad = []
                for i in range(0,3):
                    for j in range(0,4):
                        img_cropped = img.crop((left + (j*125), top + (i*112), right + (j*125), bottom + (i*112)))
                        # img_cropped.show()
                        # image_nparray = np.array(img_cropped).flatten().tolist()
                        text = pytesseract.image_to_string(img_cropped, config='--psm 6')
                        keypad.append(text.replace('\n',''))
                        

                for p in self.pin:
                    print(p)
                    idx = keypad.index(p)
                    self.driver.script("mtk.now.hidden.value += transkey_delimiter + mtk.getEncData('"+str(idx)+"')")
                    self.driver.script("document.querySelector('#" + self.inpTxtId + "').value+='" + p + "'")
                self.driver.script("document.querySelector('.dv_transkey_div_b').click()")

            else:
                print('test')
                print(self.inpTxtId )
                print(str(self.pin))
                # self.driver.find_element(By.ID, self.inpTxtId).send_keys('')
                self.driver.script("document.querySelector('#" + self.inpTxtId + "').value = '" + str(self.pin) + "'")
            sleep(0.5)
            
        self.driver.script("document.querySelector('#btnCshFrom').click()")
        
        sleep(2)

        # WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, 'chargeDatail')))
        return self
    
    def result(self):
        self.chargeResults = self.driver.script("return Array.prototype.slice.call(document.querySelectorAll('tr')).map(e => e.innerText)")
        self.chargeResults.pop(0)
        
        for chargeResult in self.chargeResults:
            rowData = chargeResult.split('\t')
            self.rslt.append({'number': rowData[0],
                                'orderNumber': rowData[0],\
                                'pin': rowData[1],\
                                'chargeResult': rowData[2],\
                                'amt': rowData[3]})
        return self.rslt
