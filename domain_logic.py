from order import Order
import repository
from typing import List
from inventory import Inventory
import paho.mqtt.publish as publish
import paho.mqtt.client as mqtt
import config 
from messages import InStock, OutOfStock

def ListInventory()->List[Inventory]:
    return repository.ListInventory()

def OrderSend(order: Order):
    
    if repository.HasOrderExistingReservation(order.order_id):
        return # Ignore possible dublicate silently

    for item in order.items:
        # try reservation
        available = repository.CheckAvailability(item.inventory_id, item.count)
        if not available:
            # Notify inventory not Ok
            __message_publish(config.mqtt_topic_out_of_stock, OutOfStock(order.order_id).to_json())
            return False

    # Reserve order products
    repository.ReserveProduct(order)
        # Notify inventory Ok 
    __message_publish(config.mqtt_topic_on_stock, InStock(order.order_id).to_json())

def OrderCanceled(order_id : str):
    repository.ReleaseReservation(order_id)
    return

def __message_publish(topic: str, payload: str):
    publish.single(
        topic, 
        payload=payload, 
        qos=1, #least once
        retain=False, 
        hostname=config.mqtt_host,
        port=config.mqtt_port, 
        client_id=config.mqtt_client_id, 
        auth= {'username' : config.mqtt_username, 'password' : config.mqtt_password}, 
        tls=None,
        protocol=mqtt.MQTTv5, transport=config.mqtt_transport)    