import repository
import domain_logic
from order import Order, OrderItem
import uuid
from typing import List

inventory = domain_logic.ListInventory()

print(inventory)

for inv in inventory:
    repository.AddBalance(inv.id, 10)

inventory = domain_logic.ListInventory()
print(inventory)


order_id = str(uuid.uuid4())

items = []

for inv in inventory:
    items.append(OrderItem(inv.id, 10))

domain_logic.OrderSend(Order(order_id, items))

inventory = domain_logic.ListInventory()
print(inventory)

domain_logic.OrderCanceled(order_id)

print(domain_logic.ListInventory())




