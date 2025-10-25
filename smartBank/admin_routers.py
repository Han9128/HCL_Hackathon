from fastapi import APIRouter, HTTPException, status, Depends
from database import Session, engine
from models import KYCDocument, User
from fastapi_jwt_auth import AuthJWT

session = Session(bind=engine)
admin_router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

@admin_router.get("/")
async def get_pending_kyc(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    if user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    pending_documents = session.query(KYCDocument).filter(
        KYCDocument.status == "PENDING"
    ).all()
    
    return [{
        "id": doc.id,
        "document_type": doc.document_type,
        "document_number": doc.document_number,
        "user_id": doc.user_id,
        "submitted_at": doc.submitted_at
    } for doc in pending_documents]

@admin_router.post("/verify/{document_id}")
async def verify_kyc_document(document_id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    if user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    document = session.query(KYCDocument).filter(KYCDocument.id == document_id).first()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    document.status = "VERIFIED"
    session.commit()
    
    return {"message": "KYC document verified successfully"}

@admin_router.post("/reject/{document_id}")
async def reject_kyc_document(document_id: int, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    if user.role != "ADMIN":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin access required"
        )
    
    document = session.query(KYCDocument).filter(KYCDocument.id == document_id).first()
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found"
        )
    
    document.status = "REJECTED"
    session.commit()
    
    return {"message": "KYC document rejected"}