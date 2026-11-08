from fastapi import APIRouter,HttpException,Request
from app.api import user_url,booking_url,restaurant_url
import httpx
router = APIRouter()
SERVICE_URLS={
    "users":user_url,
    "bookings":booking_url,
    "restaurants":restaurant_url
}
@router.api_route("/{service_name}/{path:path}",methods=["GET","POST","PUT","DELETE"])
async def proxy_request(service_name:str,path:str,request:Request):
    if service_name not in SERVICE_URLS:
        raise HttpException(status_code=404,detail=f"Service {service_name} not found")
    url=f"{SERVICE_URLS[service_name]}/{path}"
    async with httpx.AsyncClient() as client:
        try:
            response=await client.request(
                method=request.method,
                url=url,
                headers=request.headers.raw,
                content=await request.body()
            )
            return response.json()
        except httpx.RequestError as e:
            raise HttpException(status_code=500,detail=str(e))