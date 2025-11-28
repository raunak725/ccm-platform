from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Control, Tenant

router = APIRouter(prefix="/controls", tags=["controls"])

@router.get("/")
def list_controls(db: Session = Depends(get_db)):
    return db.query(Control).all()

@router.post("/")
def seed_controls(db: Session = Depends(get_db)):
    # create dummy tenant & two controls for demo
    tenant = db.query(Tenant).first()
    if not tenant:
        tenant = Tenant(name="DemoCo")
        db.add(tenant)
        db.commit()
        db.refresh(tenant)
    if db.query(Control).count() == 0:
        db.add(Control(name="3-way match", description="PO = Receipt = Invoice", status="pass", tenant_id=tenant.id))
        db.add(Control(name="SOD", description="Creator ≠ Approver", status="fail", tenant_id=tenant.id))
        db.commit()
    return {"msg": "seeded"}