from sqlalchemy import Column, Float, Integer

from .database import Base


class Prediction(Base):
    __tablename__ = "predictions_db_wine"

    id = Column(Integer, primary_key=True, index=True)
    heure = Column(Integer)
    
    fixed_acidity = Column(Float)
    volatile_acidity = Column(Float)
    citric_acid = Column(Float)
    sulfur_dioxide = Column(Float)
    pH = Column(Float)
    alcohol = Column(Float)
    quality = Column(Integer)