from sqlalchemy import Column, Float, Integer, Boolean

from .database import Base


class Prediction(Base):
    __tablename__ = "predictions_db"

    id = Column(Integer, primary_key=True, index=True)
    heure = Column(Integer)
    size = Column(Integer)
    nbrooms = Column(Integer)
    garden = Column(Boolean)
    prediction = Column(Float)