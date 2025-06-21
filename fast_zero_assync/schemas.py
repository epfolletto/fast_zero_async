from pydantic import BaseModel, ConfigDict, EmailStr, Field

from fast_zero_assync.models import TodoState


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    id: int
    model_config = ConfigDict(from_attributes=True)


class UserList(BaseModel):
    users: list[UserPublic]


class Token(BaseModel):
    access_token: str
    token_type: str


class FilterPage(BaseModel):
    offset: int = 0
    limit: int = 100


class TodoSchema(BaseModel):
    title: str
    description: str
    state: TodoState = Field(default=TodoState.todo)


class TodoPublic(TodoSchema):
    id: int


class FilterTodo(FilterPage):
    title: str | None = Field(default=None, min_length=3)
    description: str | None = None
    state: TodoState | None = None


class TodoUpdate(BaseModel):
    title: str | None = None
    description: str | None = None  # poderia usar o Optional
    state: TodoState | None = None


class TodoList(BaseModel):
    todos: list[TodoPublic]
