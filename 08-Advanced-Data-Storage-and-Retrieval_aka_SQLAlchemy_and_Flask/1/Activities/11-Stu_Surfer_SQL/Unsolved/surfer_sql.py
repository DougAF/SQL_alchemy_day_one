# Import SQL Alchemy
from sqlalchemy import create_engine


# Import and establish Base for which classes will be constructed 
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# Import modules to declare columns and column data types
from sqlalchemy import Column, Integer, String, Float

# Create Surfer and Board classes
# ----------------------------------


# Create specific instances of the Surfer and Board classes
# ----------------------------------
# Create a new surfer named "Bruno"
# Create a new board and associate it with a surfer's ID


# Create Database Connection
# ----------------------------------
# Establish Connection to a sqlite database


# Create both the Surfer and Board tables within the database


# To push the objects made and query the server we use a Session object


# Add "Bruno" to the current session
# Add "Awwwyeah" to the current session
# Commit both objects to the database


# Query the database and collect all of the surfers in the Surfer table


