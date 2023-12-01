from flask import Flask
from flask_mqtt import Mqtt
import domain.domain_logic as dl
import config
from domain.order import Order, OrderCancel

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = config.mqtt_host  # use the free broker from HIVEMQ
app.config['MQTT_BROKER_PORT'] = config.mqtt_port  # default port for non-tls connection
app.config['MQTT_USERNAME'] = config.mqtt_username  # set the username here if you need authentication for the broker
app.config['MQTT_PASSWORD'] = config.mqtt_password  # set the password here if the broker demands authentication
app.config['MQTT_KEEPALIVE'] = 60  # set the time interval for sending a ping to the broker to 5 seconds
app.config['MQTT_TLS_ENABLED'] = False  # set TLS to disabled for testing purposes

mqtt = Mqtt(app)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("flask mqtt connected")
    mqtt.subscribe(config.mqtt_topic_on_order_send, qos=1) #qos 1 makes sure that message is received least once, but may receive more than once
    mqtt.subscribe(config.mqtt_topic_on_order_canceled, qos=1)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )

    if data['topic'] == config.mqtt_topic_on_order_send:
        print(data['payload'])
        dl.OrderSend(Order.from_json(data['payload']))
    elif data['topic'] == config.mqtt_topic_on_order_canceled:
        print(data['payload'])
        dl.OrderCancel(OrderCancel.from_json(data['payload']))

@app.route("/")
def Get():
    return dl.ListInventory()