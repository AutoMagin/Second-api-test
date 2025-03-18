import json
import os
from enum import Enum
from pydantic import BaseModel
from typing import Optional


FILE_PATH = "zakaz.json"


def read_json():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        return json.load(file)

def write_json(data):
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

class OrderState(str, Enum):
    empty = ""
    pending = "В ожидании"
    preparing = "Готовиться"
    served = "Подан"
    cancelled = "Отменён"

class Item(BaseModel):
    first_meal : str
    second_meal : str
    drink : str

class Order(BaseModel):
    id : int
    table_number : int
    items : Item
    total_price : int
    status : OrderState = OrderState.empty
