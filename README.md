# CampusEats Wallet - MVP

A minimal viable prototype for the Integrated Campus Dining Ecosystem.

## Features

- **Student App**: Wallet balance, mock top-up (Self/Parent), QR code payment, transaction history.
- **Vendor POS**: Tablet-optimized interface, QR scanning (with 5-min expiry), meal presets.
- **Admin Dashboard**: Analytics cards, transaction volume, dynamic waste reduction %, user management, and balance refunds.

## Setup Instructions

### Backend (Flask)

1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
4. `pip install -r requirements.txt`
5. `cp .env.example .env`
6. `python app.py` (Runs on http://localhost:5000)

### Frontend (React)

1. `cd frontend`
2. `npm install`
3. `npm start` (Runs on http://localhost:3000)

## Demo Roles

1. **Student**: Register as student -> Top up -> View QR in Profile.
2. **Vendor**: Register/Login as vendor -> Scan student QR -> Deduct meal cost.
3. **Admin**: Register/Login as admin -> View reports -> Manage users -> Process refunds.

## Technical Stack

- **Backend**: Flask, SQLAlchemy, JWT, Bcrypt, QRcode/Pillow.
- **Frontend**: React, Tailwind CSS, Recharts, Lucide-react (icons), dayjs.
- **Security**: JWT with 24h expiry, QR tokens with 5-min expiry.
