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

    def get_details(self):
        return f"{self.type} {self.brand.name} {self.in_stock}"
        
    # low stock method and get mark up method

    def calculate_mark_up(self):
        mark_up = 100 * (self.selling_price - self.buying_price) / self.buying_price

        #attempt to round up to 2 decimal places. nothing displays
        # mark_up = 100 * (self.selling_price - self.buying_price) / self.buying_price
        # mark_up_round = round(mark_up, 2) 
        # return mark_up_round

    def stock_level(self):

        if self.in_stock == 0:
            return "No Stock"

        elif self.in_stock <= self.low_stock_threshold:
            return "Low Stock"
       
        else: 
            return "in Stock"    




