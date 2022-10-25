import unittest
from models.product import Product

class TestProduct(unittest.TestCase):
    
    def setUp(self):
        self.product = Product("Batteries", 5, 3, 2, 6, "Stax", "Silverline", None)
        
    
    def test_product_has_type(self):
        self.assertEqual("Batteries", self.product.type)