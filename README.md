# 🚀 SplitPay – Blockchain Group Payment System

## 📌 Problem Statement
Group payments are slow, confusing, and prone to errors.

## 💡 Solution
SplitPay is a blockchain-based group expense settlement platform built on Algorand.  
It enables transparent, fast, and trustless payments with real-time verification.

---

## ⚙️ Features

- 🧾 Create & split bills
- 💸 Real-time payment verification (Algorand blockchain)
- 🔐 Escrow smart contract (fund locking)
- 📊 Graph visualization (who owes whom)
- 🎤 Voice input for bill creation
- 📱 QR code payments
- 🏆 Reputation system
- ⚡ Auto settlement (minimized transactions)
- 🔗 Pera Wallet integration
- 🪙 Supports ALGO & ASA tokens

---

## 🧠 Tech Stack

### Backend
- Python (Flask)
- Algorand SDK
- PyTeal (Smart Contracts)

### Frontend
- React.js
- Tailwind CSS
- Pera Wallet

---

## 🏗️ Architecture

User → React Frontend → Flask API → Algorand Blockchain  
                                  ↘ Smart Contract (Escrow)

---

## 🔐 Smart Contract
- Built using PyTeal
- Locks funds until all users pay
- Releases funds only when conditions are met

---

## 🚀 How to Run

### Backend

```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm start
```

---

## 🧪 Testing

```bash
python test_escrow.py
```

---

## 🌍 Deployment

- Backend: Render
- Frontend: Vercel

---

## 📊 Demo Flow

1. Create bill
2. Split among users
3. Connect wallet
4. Pay using ALGO
5. Verify transaction
6. View graph & settlement

---

## 🔥 Future Improvements

- Mobile app (Capacitor)
- AI-based expense prediction
- Multi-chain support

---

## 👨‍💻 Author
Your Name

---

## ⭐ If you like this project, give it a star!
