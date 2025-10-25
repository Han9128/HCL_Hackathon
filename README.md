# HCL_Hackathon

## Objective:
The objective is to build a user registration and kyc achieving the following functionality:
1. Submit Personal details
2. Upload KYC documents (simulated)
3. System validates and User profile

### Tech Stack required
FastAPI, PostgreSQL, JWT Auth

### What will we be doing?

1. User signup/login with JWT

2. Profile management

3. Document upload simulation

4. KYC status tracking (Pending/Approved/Rejected)

5. Admin approval system

## Core Endpoints we will build

### Authentication Routes
- `POST /auth/register` - New user registration
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### User Management
- `GET /users/me` - Get user profile
- `PUT /users/me` - Update profile
- `PUT /users/me/password` - Change password

### KYC Management
- `POST /kyc/documents` - Submit KYC documents
- `GET /kyc/status` - Check KYC status
- `GET /kyc/documents` - Get uploaded documents

### Admin Routes
- `GET /admin/users` - List all users
- `GET /admin/kyc/pending` - Pending KYC applications
- `PUT /admin/kyc/{user_id}/verify` - Approve KYC
- `PUT /admin/kyc/{user_id}/reject` - Reject KYC


### Example run


Register Customer 1
- Method: POST
- URL: `http://127.0.0.1:8000/auth/signup`
- Headers: 
  - `Content-Type: application/json`
- Body: (Raw JSON)
```json
{
  "email": "alice@bank.com",
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
  "email": "bob@bank.com",
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
  "email": "alice@bank.com",
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
  "email": "admin@smartbank.com",
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
  "email": "admin@smartbank.com",
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
- URL: `http://127.0.0.1:8000/admin/verify/1` 
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


