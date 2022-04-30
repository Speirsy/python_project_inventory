from db.run_sql import run_sql

from models.brand import Brand
from models.product import Product
from models.supplier import Supplier 

def save(brand):
    sql = "INSERT INTO brands (name) VALUES (%s) RETURNING *"
    values = [brand.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    brand.id = id
    return brand

def select_all():
    brands = []

    sql = "SELECT * FROM brands"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['id'] )
        brands.append(brand)
    return brands


def delete_all():
    sql = "DELETE  FROM brands"
    run_sql(sql)    