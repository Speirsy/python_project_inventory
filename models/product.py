class Product:

    def __init__(self, type, in_stock, low_stock_threshold, buying_price, selling_price, supplier, brand, id = None):
        self.type = type
        self.in_stock = in_stock
        self.low_stock_threshold = low_stock_threshold
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.supplier = supplier
        self.brand = brand
        self.id = id

        
