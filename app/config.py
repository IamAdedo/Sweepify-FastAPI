import os
from pydantic import BaseSettings, EmailStr
from dotenv import load_dotenv

load_dotenv()  # Load .env values

class Settings(BaseSettings):
    # General
    APP_NAME: str = "Sweepify"
    DEBUG: bool = False

    # Security
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60
    TOTP_ISSUER_NAME: str = "Sweepify"

    # Database
    DATABASE_URL: str

    # Email
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    EMAIL_FROM: EmailStr
    EMAIL_FROM_NAME: str = "Sweepify"

    # Telegram
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str  # Optional: Can be dynamic per user later

    # Fee Config
    SERVICE_FEE_PERCENT: float = 10.0

    # Encryption
    ENCRYPTION_KEY: str  # 32-byte AES key (base64 or hex preferred)

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'

settings = Settings()
