from db.run_sql import run_sql

from models.product import Product
from models.supplier import Supplier
from models.brand import Brand

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.brand_repository as brand_repository

def save(product):
    sql = "INSERT INTO products (type, in_stock, low_stock_threshold, buying_price, selling_price, supplier_id, brand_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.type,
                product.in_stock,
                product.low_stock_threshold,
                product.buying_price,
                product.selling_price,
                product.supplier.id,
                product.brand.id
    ]

    results = run_sql(sql, values)
    id = results[0]['id']
    product.id = id
    return product

def select_all():
    products = []

    sql = "SELECT * FROM products"
    results = run_sql(sql)

    for row in results:
        brand = brand_repository.select(row['brand_id'])
        supplier = supplier_repository.select(row['supplier_id'])
        product = Product(row['type'], row['in_stock'], row['low_stock_threshold'], row['buying_price'], row['selling_price'], supplier, brand, row['id'])
        products.append(product)

    return product

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]   

    if result is not None:
        brand = brand_repository.select(result['brand_id'])
        supplier = supplier_repository.select(result['supplier_id'])
        product = Product(result['type'], result['in_stock'], result['low_stock_threshold'], result['buying_price'], result['selling_price'], supplier, brand, result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)   

def update(product):
    sql = "UPDATE products SET (type, in_stock, low_stock_threshold, buying_price, selling_price, supplier_id, brand_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.type, product.in_stock, product.low_stock_threshold, product.buying_price, product.selling_price, product.supplier.id, product.brand.id, product.id]
    print(values)
    run_sql(sql, values)          

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"       
    values = [id]
    run_sql(sql, values)














