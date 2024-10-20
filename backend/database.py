import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# Define the database URL for SQLite
DATABASE_URL = "sqlite:///./database.db"

# Create a SQLAlchemy engine instance with the specified database URL
# The connect_args parameter is used to set SQLite-specific options
engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a configured "Session" class
# autocommit=False: Transactions are not automatically committed
# autoflush=False: Changes are not automatically flushed to the database
# bind=engine: Bind the session to the engine
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative class definitions
Base = _declarative.declarative_base()
