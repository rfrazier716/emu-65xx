import unittest
import itertools
import numpy as np
from py65xx import alu



class TestALU(unittest.TestCase):

    def test_addition(self):
        my_alu = alu.ALU()
        math_search_range =range(-128,127)
        for x,y in itertools.product(math_search_range,math_search_range):
            out, ovflw = my_alu.run(np.byte(x), np.byte(y), alu.OpCode.ADD)
            res = x+y
            if res>127 or res<-128:
                # Check for overflow
                self.assertTrue(ovflw)
            else:
                self.assertEqual(res, np.byte(out))
                self.assertFalse(ovflw)

