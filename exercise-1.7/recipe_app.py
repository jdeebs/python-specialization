# Import the necessary SQLAlchemy modules and classes

# Core functionality for defining tables and creating the database engine
from sqlalchemy import create_engine, Column
# Data types for table columns
from sqlalchemy.types import Integer, String
# ORM tools for managing sessions and defining models
from sqlalchemy.orm import sessionmaker, declarative_base

# Create database engine to establish connection with existing
# MySQL database using MySQL credentials
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create a session factory that binds sessions to the engine
## Manages connections to the database via the engine
Session = sessionmaker(bind=engine)
# Create a session instance to interact with database
## Active connection to the database
session = Session()