from fastapi import APIRouter, HTTPException, status, Depends
from database import Session, engine
from schemas import KYCDocumentCreate, KYCDocumentResponse
from models import KYCDocument, User
from fastapi_jwt_auth import AuthJWT

session = Session(bind=engine)
kyc_router = APIRouter(
    prefix='/kyc',
    tags=['kyc']
)

@kyc_router.get("/")
async def hello_kyc():
    return {"message": "Hello, KYC System"}

@kyc_router.post("/documents")
async def submit_kyc_document(document: KYCDocumentCreate, Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    existing_doc = session.query(KYCDocument).filter(
        KYCDocument.user_id == user.id,
        KYCDocument.document_type == document.document_type
    ).first()
    
    if existing_doc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"{document.document_type} document already submitted"
        )
    
    new_document = KYCDocument(
        document_type=document.document_type,
        document_number=document.document_number,
        document_image_url=document.document_image_url,
        user_id=user.id
    )
    
    session.add(new_document)
    session.commit()
    session.refresh(new_document)
    
    return {
        "id": new_document.id,
        "document_type": new_document.document_type,
        "document_number": new_document.document_number,
        "status": new_document.status,
        "submitted_at": new_document.submitted_at
    }

@kyc_router.get("/documents")
async def get_my_kyc_documents(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    documents = session.query(KYCDocument).filter(
        KYCDocument.user_id == user.id
    ).all()
    
    return [{
        "id": doc.id,
        "document_type": doc.document_type,
        "document_number": doc.document_number,
        "status": doc.status,
        "submitted_at": doc.submitted_at
    } for doc in documents]

@kyc_router.get("/status")
async def get_kyc_status(Authorize: AuthJWT = Depends()):
    try:
        Authorize.jwt_required()
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Token"
        )
    
    current_user_email = Authorize.get_jwt_subject()
    user = session.query(User).filter(User.email == current_user_email).first()
    
    documents = session.query(KYCDocument).filter(
        KYCDocument.user_id == user.id
    ).all()
    
    if not documents:
        return {"status": "NO_DOCUMENTS", "message": "No KYC documents submitted"}
    
    all_verified = all(doc.status == "VERIFIED" for doc in documents)
    any_rejected = any(doc.status == "REJECTED" for doc in documents)
    any_pending = any(doc.status == "PENDING" for doc in documents)
    
    if all_verified:
        return {"status": "VERIFIED", "message": "All documents verified"}
    elif any_rejected:
        return {"status": "REJECTED", "message": "Some documents were rejected"}
    elif any_pending:
        return {"status": "PENDING", "message": "Documents under review"}
    
    return {"status": "UNKNOWN", "message": "Unexpected status"}