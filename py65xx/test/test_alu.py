import unittest
import itertools
import numpy as np
from py65xx import alu

class TestALU(unittest.TestCase):

    def test_addition(self):
        my_alu = alu.ALU()
        math_search_range =range(-128,127)
        for x,y in itertools.product(math_search_range,math_search_range):
            out, ovflw = my_alu.run(np.ubyte(x), np.ubyte(y), alu.OpCode.ADD)
            res = x+y
            if res>127 or res<-128:
                # Check for overflow
                self.assertTrue(ovflw)
            else:
                self.assertEqual(res, np.byte(out))
                self.assertFalse(ovflw)

    def test_or(self):
        my_alu = alu.ALU()
        math_search_range = range(-128, 127)
        for x, y in itertools.product(math_search_range, math_search_range):
            out, ovflw = my_alu.run(np.ubyte(x), np.ubyte(y), alu.OpCode.OR)
            res = np.ubyte(np.bitwise_or(x,y))
            self.assertEqual(res,out)
            self.assertFalse(ovflw)

    def test_xor(self):
        my_alu = alu.ALU()
        math_search_range = range(-128, 127)
        for x, y in itertools.product(math_search_range, math_search_range):
            out, ovflw = my_alu.run(np.ubyte(x), np.ubyte(y), alu.OpCode.XOR)
            res = np.ubyte(np.bitwise_xor(x,y))
            self.assertEqual(res,out)
            self.assertFalse(ovflw)

    def test_and(self):
        my_alu = alu.ALU()
        math_search_range = range(-128, 127)
        for x, y in itertools.product(math_search_range, math_search_range):
            out, ovflw = my_alu.run(np.ubyte(x), np.ubyte(y), alu.OpCode.AND)
            res = np.ubyte(np.bitwise_and(x,y))
            self.assertEqual(res,out)
            self.assertFalse(ovflw)

