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
- FastAPI
- SQLAlchemy (PostgreSQL or SQLite)
- Docker / Docker Compose
- JWT Auth + TOTP (2FA)

## 📦 Deployment

```bash
git clone  https://github.com/your-username/sweepify-fastapi.git
cd sweepify-fastapi
cp .env.example .env
docker-compose up --build
