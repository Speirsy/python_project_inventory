from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository
import repositories.brand_repository as brand_repository

products_blueprint = Blueprint("products", __name__)

# GET '/products/new'

@products_blueprint.route("/products")
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", all_products = products)


@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    suppliers = supplier_repository.select_all()
    brands = brand_repository.select_all()
    return render_template("products/new.html", all_suppliers = suppliers, all_brands = brands)

    # CREATE POST '/products'

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    type = request.form['type']
    in_stock = request.form['in_stock']
    low_stock_threshold = request.form['low_stock_threshold']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    supplier = supplier_repository.select(request.form['supplier_id'])
    brand = brand_repository.select(request.form['brand_id'])
    product = Product(type, in_stock, low_stock_threshold, buying_price, selling_price, supplier, brand)
    product_repository.save(product)
    return redirect('/products')

# SHOW
# GET '/products/<id>'

@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template('products/show.html', product = product)

# EDIT
# PUT '/products/<id>

# not sure about this function. edit? is it workking with update? 

@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    brands = brand_repository.select_all()
    suppliers = supplier_repository.select_all()
    return render_template('products/edit.html', product = product, all_brands = brands, all_suppliers = suppliers) 


# UPDATE  
# do I need PRINT statements somewhere here?

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    type = request.form['type']
    in_stock = request.form['in_stock']
    low_stock_threshold = request.form['low_stock_threshold']
    buying_price = request.form['buying_price']
    selling_price = request.form['selling_price']
    supplier = supplier_repository.select(request.form['supplier_id'])
    brand = brand_repository.select(request.form['brand_id'])
    product = Product(type, in_stock, low_stock_threshold, buying_price, selling_price, supplier, brand, id)
    product_repository.update(product)
    return redirect('/products')


# DELETE '/products/<id>

@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')


