from db.run_sql import run_sql

from models.brand import Brand
from models.product import Product
from models.supplier import Supplier 

def save(supplier):
    sql = "INSERT INTO suppliers (name, contact, carraige_paid) VALUES (%s, %s, %s) RETURNING *"
    values = [supplier.name, supplier.contact, supplier.carraige_paid]
    results = run_sql(sql, values)
    id = results[0]['id']
    supplier.id = id
    return supplier

def select_all():
    suppliers = []

    sql = "SELECT * FROM suppliers ORDER BY name"
    results = run_sql(sql)

    for row in results:
        supplier = Supplier(row['name'], row['contact'], row['carraige_paid'], row['id'] )
        suppliers.append(supplier)
    return suppliers

def select(id):
    supplier = None
    sql = "SELECT * FROM suppliers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]   

    if result is not None:
        supplier = Supplier(result['name'], result['contact'], result['carraige_paid'], result['id'])
    return supplier


def delete_all():
    sql = "DELETE FROM suppliers"
    run_sql(sql)       
    
def update(supplier):
    sql = "UPDATE suppliers SET (name, contact, carraige_paid ) = (%s, %s, %s) WHERE id = %s"
    values = [supplier.name, supplier.contact, supplier.carraige_paid, supplier.id]
    print(values)
    run_sql(sql, values)    

def delete(id):
    sql = "DELETE FROM suppliers WHERE id = %s"       
    values = [id]
    run_sql(sql, values)    