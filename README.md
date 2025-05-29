# Sweepify-FastAPI
A FastAPI-based SaaS that enables users to securely sweep funds from compromised crypto wallets to safe destinations. Supports multiple blockchains, encrypted key storage, email &amp; Telegram notifications, and adjustable service fees for the provider.

# 🧹 Crypto Sweeper Bot

A SaaS platform built with **FastAPI** that helps users securely sweep funds from vulnerable or compromised crypto wallets across multiple blockchains into a safe destination.

## 🚀 Features

- 🌐 Multi-chain sweeping: BTC, ETH, BSC, TON, SUI, and Pi Network (planned)
- 🔐 Encrypted private key storage
- 🛡️ Two-Factor Authentication (2FA)
- ✉️ Email and Telegram notifications
- 🧮 Dynamic service fee configuration (default: 10%)
- 🧑‍💼 Admin dashboard for managing users, logs, and system settings
- 🐳 Dockerized for easy deployment

## 🛠️ Tech Stack
- **Backend**: FastAPI + SQLAlchemy
- **Database**: PostgreSQL or SQLite
- **Auth**: JWT + 2FA (PyOTP)
- **Notifications**: SMTP + Telegram Bot API
- **Deployment**: Docker & Docker Compose


## 📦 Deployment

```bash
git clone  https://github.com/IamAdedo/sweepify-fastapi.git
cd sweepify-fastapi
cp .env.example .env
docker-compose up --build
```


## ⚠️ Disclaimer

Sweepify is intended for ethical recovery of assets from wallets under user control. Misuse is strictly prohibited. The developers are not liable for unauthorized use of this software.


with ❤️ by 𝙸𝚊𝚖𝙰𝚍𝚎𝚍𝚘 𓆩☬𓆪 ㄒ卄乇 ㄥ卂乙ㄚ 卄凵几ㄒ乇尺


# 🧹 Sweepify (FastAPI Edition)

**Sweepify** is a secure crypto sweeping platform built with **FastAPI**, enabling users to safely transfer tokens from compromised wallets to secure addresses across multiple blockchains.

## 🌟 Key Features

- ✅ **Multi-chain support**: Pi (placeholder), BTC, ETH, BSC, TON, SUI
- 🔐 **Private key encryption** (AES-256)
- 📱 **2FA (TOTP)** with backup codes
- 📩 **Email & Telegram notifications**
- 💸 **10% service fee** on every sweep (configurable)
- 🧑‍💼 Admin dashboard (coming soon)
- 🐳 Dockerized for easy deployment

---

## ⚙️ Tech Stack

- **Backend**: FastAPI + SQLAlchemy
- **Database**: PostgreSQL or SQLite
- **Auth**: JWT + 2FA (PyOTP)
- **Notifications**: SMTP + Telegram Bot API
- **Deployment**: Docker & Docker Compose

---

## 🚀 Getting Started

```bash
git clone https://github.com/your-username/sweepify-fastapi.git
cd sweepify-fastapi
cp .env.example .env
docker-compose up --build
