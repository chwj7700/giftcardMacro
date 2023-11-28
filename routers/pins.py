from fastapi import APIRouter
from domain.giftCardPin import GiftCardPin
from dto.ssgPinDto import SsgPinDto
from domain.scraping import createDriver

router = APIRouter(prefix="/pin", tags=["pin"])

@router.post('/ssg')
def list(ssgPinDto : SsgPinDto):
    try:
        id = ssgPinDto.id
        password = ssgPinDto.password

        print('id : {0}', id)
        result = []
        driver = createDriver()
        
        print("TEST")
        result = GiftCardPin(driver).findSsgPin(id, password).result()
    finally:
        driver.close()
    return result
