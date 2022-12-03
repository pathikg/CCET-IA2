from influxdb import InfluxDBClient
import random
import datetime
import time

INFLUXDB_HOST = 'localhost'
INFLUXDB_NAME = 'ccet-ia2'

fixed_interval = 0.5

while 1:
    timestamp = datetime.datetime.utcnow().isoformat()
    sensor1 = random.randint(0, 10)
    sensor2 = random.randint(450, 500)
    sensor3 = random.randint(30, 40)
    sensor4 = random.randint(0, 100)
    sensor5 = random.randint(20, 60)
    sensor6 = random.randint(50, 70)
    sensor7 = random.randint(100, 500)
    sensor8 = random.randint(0, 50)
    sensor9 = random.randint(200, 300)
    sensor10 = random.randint(100, 500)
    sensor11 = random.randint(0, 80)
    sensor12 = random.randint(45, 50)
    sensor13 = random.randint(30, 50)
    sensor14 = random.randint(0, 500)
    sensor15 = random.randint(500, 600)
    sensor16 = random.randint(750, 900)
    sensor17 = random.randint(40, 100)
    sensor18 = random.randint(1000, 1500)
    sensor19 = random.randint(0, 5)
    sensor20 = random.randint(5, 20)

    error_string = ""
    client = InfluxDBClient(INFLUXDB_HOST, '8086', 'admin', 'admin', INFLUXDB_NAME)
    

    json_data = [
        {
            "measurement": "device_1",
            "time": timestamp,
            "tags": {
                "Node": "Node_1"
            },
            "fields": {
                "Sensor_1": sensor2,
                "Sensor_2": sensor1,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_1",
            "time": timestamp,
            "tags": {
                "Node": "Node_2"
            },
            "fields": {
                "Sensor_1": sensor1,
                "Sensor_2": sensor2,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor6,
                "Sensor_7": sensor7,
                "Sensor_8": sensor8,
                "Sensor_9": sensor9,
                "Sensor_10": sensor10,
                "Sensor_11": sensor11,
                "Sensor_12": sensor12,
                "Sensor_13": sensor13,
                "Sensor_14": sensor14,
                "Sensor_15": sensor15,
                "Sensor_16": sensor16,
                "Sensor_17": sensor17,
                "Sensor_18": sensor18,
                "Sensor_19": sensor19,
                "Sensor_20": sensor20
            }
        },
        {
            "measurement": "device_1",
            "time": timestamp,
            "tags": {
                "Node": "Node_3"
            },
            "fields": {
                "Sensor_1": sensor9,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor13,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor18,
                "Sensor_19": sensor15,
                "Sensor_20": sensor17
            }
        },
        {
            "measurement": "device_1",
            "time": timestamp,
            "tags": {
                "Node": "Node_4"
            },
            "fields": {
                "Sensor_1": sensor5,
                "Sensor_2": sensor20,
                "Sensor_3": sensor18,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor16,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_1",
            "time": timestamp,
            "tags": {
                "Node": "Node_5"
            },
            "fields": {
                "Sensor_1": sensor20,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor14,
                "Sensor_5": sensor15,
                "Sensor_6": sensor19,
                "Sensor_7": sensor17,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor1,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor5,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_2",
            "time": timestamp,
            "tags": {
                "Node": "Node_2"
            },
            "fields": {
                "Sensor_1": sensor2,
                "Sensor_2": sensor1,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_2",
            "time": timestamp,
            "tags": {
                "Node": "Node_1"
            },
            "fields": {
                "Sensor_1": sensor1,
                "Sensor_2": sensor2,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor6,
                "Sensor_7": sensor7,
                "Sensor_8": sensor8,
                "Sensor_9": sensor9,
                "Sensor_10": sensor10,
                "Sensor_11": sensor11,
                "Sensor_12": sensor12,
                "Sensor_13": sensor13,
                "Sensor_14": sensor14,
                "Sensor_15": sensor15,
                "Sensor_16": sensor16,
                "Sensor_17": sensor17,
                "Sensor_18": sensor18,
                "Sensor_19": sensor19,
                "Sensor_20": sensor20
            }
        },
        {
            "measurement": "device_2",
            "time": timestamp,
            "tags": {
                "Node": "Node_5"
            },
            "fields": {
                "Sensor_1": sensor9,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor13,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor18,
                "Sensor_19": sensor15,
                "Sensor_20": sensor17
            }
        },
        {
            "measurement": "device_2",
            "time": timestamp,
            "tags": {
                "Node": "Node_3"
            },
            "fields": {
                "Sensor_1": sensor5,
                "Sensor_2": sensor20,
                "Sensor_3": sensor18,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor16,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_2",
            "time": timestamp,
            "tags": {
                "Node": "Node_4"
            },
            "fields": {
                "Sensor_1": sensor20,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor14,
                "Sensor_5": sensor15,
                "Sensor_6": sensor19,
                "Sensor_7": sensor17,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor1,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor5,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_3",
            "time": timestamp,
            "tags": {
                "Node": "Node_5"
            },
            "fields": {
                "Sensor_1": sensor2,
                "Sensor_2": sensor1,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_3",
            "time": timestamp,
            "tags": {
                "Node": "Node_4"
            },
            "fields": {
                "Sensor_1": sensor1,
                "Sensor_2": sensor2,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor6,
                "Sensor_7": sensor7,
                "Sensor_8": sensor8,
                "Sensor_9": sensor9,
                "Sensor_10": sensor10,
                "Sensor_11": sensor11,
                "Sensor_12": sensor12,
                "Sensor_13": sensor13,
                "Sensor_14": sensor14,
                "Sensor_15": sensor15,
                "Sensor_16": sensor16,
                "Sensor_17": sensor17,
                "Sensor_18": sensor18,
                "Sensor_19": sensor19,
                "Sensor_20": sensor20
            }
        },
        {
            "measurement": "device_3",
            "time": timestamp,
            "tags": {
                "Node": "Node_3"
            },
            "fields": {
                "Sensor_1": sensor9,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor13,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor18,
                "Sensor_19": sensor15,
                "Sensor_20": sensor17
            }
        },
        {
            "measurement": "device_3",
            "time": timestamp,
            "tags": {
                "Node": "Node_2"
            },
            "fields": {
                "Sensor_1": sensor5,
                "Sensor_2": sensor20,
                "Sensor_3": sensor18,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor16,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_3",
            "time": timestamp,
            "tags": {
                "Node": "Node_1"
            },
            "fields": {
                "Sensor_1": sensor20,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor14,
                "Sensor_5": sensor15,
                "Sensor_6": sensor19,
                "Sensor_7": sensor17,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor1,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor5,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_4",
            "time": timestamp,
            "tags": {
                "Node": "Node_4"
            },
            "fields": {
                "Sensor_1": sensor2,
                "Sensor_2": sensor1,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_4",
            "time": timestamp,
            "tags": {
                "Node": "Node_1"
            },
            "fields": {
                "Sensor_1": sensor1,
                "Sensor_2": sensor2,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor6,
                "Sensor_7": sensor7,
                "Sensor_8": sensor8,
                "Sensor_9": sensor9,
                "Sensor_10": sensor10,
                "Sensor_11": sensor11,
                "Sensor_12": sensor12,
                "Sensor_13": sensor13,
                "Sensor_14": sensor14,
                "Sensor_15": sensor15,
                "Sensor_16": sensor16,
                "Sensor_17": sensor17,
                "Sensor_18": sensor18,
                "Sensor_19": sensor19,
                "Sensor_20": sensor20
            }
        },
        {
            "measurement": "device_4",
            "time": timestamp,
            "tags": {
                "Node": "Node_2"
            },
            "fields": {
                "Sensor_1": sensor9,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor13,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor18,
                "Sensor_19": sensor15,
                "Sensor_20": sensor17
            }
        },
        {
            "measurement": "device_4",
            "time": timestamp,
            "tags": {
                "Node": "Node_3"
            },
            "fields": {
                "Sensor_1": sensor5,
                "Sensor_2": sensor20,
                "Sensor_3": sensor18,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor16,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_4",
            "time": timestamp,
            "tags": {
                "Node": "Node_5"
            },
            "fields": {
                "Sensor_1": sensor20,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor14,
                "Sensor_5": sensor15,
                "Sensor_6": sensor19,
                "Sensor_7": sensor17,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor1,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor5,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_5",
            "time": timestamp,
            "tags": {
                "Node": "Node_2"
            },
            "fields": {
                "Sensor_1": sensor2,
                "Sensor_2": sensor1,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_5",
            "time": timestamp,
            "tags": {
                "Node": "Node_4"
            },
            "fields": {
                "Sensor_1": sensor1,
                "Sensor_2": sensor2,
                "Sensor_3": sensor3,
                "Sensor_4": sensor4,
                "Sensor_5": sensor5,
                "Sensor_6": sensor6,
                "Sensor_7": sensor7,
                "Sensor_8": sensor8,
                "Sensor_9": sensor9,
                "Sensor_10": sensor10,
                "Sensor_11": sensor11,
                "Sensor_12": sensor12,
                "Sensor_13": sensor13,
                "Sensor_14": sensor14,
                "Sensor_15": sensor15,
                "Sensor_16": sensor16,
                "Sensor_17": sensor17,
                "Sensor_18": sensor18,
                "Sensor_19": sensor19,
                "Sensor_20": sensor20
            }
        },
        {
            "measurement": "device_5",
            "time": timestamp,
            "tags": {
                "Node": "Node_3"
            },
            "fields": {
                "Sensor_1": sensor9,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor13,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor18,
                "Sensor_19": sensor15,
                "Sensor_20": sensor17
            }
        },
        {
            "measurement": "device_5",
            "time": timestamp,
            "tags": {
                "Node": "Node_5"
            },
            "fields": {
                "Sensor_1": sensor5,
                "Sensor_2": sensor20,
                "Sensor_3": sensor18,
                "Sensor_4": sensor4,
                "Sensor_5": sensor15,
                "Sensor_6": sensor9,
                "Sensor_7": sensor7,
                "Sensor_8": sensor10,
                "Sensor_9": sensor16,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor11,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor13,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor15,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "device_5",
            "time": timestamp,
            "tags": {
                "Node": "Node_1"
            },
            "fields": {
                "Sensor_1": sensor20,
                "Sensor_2": sensor11,
                "Sensor_3": sensor13,
                "Sensor_4": sensor14,
                "Sensor_5": sensor15,
                "Sensor_6": sensor19,
                "Sensor_7": sensor17,
                "Sensor_8": sensor10,
                "Sensor_9": sensor17,
                "Sensor_10": sensor12,
                "Sensor_11": sensor16,
                "Sensor_12": sensor18,
                "Sensor_13": sensor1,
                "Sensor_14": sensor14,
                "Sensor_15": sensor19,
                "Sensor_16": sensor1,
                "Sensor_17": sensor20,
                "Sensor_18": sensor8,
                "Sensor_19": sensor5,
                "Sensor_20": sensor7
            }
        },
        {
            "measurement": "Error",
            "time": timestamp,
            "fields": {
                "Node_1": "",
                "Node_2": "",
                "Node_3": "",
                "Node_4": "",
                "node_5": ""
            }
        }
    ]
    bResult = client.write_points(json_data)
    print("Result of Write Data : ", bResult)
    time.sleep(fixed_interval)
