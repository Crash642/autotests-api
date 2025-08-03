
from pydantic import BaseModel, Field, EmailStr


class CreateUserRequestSchema(BaseModel):
    """запрос на создание пользователя"""
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class UserSchema(CreateUserRequestSchema):
    """модель данных пользователя"""
    id: str


class CreateUserResponseSchema(BaseModel):
    """ответ с данными созданного пользователя"""
    user: UserSchema

