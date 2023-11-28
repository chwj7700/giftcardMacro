from fastapi import APIRouter
from domain.giftCardDeal import GiftCardDeal

router = APIRouter(prefix="/deal", tags=["deal"])

@router.post('/list')
def list():
    print("TEST")
    result = GiftCardDeal().findDdartDeal().result()
    return result
