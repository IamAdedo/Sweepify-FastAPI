
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import user, sweep
from app.core.db import init_db

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG)

# CORS (customize for frontend later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # update in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database
@app.on_event("startup")
async def on_startup():
    await init_db()

# Routes
app.include_router(user.router, prefix="/api/users", tags=["Users"])
app.include_router(sweep.router, prefix="/api/sweep", tags=["Sweep"])

@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.APP_NAME} API"}
