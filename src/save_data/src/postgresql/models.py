from sqlalchemy import Column, PickleType, Float, Integer

from .database import Base


class Prediction(Base):
    __tablename__ = "predictions_table"

    id = Column(Integer, primary_key=True, index=True)
    heure = Column(Integer)
    features = Column(PickleType)
    prediction = Column(Float)