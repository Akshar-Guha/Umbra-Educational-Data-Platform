# Copyright (c) 2024 Umbra. All rights reserved.
<<<<<<< HEAD
from pydantic import BaseModel, HttpUrl, ConfigDict, Field
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    user_identifier: str  # This will be the user-provided unique ID


class UserCreate(UserBase):
    password: str = Field(min_length=4)  # Password for creation, with min length of 4

=======
from pydantic import BaseModel, HttpUrl, ConfigDict
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str # Password for creation, not stored directly
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

class User(UserBase):
    id: int
    role: str
    registration_date: datetime
    last_login: Optional[datetime] = None
<<<<<<< HEAD
    learning_preferences: Optional[str] = (
        None  # JSON or similar for structured preferences
    )

    model_config = ConfigDict(from_attributes=True)


=======
    learning_preferences: Optional[str] = None # JSON or similar for structured preferences

    model_config = ConfigDict(from_attributes=True)

>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    url: HttpUrl
<<<<<<< HEAD
    instructor: Optional[str] = None
    price: Optional[float] = None
    currency: Optional[str] = None
    difficulty_level: Optional[str] = None  # Aligned with database model
    category: Optional[str] = None
    platform: Optional[str] = None

=======
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)

class CourseCreate(CourseBase):
    pass

<<<<<<< HEAD

=======
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
class Course(CourseBase):
    id: int
    created_by_user_id: Optional[int] = None
    creation_date: datetime
<<<<<<< HEAD
    ai_generated_version: int

    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_identifier: Optional[str] = None  # Renamed from username
=======
    difficulty_level: Optional[str] = None
    ai_generated_version: int

    model_config = ConfigDict(from_attributes=True) 
>>>>>>> 63e865f (Initial commit: Umbra Educational Data Platform)
