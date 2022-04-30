import pdb
from models.brand import Brand
from models.supplier import Supplier
from models.product import Product

import repositories.brand_repository as brand_repository
import repositories.supplier_repository as supplier_repository
import repositories.product_repository as product_repository

brand_repository.delete_all()
supplier_repository.delete_all()
product_repository.delete_all()

brand1 = Brand("Stanley")
brand_repository.save(brand1)

brand2 = Brand("Silverline")
brand_repository.save(brand2)

brand3 = Brand("Guff")
brand_repository.save(brand3)

supplier1 = Supplier("Stax", "0141 111 1111", 50)
supplier_repository.save(supplier1)

supplier2 = Supplier("CPC", "0151 222 2222", 100)
supplier_repository.save(supplier2)

supplier3 = Supplier("Toolstream", "0161 333 3333", 50)
supplier_repository.save(supplier3)


product1 = Product("Tape Measure", 20, 6, 5, 9, supplier3, brand2)
product_repository.save(product1)

product2 = Product("Tape Measure", 8, 3, 7, 12, supplier1, brand1)
product_repository.save(product2)

product3 = Product("Hammer", 4, 0, 4, 10, supplier1, brand3)
product_repository.save(product3)

product4 = Product("Hammer", 2, 1, 8, 15, supplier1, brand2)
product_repository.save(product4)

product5 = Product("Saw", 3, 2, 9, 18, supplier3, brand2)
product_repository.save(product5)

product6 = Product("Saw", 2, 0, 5, 11, supplier2, brand3)
product_repository.save(product6)

product7 = Product("Saw", 0, 2, 14, 25, supplier3, brand1)
product_repository.save(product7)

product8 = Product("Knife", 10, 5, 1, 4, supplier1, brand3)
product_repository.save(product8)

product9 = Product("Knife", 20, 10, 3, 8, supplier3, brand2)
product_repository.save(product9)

product10 = Product("Knife", 5, 3, 5, 12, supplier1, brand1)
product_repository.save(product10)

product11 = Product("Pliers", 0, 3, 2, 4, supplier3, brand3)
product_repository.save(product11)

product12 = Product("Pliers", 10, 5, 3, 5, supplier2, brand2)
product_repository.save(product12)

product13 = Product("wrench", 3, 3, 9, 16, supplier1, brand1)
product_repository.save(product13)

product14 = Product("Drill Bits", 3, 2, 10, 25, supplier1, brand1)
product_repository.save(product14)

product15 = Product("Drill Bits", 3, 0, 17, 25, supplier2, brand1)
product_repository.save(product15)








