SplitPay – Blockchain Group Payment System

Problem Statement
Group payments are slow, confusing, and prone to errors.

Solution
SplitPay is a blockchain-based group expense settlement platform built on Algorand.  
It enables transparent, fast, and trustless payments with real-time verification.



Features

- Create & split bills
-Real-time payment verification (Algorand blockchain)
-Escrow smart contract (fund locking)
-Graph visualization (who owes whom)
- Voice input for bill creation
- QR code payments
- Reputation system
- Auto settlement (minimized transactions)
- Pera Wallet integration
- Supports ALGO & ASA tokens



Tech Stack

Backend
- Python (Flask)
- Algorand SDK
- PyTeal (Smart Contracts)

Frontend
- React.js
- Tailwind CSS
- Pera Wallet



Architecture

User → React Frontend → Flask API → Algorand Blockchain  
                                  ↘ Smart Contract (Escrow)



Smart Contract
- Built using PyTeal
- Locks funds until all users pay
- Releases funds only when conditions are met





