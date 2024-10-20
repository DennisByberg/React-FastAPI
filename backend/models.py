import datetime as _dt
import sqlalchemy as _sql
import sqlalchemy.orm as _orm
import passlib.hash as _hash
import database as _database


# Define the User model
class User(_database.Base):
    __tablename__ = "users"  # Name of the table in the database

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    email = _sql.Column(_sql.String, unique=True)
    hashed_password = _sql.Column(_sql.String)

    # Relationship to the Lead model
    leads = _orm.relationship("Lead", back_populates="owner")

    def verify_password(self, password: str):
        return _hash.bcrypt.verify(password, self.hashed_password)


# Define the Lead model
class Lead(_database.Base):
    __tablename__ = "leads"  # Name of the table in the database

    id = _sql.Column(_sql.Integer, primary_key=True, index=True)
    owner_id = _sql.Column(_sql.Integer, _sql.ForeignKey("users.id"))
    first_name = _sql.Column(_sql.String, index=True)
    last_name = _sql.Column(_sql.String, index=True)
    email = _sql.Column(_sql.String, index=True)
    company = _sql.Column(_sql.String, index=True, default="")
    note = _sql.Column(_sql.String, default="")
    date_created = _sql.Column(
        _sql.DateTime, default=lambda: _dt.datetime.now(_dt.timezone.utc)
    )
    date_last_updated = _sql.Column(
        _sql.DateTime, default=lambda: _dt.datetime.now(_dt.timezone.utc)
    )

    # Relationship to the User model
    owner = _orm.relationship("User", back_populates="leads")
