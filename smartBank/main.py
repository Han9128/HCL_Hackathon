from fastapi import FastAPI
from auth_routers import auth_router
from kyc_routers import kyc_router
from admin_routers import admin_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings

app = FastAPI(title="SmartBank KYC API", version="1.0.0")

@AuthJWT.load_config
def get_config():
    return Settings()

app.include_router(auth_router)
app.include_router(kyc_router)
app.include_router(admin_router)

@app.get("/")
async def root():
    return {"message": "SmartBank KYC API - Welcome to the banking system"}