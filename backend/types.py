from pydantic import BaseModel


class TodoItem(BaseModel):
    category: str
    item: str


class NewTodoCategory(BaseModel):
    category: str


class UpdateTodoItem(BaseModel):
    id: str
    category: str
    new_item: str


class DeleteTodoItem(BaseModel):
    id: str
    category: str
