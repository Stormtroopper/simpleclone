from typing import List
from datetime import datetime
from fastapi import APIRouter, HTTPException,status
from beanie import PydanticObjectId
from app.models.reservation import Reservation,ReservationStatus
from app.models.restaurant import Restaurant
from app.models.user import User

router=APIRouter(prefix="/reservations",tags=["Reservations"])
@router.post("/",response_model=Reservation,status_code=status.HTTP_201_CREATED)
async def create_reservation(reservation:Reservation):
    # validate restaurant
    restaurant=await Restaurant.find_one(Restaurant.id==reservation.restaurant.ref.id)
    if not restaurant or not restaurant.is_active:
        raise HTTPException(status_code=404,detail="Restaurant not available")
    #validate user
    user=await User.find_one(User.id==reservation.user.id)
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    #Check if the reservation time is in the past
    if reservation.reservation_time<datetime.utcnow():
        raise HTTPException(status_code=400,detail="Reservation time cannot be in the past") 
    await reservation.insert()
    return reservation
@router.get("/",response_model=List[Reservation])
async def list_reservations(user_id:PydanticObjectId|None=None,restaurant_id:PydanticObjectId|None=None,status:ReservationStatus|None=None,skip:int=0,limit:int=20):
    query=Reservation.find_all()
    if user_id:
        query=query.find(Reservation.user.id==user_id)
    if restaurant_id:
        query=query.find(Reservation.restaurant.ref.id==restaurant_id)
    if status:
        query=query.find(Reservation.status==status)
    return await query.skip(skip).limit(limit).to_list()
@router.get("/{reservation_id}",response_model=Reservation)
async def get_reservation(reservation_id:PydanticObjectId):
    reservation=await Reservation.get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=400,detail='Reservation not found')
    return reservation
@router.patch("/{resrrvation_id}",response_model=Reservation)
async def update_reservation_status(reservation_id:PydanticObjectId,new_status:ReservationStatus):
    reservation=await Reservation.get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=400,detail='Reservation not found')
    reservation.status=new_status
    await reservation.save()
    return reservation
@router.delete("/delete/{reservation_id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_reservation(reservation_id:PydanticObjectId):
    reservation=await Reservation.get(reservation_id)
    if not reservation:
        raise HTTPException(status_code=400,detail='Reservation not found')
    reservation.status=ReservationStatus.CANCELLED
    reservation.version+1
    await reservation.save()
    