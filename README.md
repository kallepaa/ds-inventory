# ds-inventory service
Distributed Systems, Fall 2023

## Structure

* db contains SQLite database files
* domain contains domain logic
* migrate_scripts contains SQL files to create and upgrade database
* app.py is service start entry point. It contains topic subscriptions
* _config_sample is configuration file example. Should be copied and named as config.py
* migrate.py runs database migration
* test.py contains simple component test

## Visual Studio Code

Setup Flask to Visual Studio Code

https://code.visualstudio.com/docs/python/tutorial-flask

Install from requirements file

```console
pip install -r requirements.txt
```

## Migrate databse

python3 migrate.py

## Run Tests

python3 test.py

### Run service

```console
python3 -m flask run --host=0.0.0.0 --port=8081
```

## Public API

### List inventory

```console
wget -qO - http://svm-11-2.cs.helsinki.fi:8081/inventory
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