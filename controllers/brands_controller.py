from flask import Flask, render_template, request, redirect
from flask import Blueprint 
from models.brand import Brand
import repositories.brand_repository as brand_repository

brands_blueprint = Blueprint("brands", __name__)

@brands_blueprint.route("/brands")
def brands():
    brands = brand_repository.select_all()
    return render_template("brands/index.html", all_brands = brands)

    # NEW
# GET '/brands/new'  I DON'T KNOW IF I WANT THE ROUTES TO BE AS THEY ARE. 

@brands_blueprint.route("/brands/new", methods=['GET'])
def new_brand():
    return render_template("brands/new.html")
    


# CREATE
# POST '/brands'
@brands_blueprint.route("/brands", methods=['POST'])
def create_brand():
    name = request.form['name']
    brand = Brand(name)
    brand_repository.save(brand)
    return redirect('/brands')






# SHOW
# GET '/brands/<id>'

# EDIT
# GET '/brands/<id>/edit'


# UPDATE
# PUT '/brands /<id>'


# DELETE
# DELETE '/books/<id>'

