import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_percentiles(self):
        for i in range(20) : 
           self.assertTrue( np.abs( percentile( x, 5+i*5 ) - np.percentile(x, 5+i*5) ) < 1e-5, "Your function for calculating percentiles is not working correctly" )
