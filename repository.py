from inventory import Inventory
from typing import List
import sqlite3
import config
from sqlite3 import Error
from order import Order

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

def HasOrderExistingReservation(order_id: str)->bool:
    #check reservations
    conn = create_connection(config.db)
    if conn:
        try:
            cursor = conn.execute("SELECT EXISTS(SELECT 1 FROM reservation WHERE order_id=?);", (order_id, ))
            for row in cursor:
                return row[0] == 1
        finally:
            conn.close()

def CheckAvailability(inventory_id: int, count : int)->bool:
    conn = create_connection(config.db)
    if conn:
        try:
            cursor = conn.execute("SELECT EXISTS(SELECT 1 FROM inventory where id=? and balance >=?);", (inventory_id, count))
            for row in cursor:
                return row[0] == 1
        finally:
            conn.close()

def ReserveProduct(order: Order):
    conn = create_connection(config.db)
    if conn:
        try:
            for item in order.items:
                conn.execute("UPDATE inventory set balance = balance - ? where id = ?;", (item.count, item.inventory_id))
                conn.execute("INSERT INTO reservation (reserved, inventory_id, order_id) values(?,?,?);", (item.count, item.inventory_id, order.order_id))            
            conn.commit()
        finally:
            conn.close()
    return

def ReleaseReservation(order_id)->bool:
    conn = create_connection(config.db)
    if conn:
        try:
            cursor = conn.execute("SELECT id, reserved, inventory_id FROM reservation where order_id=?;", (order_id,))
            for row in cursor:
                id, reserved, inventory_id = row
                conn.execute("UPDATE inventory SET balance = balance + ? where id=?", (reserved, inventory_id))
                conn.execute("DELETE FROM reservation WHERE id=?;", (id, ))            
            conn.commit()
        finally:
            conn.close()
    return

def ListInventory()->List[Inventory]:
    ret = []
    conn = create_connection(config.db)
    if conn:
        try:
            cursor = conn.execute("SELECT id, product_name, price, balance FROM inventory;")
            for row in cursor:
                ret.append(Inventory(row[0], row[1], row[2], row[3]))
        finally:
            conn.close()            
    return ret
    
def AddBalance(inventory_id : int, count: int):
    conn = create_connection(config.db)
    if conn:
        try:
            conn.execute("UPDATE inventory set balance = balance + ? where id = ?;", (count, inventory_id))
            conn.commit()
        finally:
            conn.close()
    return