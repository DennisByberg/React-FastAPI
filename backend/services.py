import database as _database


# Function to create the database tables
def create_database():
    # Create all tables defined in the metadata of the Base class
    # bind=_database.engine:
    # Use the engine defined in the database module to connect to the database
    return _database.Base.metadata.create_all(bind=_database.engine)
