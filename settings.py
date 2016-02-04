# coding=utf-8

# FLASK VARS
IP_HOST = "0.0.0.0"
PORT_HOST = 5000

# MONGODB VARS
DATABASE = "opendata"

try:
    from local_settings import *
except Exception as e:
    pass
