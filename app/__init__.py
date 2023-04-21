"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13b88rddl13a563tkg-a.oregon-postgres.render.com",
        database="todo_ed6w",
        user="todo_ed6w_user",
        password="xVwQiUrAXo1deZADeIKRtcV7fTpNdCHb")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
