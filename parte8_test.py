import unittest
from parte8 import variazione_media

class Test(unittest.TestCase):
    def test(self):
        array = [1,1,1,1,1,1,1]
        self.assertEqual(variazione_media(array, 3), 0)
    
    def test2(self):
        array = [2,-2,-1,0,1,2,3]
        self.assertEqual(variazione_media(array, 3), 1)