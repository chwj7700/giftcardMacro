import requests
from io import BytesIO
from PIL import Image
import numpy as np
from scraping import createDriver
from selenium.webdriver.common.by import By

driver = createDriver()
driver.get(url=f'https://m.cultureland.co.kr/mmb/loginMain.do')  # 주소 이동
transkeyUuid = driver.script("return mtk.transkeyUuid")
allocationIndex = driver.script("return transkey.passwd.allocationIndex")
keyIndex = driver.script("return transkey.passwd.keyIndex")

print(transkeyUuid)
print(allocationIndex)
print(keyIndex)
params = {
    'op':'getKey',
    'name':'passwd',
    'keyType':'lower',
    'keyboardType':'qwertyMobile',
    'fieldType':'password',
    'inputName':'passwd',
    'parentKeyboard':'false',
    'transkeyUuid': transkeyUuid,
    'exE2E':'false',
    'TK_requestToken':'0',
    'allocationIndex': allocationIndex,
    'keyIndex': keyIndex
}

response = requests.get('https://m.cultureland.co.kr/transkeyServlet', params=params)

# Img open
img = Image.open(BytesIO(response.content))
img = img.resize((1100,500))

left, top, right, bottom = 30, 30, 70, 70
result = []
for i in range(0,4):
    for j in range(0,11):
        img_cropped = img.crop((left + (j*100), top + (i*100), right + (j*100), bottom + (i*100)))
        image_nparray = np.array(img_cropped).flatten().tolist()
        result.append(any(image_nparray))

dkis = [i for i in range(len(result)) if result[i] == False]

print(dkis)
