from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Tenant(Base):
    __tablename__ = "tenants"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

class Control(Base):
    __tablename__ = "controls"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    status = Column(String, default="pass")  # pass / fail / error
    tested_at = Column(DateTime)
    tenant_id = Column(Integer, ForeignKey("tenants.id"))
    tenant = relationship("Tenant")