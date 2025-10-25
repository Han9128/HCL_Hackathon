from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    email = Column(String(50), unique=True)
    password = Column(Text, nullable=True)
    full_name = Column(String(100))
    phone = Column(String(15))
    
    USER_ROLES = (
        ('CUSTOMER', 'CUSTOMER'),  
        ('ADMIN', 'ADMIN'),        
    )
    role = Column(ChoiceType(choices=USER_ROLES), default="CUSTOMER")
    
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    kyc_documents = relationship('KYCDocument', back_populates='user')

    def __repr__(self):
        return f"<User {self.email}>"

class KYCDocument(Base):
    __tablename__ = 'kyc_documents'
    
    DOCUMENT_TYPES = (
        ('AADHAAR', 'AADHAAR'),
        ('PAN', 'PAN'),
        ('PASSPORT', 'PASSPORT'),
        ('DRIVING_LICENSE', 'DRIVING_LICENSE')
    )
    
    KYC_STATUSES = (
        ('PENDING', 'PENDING'),
        ('VERIFIED', 'VERIFIED'), 
        ('REJECTED', 'REJECTED')
    )
    
    id = Column(Integer, primary_key=True)
    document_type = Column(ChoiceType(choices=DOCUMENT_TYPES))
    document_number = Column(String(50), nullable=False)
    document_image_url = Column(String(255))
    status = Column(ChoiceType(choices=KYC_STATUSES), default="PENDING")
    submitted_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='kyc_documents')

    def __repr__(self):
        return f"<KYCDocument {self.document_type} {self.id}>"