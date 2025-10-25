from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class SignUp(BaseModel):
    email: EmailStr
    password: str
    full_name: str
    phone: str
    role: Optional[str] = "CUSTOMER"  

    class Config:
        from_attributes = True
        schema_extra = {
            'example': {
                "email": "customer@bank.com",
                "password": "securepassword", 
                "full_name": "John Doe",
                "phone": "+1234567890",
                "role": "CUSTOMER"  
            }
        }

class LoginModel(BaseModel):
    email: str
    password: str

class Settings(BaseModel):
    authjwt_secret_key: str = 'a3924b7e2f3e53585205fba13130b3e415354d2ad562fdcbc06e78fba4353537'

class KYCDocumentCreate(BaseModel):
    document_type: str
    document_number: str
    document_image_url: Optional[str] = None

class KYCDocumentResponse(BaseModel):
    id: int
    document_type: str
    document_number: str  
    status: str
    submitted_at: datetime

    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    email: str
    full_name: str
    phone: str
    role: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True