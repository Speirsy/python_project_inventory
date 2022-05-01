from click import edit
from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.supplier import Supplier
import repositories.supplier_repository as supplier_repository

suppliers_blueprint = Blueprint("suppliers", __name__)

# INDEX
# GET '/suppliers

@suppliers_blueprint.route("/suppliers")
def suppliers():
    suppliers = supplier_repository.select_all()
    return render_template("suppliers/index.html", all_suppliers = suppliers)

# NEW
# GET '/suppliers/new'  not sure about these paths

@suppliers_blueprint.route("/suppliers/new", methods=['GET'])
def new_supplier():

    return render_template("suppliers/new.html")

# CREATE
# POST '/suppliers'
@suppliers_blueprint.route("/suppliers", methods=['POST'])
def create_supplier():
    name = request.form['name']
    contact = request.form['contact']
    carraige_paid = request.form['carraige_paid']
    supplier = Supplier(name, contact, carraige_paid)
    supplier_repository.save(supplier)
    return redirect('/suppliers')
    
#SHOW
#GET '/suppliers/<id>

@suppliers_blueprint.route("/suppliers/<id>", methods=['GET'])    
def show_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('supplier/show.html', supplier = supplier)

# EDIT
#GET '/suppliers/<id>/edit

@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'] )
def edit_supplier(id):
    supplier = supplier_repository.select(id)
    return render_template('suppliers/edit.html', supplier = supplier)


# UPDATE
#PUT'/suppliers/<id>

@suppliers_blueprint.route("/suppliers/<id>", methods=['POST'])
def update_suppliers(id):
    name = request.form['name']
    contact = request.form['contact']
    carraige_paid = request.form['carraige_paid']
    supplier = Supplier(name, contact, carraige_paid, id)
    supplier_repository.update(supplier)
    return redirect('/suppliers')


# DELETE
# DELETE '/WORKS/<ID>

@suppliers_blueprint.route("/supliers/<id>/delete", methods=['POST'])
def delete_suppliers(id):
    supplier_repository.delete(id)
    return redirect('/suppliers')



