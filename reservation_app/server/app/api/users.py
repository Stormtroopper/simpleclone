from typing import List
from fastapi import APIRouter,HTTPException, status
from beanie import PydanticObjectId
from app.models.user import User
router=APIRouter(prefix="/users",tags=["Users"])
@router.post("/",response_model=User,status_code=status.HTTP_201_CREATED)
async def create_user(user:User):
    check_user=await User.find_one(User.email==user.email)
    if check_user:
        raise HTTPException(status_code=400,detail="Email Already exists")
    new_user=await user.insert()
    return new_user
@router.get("/",response_model=List[User])
async def get_users(skip:int=0,limit:int=10):
    return await User.find(User.is_active==True).skip(skip).limit(limit).to_list()
@router.get("/{user_id}",response_model=User)
async def get_user(user_id:PydanticObjectId):
    user=await User.get(user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=404,detail="User not found")
    return user
