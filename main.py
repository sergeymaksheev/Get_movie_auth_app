from fastapi import FastAPI
from pydantic import BaseModel
from pydantic import Field
from datetime import datetime
from typing import List, Optional
from enum import Enum


app = FastAPI(
    title='Trading App'
)

@app.get('/')
def hello():
    return 'Hello world!!!'

fake_users = [
    {'id': 1, 'role': ['admin'], 'name': 'sergey'},
    {'id': 2, 'role': 'trador', 'name': 'Milka'}
]

fake_trades = [
    {'id': 1, 'user_id': 1, 'price': 100},
    {'id': 2, 'user_id': 2, 'price': 200},
]

class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[List[Degree]]


@app.get('/users/{user_id}', response_model=List[User])
def get_user(user_id: int):
    return [user for user in fake_users if user.get('id') == user_id]

@app.get('/trades')
def get_trades(limit: int = 0, offset: int = 0):  # you can point default value
    return fake_trades[offset:][:limit]


@app.post('/users/{users_id}', response_model=List[User])
def change_user_name(user_id: int, new_name:str):
    current_user = list(filter(lambda user: user.get('id') == user_id, fake_users))[0]
    current_user['name'] = new_name
    return {'status': 200, 'data': current_user}


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades/')
def add_trades(trades: List[Trade]):
    fake_trades.extend(trades)
    return {'status': 200, 'data': fake_trades}