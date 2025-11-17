
# Multi-Wallet Microfinance SaaS – Phase 1

## Overview

This project is a multi-wallet microfinance platform designed to manage users, loans, and transactions in real-time. Phase 1 establishes the core system for account management and basic financial operations.

## Features Implemented in Phase 1

* **User Management**

  * Create, update, and delete user accounts
  * Unique user identification and authentication

* **Wallet Management**

  * Multi-wallet support per user
  * Real-time balance tracking

* **Loan Management**

  * Issue loans to users
  * Track loan status (active, repaid, overdue)

* **Transactions**

  * Record deposits, withdrawals, and transfers
  * Real-time transaction updates

## Tech Stack

* Backend: Python, FastAPI
* Database: PostgreSQL
* Migrations: Alembic
* API Testing: Postman / cURL

## Setup

1. Clone the repository

   ```bash
   git clone <repo-url>
   cd <repo-folder>
   ```
2. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
3. Configure environment variables (`.env`)
4. Run migrations

   ```bash
   alembic upgrade head
   ```
5. Start the server

   ```bash
   uvicorn main:app --reload
   ```

## Phase 1 Status

✅ Core user management implemented
✅ Wallets and transaction system implemented
✅ Basic loan issuance implemented
✅ API ready for internal testing
