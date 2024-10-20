import datetime as _dt
import pydantic as _pydantic


# Base class for User schemas
class _UserBase(_pydantic.BaseModel):
    email: str


# Schema for creating a new user
class UserCreate(_UserBase):
    hashed_password: str

    class Config:
        orm_mode = True


# Schema for representing a user
class User(_UserBase):
    id: int

    class Config:
        orm_mode = True


# Base class for Lead schemas
class _LeadBase(_pydantic.BaseModel):
    first_name: str
    last_name: str
    email: str
    company: str
    note: str


# Schema for creating a new lead
class LeadCreate(_LeadBase):
    pass


# Schema for representing a lead
class Lead(_LeadBase):
    id: int
    owner_id: int
    date_created: _dt.datetime
    date_last_updated: _dt.datetime

    class Config:
        orm_mode = True
