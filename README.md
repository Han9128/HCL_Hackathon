# SmartBank KYC API - HCL Hackathon

## Objective:
The objective is to build a user registration and kyc achieving the following functionality:
1. Submit Personal details
2. Upload KYC documents (simulated)
3. System validates and User profile

### Tech Stack
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL (hosted on Supabase)
- **Authentication**: JWT Tokens
- **ORM**: SQLAlchemy
- **Security**: Password hashing with Werkzeug

## System Architecture

### Core Modules
- **Authentication System** (`auth_routers.py`) - User registration, login, JWT management
- **KYC Management** (`kyc_routers.py`) - Document submission and status tracking
- **Admin Panel** (`admin_routers.py`) - KYC verification and approval system
- **Data Models** (`models.py`) - Database schema definition
- **API Validation** (`schemas.py`) - Request/response serialization

## API Endpoints

### Authentication Routes
- `POST /auth/signup` - New user registration
- `POST /auth/login` - User login with JWT token generation
- `GET /auth/refresh` - Refresh access token using refresh token
- `GET /auth/` - Protected test endpoint

### User KYC Management
- `POST /kyc/documents` - Submit KYC documents (AADHAAR, PAN, PASSPORT, DRIVING_LICENSE)
- `GET /kyc/documents` - Get user's submitted KYC documents
- `GET /kyc/status` - Check overall KYC verification status

### Admin Routes
- `GET /admin/` - View all pending KYC documents
- `POST /admin/verify/{document_id}` - Approve specific KYC document
- `POST /admin/reject/{document_id}` - Reject specific KYC document

## Database Schema

### Users Table
- `id`, `email`, `password` (hashed), `full_name`, `phone`
- `role` (CUSTOMER/ADMIN), `is_active`, `created_at`

### KYC Documents Table
- `id`, `document_type`, `document_number`, `document_image_url`
- `status` (PENDING/VERIFIED/REJECTED), `submitted_at`, `user_id`


## Workflow
1. User registers via `/auth/signup`
2. User logs in and obtains JWT token via `/auth/login`
3. User submits KYC documents via `/kyc/documents`
4. Admin reviews pending documents via `/admin/`
5. Admin approves/rejects documents via `/admin/verify|reject/{id}`
6. User checks verification status via `/kyc/status`

## Setup & Execution
1. clone the repository using `git clone https://github.com/Han9128/HCL_Hackathon.git`
2. 2. switch to smartBank folder using `cd smartBank`
1. Run `init_db.py` to initialize database tables
2. Start the FastAPI server: `uvicorn main:app --reload`
3. Use `examples run` for comprehensive API testing scenarios
4. Access API documentation at `http://127.0.0.1:8000/docs`

### Example run


Register Customer 1
- Method: POST
- URL: `http://127.0.0.1:8000/auth/signup`
- Headers: 
  - `Content-Type: application/json`
- Body: (Raw JSON)
```json
{
  "email": "alice@bankd.com",
  "password": "alice123",
  "full_name": "Alice Johnson",
  "phone": "+1111111111",
  "role": "CUSTOMER"
}
```

Register Customer 2
- Method: POST
- URL: `http://127.0.0.1:8000/auth/signup`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "email": "bob@banke.com",
  "password": "bob123", 
  "full_name": "Bob Smith",
  "phone": "+1222222222",
  "role": "CUSTOMER"
}
```

### Customer Login (GET TOKEN)
- Method: POST
- URL: `http://127.0.0.1:8000/auth/login`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "email": "alice@bankd.com",
  "password": "alice123"
}
```
**SAVE THE ACCESS TOKEN** 

### KYC Document Submission

#### Submit KYC Documents (with Auth)
- Method: POST
- URL: `http://127.0.0.1:8000/kyc/documents`
- Headers: 
  - `Content-Type: application/json`
  - `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE` 
- Body:
```json
{
  "document_type": "AADHAAR",
  "document_number": "1234-5678-9012",
  "document_image_url": "https://bank.com/documents/alice_aadhaar.jpg"
}
```
**Save Response:** Note the document ID

#### Submit Second Document
- Method: POST
- URL: `http://127.0.0.1:8000/kyc/documents`
- Headers: 
  - `Content-Type: application/json`
  - `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE`
- Body:
```json
{
  "document_type": "PAN",
  "document_number": "ABCDE1234F",
  "document_image_url": "https://bank.com/documents/alice_pan.jpg"
}
```

#### View Submitted Documents
- Method: GET
- URL: `http://127.0.0.1:8000/kyc/documents`
- Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE`

#### Check KYC Status
- Method: GET
- URL: `http://127.0.0.1:8000/kyc/status`
- Headers: `Authorization: Bearer YOUR_ACCESS_TOKEN_HERE`

#### Register Admin User
- Method: POST
- URL: `http://127.0.0.1:8000/auth/signup`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "email": "admin@smartbankd.com",
  "password": "admin123",
  "full_name": "Bank Manager",
  "phone": "+1999999999",
  "role": "ADMIN"
}
```

#### Admin Login (GET ADMIN TOKEN)
- Method: POST
- URL: `http://127.0.0.1:8000/auth/login`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "email": "admin@smartbankd.com",
  "password": "admin123"
}
```
**SAVE THE ADMIN ACCESS TOKEN**

#### View Pending KYC (Admin)
- Method: GET
- URL: `http://127.0.0.1:8000/admin/`
- Headers: `Authorization: Bearer ADMIN_ACCESS_TOKEN_HERE`

#### Verify Documents (Admin)
- Method: POST
- URL: `http://127.0.0.1:8000/admin/verify/1` (replace 1 with your id)
- Headers: `Authorization: Bearer ADMIN_ACCESS_TOKEN_HERE`

#### Verify Second Document
- Method: POST
- URL: `http://127.0.0.1:8000/admin/verify/2`
- Headers: `Authorization: Bearer ADMIN_ACCESS_TOKEN_HERE`

### Final Verification

#### Check Final Status (as Customer)
- Method: GET
- URL: `http://127.0.0.1:8000/kyc/status`
- Headers: `Authorization: Bearer CUSTOMER_ACCESS_TOKEN_HERE`

#### View Verified Documents
- Method: GET
- URL: `http://127.0.0.1:8000/kyc/documents`
- Headers: `Authorization: Bearer CUSTOMER_ACCESS_TOKEN_HERE`


