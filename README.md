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

## Core Endpoints to Build

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


