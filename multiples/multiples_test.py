import unittest

from multiples import *

class TestMultiples(unittest.TestCase):
    
    def test_multiples(self):
        self.assertEqual(0, multiples())
        