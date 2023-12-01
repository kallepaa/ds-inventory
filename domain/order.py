from dataclasses import dataclass
from typing import List

@dataclass
class OrderItem():
    inventory_id: int
    count : int

@dataclass
class Order():
    order_id: str
    items : List[OrderItem]
