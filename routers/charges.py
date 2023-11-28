from fastapi import APIRouter
from dto.hmChargeDto import HmChargeDto
from dto.clChargeDto import ClChargeDto
from domain.hmCharge import HmCharge
from domain.clCharge import ClCharge
from domain.scraping import createDriver
from time import sleep
# ("/charge/") 라고 마지막에 슬레시 '/' 를 넣으면 안 된다.
router = APIRouter(prefix="/charge", tags=["charge"])

@router.post('/hm')
def charge(hmChargeDto:  HmChargeDto):
    try:
        id = hmChargeDto.id
        password = hmChargeDto.password
        pins = hmChargeDto.pins

        print('id : {0}, pins :{1}', id, pins)
        result = []
        driver = createDriver()
        hmCharge = HmCharge(driver).login(id, password)

        while (len(pins)):  # TODO 충전도중에 죽으면?
            splitedPins = '-'.join(pins).replace('_', '-').split('-')
            result = hmCharge.charge(splitedPins).result()
            pins = pins[10:]
    finally:
        driver.close()
    return result


@router.post('/cl')
async def charge(clChargeDto:  ClChargeDto):
    try:
        id = clChargeDto.id
        password = clChargeDto.password
        pins = clChargeDto.pins

        print('id : {0}, pins :{1}', id, pins)
        result = []
        driver = createDriver()
        clCharge = ClCharge(driver).login(id, password)
        splitedPins = '-'.join(pins).split('-')

        await clCharge.charge(splitedPins)
            #while (len(pins)):  # TODO 충전도중에 죽으면?
            #    splitedPins = '-'.join(pins).replace('_', '-').split('-')
            #    result = clCharge.charge(splitedPins).result()
            #    pins = pins[10:]
    finally:
    #   driver.close()
        pass
    return result
