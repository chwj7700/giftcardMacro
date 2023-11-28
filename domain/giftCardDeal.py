import requests
from bs4 import BeautifulSoup


class GiftCardDeal():

    def __init__(self):
        self.rslt = []

    def findDdartDeal(self):
        response = requests.get('https://auto.ddart.net/market/')

        if response.status_code == 200 :
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')

            tbody = soup.select_one('#GIFTCARD_CONTENTS > div:nth-child(1) > div > table > tbody')
            trs = tbody.select('tr')
            
            for tr in trs:
                tds = tr.select('td')
                self.rslt.append({
                    'kind': tds[0].getText(),
                    'amt': tds[1].getText(),
                    'discountRate': tds[2].getText(),
                    'market' : tds[3].getText(),
                    'title' : tds[4].getText(),
                    'link': tds[4].find("a")["href"]
                })
        else:
            print(response.status_code)
        return self

    def result(self):
        return self.rslt
