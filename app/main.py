from fastapi import FastAPI
from app.database import engine, Base
from app.routers import controls

# Create tables on startup (ok for MVP)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="CCM Platform", version="0.1.0")
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(controls.router)

@app.get("/")
def read_root():
    return {"msg": "Continuous Controls Monitoring API v0.1.0"}