from domain import repository as repo
from domain import domain_logic as dl
from domain.order import Order, OrderItem
import uuid
from typing import List
import config
from migrate import Migrate

config.db = config.db_test
mg = Migrate(config.db_test, config.db_migrate)
mg.migrate()

inventory = dl.ListInventory()

print(inventory)

for inv in inventory:
    repo.AddBalance(inv.id, 10)

inventory = dl.ListInventory()
print(inventory)


order_id = str(uuid.uuid4())

items = []

for inv in inventory:
    items.append(OrderItem(inv.id, 10))

dl.OrderSend(Order(order_id, items))

inventory = dl.ListInventory()
print(inventory)

dl.OrderCanceled(order_id)

print(dl.ListInventory())




