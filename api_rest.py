# coding=utf-
from flask import Flask
from pymongo import MongoClient

import json

from settings import *


app = Flask(__name__)

CLIENT = MongoClient()
DB = CLIENT[DATABASE]


@app.route('/api/<resource>', methods=['GET'])
def get_resource(resource):
    try:
        collection = DB[resource]
    except Exception as e:
        print("THis resource not exist %s" % e)
        raise

    json_data = []

    for item in collection.find():
        for key, val in item.items():
            if not isinstance(item[key], str):
                item[key] = str(val)
        json_data.append(item)

    return json.dumps(json_data)


if __name__ == '__main__':
    app.debug = True
    app.run(IP_HOST, PORT_HOST)
