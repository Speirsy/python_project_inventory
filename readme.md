# Shop Inventory App

A small hardware retailer wants to automate his stock inventory. He wishes to log all his products by type (hammer, paint, screws..), by each items Brand name (Stanley, Dulux..) and by Supplier or wholesaler from where they have been purchased. 

# MVP

The user should be able to

- view a full list of store products associated data - Supplier, Brand, Stock Level, Cost, Mark Up, and links to an edit page for changes and adds. 
- view a full list of Suppliers with links for individual edits and a button to add more.
- view a full list of Brands with links for edits and a button to add more.
- enter purchase and sale price for each product and view mark up as a percentage. 
- view low stock and out of stock indicators for each product. 

## Extensions achieved

- set a low stock indicator threshold for each individual product 


## Next steps

Add css to improve the look and feel of the app.


# Further Extensions 

The user would like to

- order products from suppliers with "carraige paid" being met a priority. Thus a purchase order totaliser / calculator where products are selected to break through the carraige paid of the supplier. The aim being to save on delivery charges.
- view all store products from a specific supplier.
- view all store products by brand.

# Installation


This application requires jinja2, postgreSQL and python 3 installed in your IDE.

- to run the program, 
    
    in terminal, type

    flask run 

    or

    python3 app.py

-   command + click on http://127.0.0.1:5000 or similar to open in your browser.









