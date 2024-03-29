from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create database engine
engine = create_engine('sqlite:///patient_manager.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define Patient model
class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    address = Column(String)

# Create database tables
Base.metadata.create_all(engine)

# Create a session factory
Session = sessionmaker(bind=engine)
