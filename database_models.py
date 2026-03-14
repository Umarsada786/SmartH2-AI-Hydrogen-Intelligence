# database_models.py

from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class HydrogenProduction(Base):
    __tablename__ = 'hydrogen_production'

    id = Column(Integer, primary_key=True)
    production_volume = Column(Float, nullable=False)  # in kg
    production_date = Column(DateTime, nullable=False)


class EquipmentSensor(Base):
    __tablename__ = 'equipment_sensors'

    id = Column(Integer, primary_key=True)
    sensor_type = Column(String, nullable=False)
    value = Column(Float, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    production_id = Column(Integer, ForeignKey('hydrogen_production.id'))

    production = relationship('HydrogenProduction', back_populates='sensors')


class MaintenanceRecord(Base):
    __tablename__ = 'maintenance_records'

    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment_sensors.id'))
    maintenance_date = Column(DateTime, nullable=False)
    description = Column(String, nullable=False)

    equipment = relationship('EquipmentSensor')


class EnergyData(Base):
    __tablename__ = 'energy_data'

    id = Column(Integer, primary_key=True)
    energy_consumption = Column(Float, nullable=False)  # in kWh
    timestamp = Column(DateTime, nullable=False)


class MarketData(Base):
    __tablename__ = 'market_data'

    id = Column(Integer, primary_key=True)
    market_price = Column(Float, nullable=False)  # per kg
    timestamp = Column(DateTime, nullable=False)  

# Relationships
HydrogenProduction.sensors = relationship('EquipmentSensor', back_populates='production')