# botg2/database/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True)
    tariff = Column(String(10), nullable=False)
    location = Column(String(50), nullable=False)
    subcode = Column(String(50), nullable=False)
    filename = Column(String(255), nullable=False)
    drive_id = Column(String(100), nullable=False)  # ID файла на Google Drive
