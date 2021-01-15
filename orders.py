import sqlite3
import atexit
import sys
import summary
from initiate import _Repository

_conn = sqlite3.connect('database.db')
_conn.text_factory = str
cur = _conn.cursor()

repo = _Repository()


def _close_db():
    _conn.commit()
    _conn.close()
    summary.main()


atexit.register(_close_db)






def parse_orders(file_name):
    orders_file = open(file_name)
    for line in orders_file:
        order = line.split(",")

        if len(order) == 3:
            receive_shipment (order[0],order[1],order[2])

        else:
            sent_shipment(order[0],order[1])


def receive_shipment (name,amount,date):
    supplier = repo.suppliers.find(name)
    id_supplier = supplier.id
    repo.vaccines.insert(date,id_supplier,amount)
    new_quantity = repo.logistics.find(supplier.logistics).count_received + amount
    repo.logistics.update_count_received(supplier.logistics,new_quantity)


def sent_shipment(location,amount):


def total_inventory:









