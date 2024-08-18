from pydantic import BaseModel


class TodoItem(BaseModel):
    category: str
    item: str


class NewTodoCategory(BaseModel):
    category: str


class UpdateTodoItem(BaseModel):
    category: str
    old_item: str
    new_item: str
