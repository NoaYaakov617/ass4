
import sqlite3
import  os
import atexit
import sys

DBExist = os.path.isfile('database.db')
if DBExist:
    os.remove('database.db')


_conn = sqlite3.connect('database.db')
cur = _conn.cursor()

def _close_db(): # no need?
    _conn.commit()
    _conn.close()


atexit.register(_close_db)



# DTO Objects

class Vaccine:
    def __init__(self, id, date, supplier, quantity):
        self.id = id
        self.date = date
        self.supplier = supplier
        self.quantity = quantity


class Supplier:
    def __init__(self, id, name, logistics):
        self.id = id
        self.name = name
        self.logistics = logistics


class Clinic:
    def __init__(self, id, location, demand, logistics ):
        self.id = id
        self.location = location
        self.demand = demand
        self.logistics = logistics


class Logistic:
    def __init__(self, id, name, count_sent, count_received):
        self.id = id
        self.name = name
        self.count_sent = count_sent
        self.count_received = count_received


      # DAO

class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""
               INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
           """, [vaccine.id,vaccine.date,vaccine.supplier,vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines WHERE id = ?
        """, [vaccine_id])
        return Vaccine(*c.fetchone())

    def get_sum_quantity(self):
        c = self._conn.cursor()
        c.execute("""SELECT SUM (quantity) FROM vaccines """";)
        return

class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
                INSERT INTO suppliers (id, name, logistics) VALUES (?, ?, ?)
        """, [supplier.id,supplier.name,supplier.logistics])

    def find(self, name):
        c = self._conn.cursor()
        c.execute("""
                SELECT id,name,logistics FROM suppliers WHERE name = ?
            """, [name])

        return Supplier(*c.fetchone())

class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
            INSERT INTO clinics (id, location, demand, logistics) VALUES (?, ?, ?, ?)
        """, [clinic.id, clinic.location,clinic.demand,clinic.logistics])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                 SELECT id,location,demand, logistics FROM clinics WHERE id = ?
             """, [id])

        return Supplier(*c.fetchone())

class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
            INSERT INTO logistics (id, name, count_sent, count_ received) VALUES (?, ?, ?, ?)
         """, [logistic.id,logistic.name,logistic.count_sent,logistic.count_received])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
                 SELECT id,name,count_sent, count_received FROM logistics WHERE id = ?
             """, [id])
        return Logistic(*c.fetchone())

    def update_count_received(id, new_quantity):
        cur.execute("""UPDATE Products SET quantity=? WHERE id=?""", [new_quantity, id])

    #Repository
class _Repository:
    def __init__(self):
        self._conn = sqlite3.connect('database.db')
        self.vaccines = _Vaccines(self._conn)
        self.suppliers = _Suppliers(self._conn)
        self.clinics = _Clinics(self._conn)
        self.logistics = _Logistics(self._conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()


def create_tables(self):
    self._conn.executescript("""
        CREATE TABLE vaccines (
            id       INT         PRIMARY KEY,
            date     TEXT        NOT NULL,
            supplier INT         NOT NULL,
            quantity INT         NOT NULL,
            
            FOREIGN KEY(supplier)     REFERENCES suppliers(id),
        );

        CREATE TABLE suppliers (
            id         INT     PRIMARY KEY,
            name       TEXT    NOT NULL
            logistic   INT     NOT NULL,
            
            FOREIGN KEY(logistic)     REFERENCES Logistic(id),
            
        );
        

        CREATE TABLE clinics (
            id        INT     PRIMARY KEY,
            location  TEXT    NOT NULL,
            demand    INT     NOT NULL,
            logistic  INT     NOT NULL,

            FOREIGN KEY(logistic)    REFERENCES Logistics(id),
            
        );
        
        CREATE TABLE logistics (
            id                INT     PRIMARY KEY,
            name              TEXT    NOT NULL,
            count_sent        INT     NOT NULL,
            count_received    INT     NOT NULL,
     
            
        );
    """)

def parse_config(file_name):
      config_file = open(file_name)
      first_line_data = config_file.readline().split(",")
      vaccines_num = first_line_data[0]
      supplier_num = first_line_data[1]
      clinics_num = first_line_data[2]
      logistics_num = first_line_data[3];



      for line in config_file:
        data = line.split(",")

        if(0 <  vaccines_num)
          vaccine_id = data[0].strip()
          vaccine_date = data[1].strip()
          vaccine_supplier = data[2].strip()
          vaccine_quantity = data[3].strip()
          _Vaccines.insert(vaccine_id,vaccine_date,vaccine_supplier,vaccine_quantity)

        if(0 < supplier_n






def main(args):
    repo = _Repository()
    repo.create_tables()
    parse_config(args[1])

if __name__ == '__main__':
        main(sys.argv)










