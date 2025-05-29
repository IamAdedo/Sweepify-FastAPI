

import pyotp

def generate_totp_secret() -> str:
    return pyotp.random_base32()

def get_totp_uri(email: str, secret: str, issuer: str) -> str:
    return pyotp.totp.TOTP(secret).provisioning_uri(name=email, issuer_name=issuer)

def verify_totp(secret: str, code: str) -> bool:
    totp = pyotp.TOTP(secret)
    return totp.verify(code)
