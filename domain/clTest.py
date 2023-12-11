import requests
from io import BytesIO
from PIL import Image
import numpy as np
from scraping import createDriver
from selenium.webdriver.common.by import By
from pytesseract import *
import os

# driver = createDriver()
# driver.get(url=f'https://m.cultureland.co.kr/mmb/loginMain.do')  # 주소 이동
# transkeyUuid = driver.script("return mtk.transkeyUuid")
# allocationIndex = driver.script("return transkey.passwd.allocationIndex")
# keyIndex = driver.script("return transkey.passwd.keyIndex")

# print(transkeyUuid)
# print(allocationIndex)
# print(keyIndex)
# params = {
#     'op':'getKey',
#     'name':'passwd',
#     'keyType':'lower',
#     'keyboardType':'qwertyMobile',
#     'fieldType':'password',
#     'inputName':'passwd',
#     'parentKeyboard':'false',
#     'transkeyUuid': transkeyUuid,
#     'exE2E':'false',
#     'TK_requestToken':'0',
#     'allocationIndex': allocationIndex,
#     'keyIndex': keyIndex
# }

# response = requests.get('https://m.cultureland.co.kr/transkeyServlet', params=params)
url = 'https://m.cultureland.co.kr/transkeyServlet?op=getKey&name=txtScr24&keyType=single&keyboardType=numberMobile&fieldType=password&inputName=scr24&parentKeyboard=false&transkeyUuid=fb20bba691a7b13d0337a1f48086056d60e316f4b319c6d795817b25166f0f50&exE2E=false&TK_requestToken=0&allocationIndex=2545914344&keyIndex=5911256f4be408bde8dad1713d49ee0f6e84fe6c95da6b10d4a8de012abb941d301f20e2f8a94eef7df9d506e36e794bd80507fa547b746dd32c63f011025af43f25aa29f1c245c9ee5b9d522450fb73ee2370a13d0cbffd7eaf969cbcb81975a032203846220234055f8570455d4cb405d729479fac7a3d7b27d9abf65ada53ac875740073e3f4ab1b9f4cac91e60ce8493ebf766b7ff3e4a6af485caa0ea18527383d4b832098cba7fbd78444796a869fb2585b2a4e4a587bde5f31a5a6c220bfb4d13262bc6124547760ac2ea33d9c53ddd392b1b3fc966adac0e6aaa89b3b9971f02c7b1d42d267a4bfc58e85f193c4fbd46b5171070c2dd54e281b8a6ad&initTime=-167549625902339373777744137549753639762&quot'
response = requests.get(url)

# Img open
img = Image.open(BytesIO(response.content))

img = img.resize((500,455))
img.show()
left, top, right, bottom = 0, 0, 125, 112
result = []
for i in range(0,3):
    for j in range(0,4):
        img_cropped = img.crop((left + (j*125), top + (i*112), right + (j*125), bottom + (i*112)))
        # img_cropped.show()
        # image_nparray = np.array(img_cropped).flatten().tolist()
        text = pytesseract.image_to_string(img_cropped, config='--psm 6') 
        result.append(text.replace('\n',''))

# dkis = [i for i in range(len(result)) if result[i] == False]

print(result)
