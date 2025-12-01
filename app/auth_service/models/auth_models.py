from pydantic import BaseModel, Field

class RegisterData(BaseModel):
    first_name: str = Field(min_length=3, max_length=20)
    last_name: str = Field(min_length=3, max_length=20)
    email: str = Field(pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')
    password: str = Field(min_length=8, max_length=20)

class LoginData(BaseModel):
    email: str = Field(pattern=r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$')
    password: str = Field(min_length=8, max_length=20)
