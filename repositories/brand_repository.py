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

    sql = "SELECT * FROM brands ORDER BY name"
    results = run_sql(sql)

    for row in results:
        brand = Brand(row['name'], row['id'] )
        brands.append(brand)
    return brands

def select(id):
    brand = None
    sql = "SELECT * FROM brands WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]   

    if result is not None:
        brand = Brand(result['name'], result['id'])
    return brand    

def update(brand):
    sql = "UPDATE brands SET (name) = (%s) WHERE id = %s"
    values = [brand.name, brand.id]
    print(values)


def delete_all():
    sql = "DELETE  FROM brands"
    run_sql(sql)    

def delete(id):
    sql = "DELETE FROM brands WHERE id = %s"       
    values = [id]
    run_sql(sql, values)        