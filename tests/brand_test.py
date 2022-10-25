import unittest
from models.brand import Brand

class TestBrand(unittest.TestCase):
    
    def setUp(self):
        self.brand = Brand("CheapCheap")
        
    
    def test_brand_has_name(self):
        self.assertEqual("CheapCheap", self.brand.name)
                        
                        
 
        