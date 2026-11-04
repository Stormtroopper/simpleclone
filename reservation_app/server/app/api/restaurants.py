from typing import List
from fastapi import APIRouter,HTTPException,status
from beanie import PydanticObjectId
from app.models.restaurant import Restaurant
router=APIRouter(prefix="/restaurants",tags=["Restaurants"])
@router.post('/',response_model=Restaurant)
async def create_restaurant(restaurant:Restaurant):
    await restaurant.insert()
    return restaurant
@router.get('/',response_model=List[Restaurant])
async def list_restaurants(city:str|None=None,limit:int=20,skip:int=0):
    query=Restaurant.find(Restaurant.is_active==True)
    if city:
        query=query.find(Restaurant.city==city)
    return await query.skip(skip).limit(limit).to_list()
@router.get('/{restaurant_id}',response_model=Restaurant)
async def get_restaurant(restaurant_id:PydanticObjectId):
    restaurant=await Restaurant.get(restaurant_id)
    if not restaurant or not restaurant.is_active:
        raise HTTPException(status_code=404,detail="Restaurant not found")
    return restaurant
@router.delete('/delete/{restaurant_id}',status_code=status.HTTP_204_NO_CONTENT)
async def cancel_restaurant(restaurant_id:PydanticObjectId):
    resturant_cancelled=await Restaurant.get(restaurant_id)
    if not resturant_cancelled or not resturant_cancelled.is_active:
        raise HTTPException(status_code=404,detail="Restaurant not found")
    resturant_cancelled.is_active=False
    await resturant_cancelled.save()
        