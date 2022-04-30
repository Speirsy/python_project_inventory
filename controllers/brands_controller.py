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
# GET '/brands/new'


# CREATE
# POST '/brands'



# SHOW
# GET '/brands/<id>'

# EDIT
# GET '/brands/<id>/edit'


# UPDATE
# PUT '/brands /<id>'


# DELETE
# DELETE '/books/<id>'

