from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.proxy import router as proxy_router
app=FastAPI(title="API Gateway")
# allowed_origins = [
#     origin.strip()
#     for origin in os.getenv("CORS_ORIGINS", "http://localhost:5173").split(",")
#     if origin.strip()
# ]
app.middleware("cors")(CORSMiddleware(allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"]))
app.include_router(proxy_router)
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API Gateway is healthy"}