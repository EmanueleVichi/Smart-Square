"""Test square"""
import unittest
from smartsquare.core import square

class TestCore(unittest.TestCase):
    '''Unittest for core module'''

    def test_float(self):
        '''Test with the float'''
        self.assertAlmostEqual(square(2.), 4.)

if __name__=='__main__':
    unittest.main()
