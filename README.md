# ds-inventory service
Distributed Systems, Fall 2023

## Visual Studio Code

Setup Flask to Visual Studio Code

https://code.visualstudio.com/docs/python/tutorial-flask

Install from requirements file

```console
pip install -r requirements.txt
```

## Migrate databse

python migrate.py

## Run Tests

python3 test.py

### Run service

```console
python3 -m flask run --host=0.0.0.0 --port=8081
```

## Public API

### List inventory

```console
wget -qO - http://svm-11.cs.helsinki.fi:8081/
```


Response

```json
[
    {
        "balance": 171,
        "id": 1,
        "price": 1000,
        "product_name": "One Leg Web Shop Prototype"
    },
    {
        "balance": 173,
        "id": 2,
        "price": 2000,
        "product_name": "One Leg Web Shop Prototype v 2.0"
    }
]
```

## Messaging

Console
https://el6icz3en0fo-scdyi8ws59yk.cedalo.dev/

MQTT Endpoint Address: mqtt://el6icz3en0fo-scdyi8ws59yk.cedalo.dev:1883

## Outgoing messages 

### InStock

topic: inventory/on-stock

```json
{"orderId": "61161883-f796-4405-ac07-263190466f40"}
```

### OutOfStock

topic: inventory/out-of-stock

```json
{"orderId": "61161883-f796-4405-ac07-263190466f40"}
```

## Incoming messages

### Order

topic: public-front/order-send

```json
{"orderId": "32449a83-8351-45e0-b0ba-082f7cc20d25", "items": [{"inventoryId": 1, "count": 10}, {"inventoryId": 2, "count": 10}]}
```

### OrderCanceled

topic: order/order-canceled

```json
{"orderId": "61161883-f796-4405-ac07-263190466f40"}
```

## Notes

Python tutorial
https://www.hivemq.com/blog/mqtt-essentials-part-6-mqtt-quality-of-service-levels/
https://pypi.org/project/paho-mqtt/
https://cedalo.com/blog/configuring-paho-mqtt-python-client-with-examples/
https://pypi.org/project/Flask-MQTT/
https://flask-mqtt.readthedocs.io/en/latest/usage.html#configure-the-mqtt-client

Python Requirements
https://learnpython.com/blog/python-requirements-file/

Create requirements file
pip freeze > requirements.txt

Install from requirements file
pip install -r requirements.txt

Configuration File
https://janakiev.com/blog/python-credentials-and-configuration/
