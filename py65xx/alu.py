"""
ALU For 65XX processor

The hardware implementation of the 6502 executes all operations in parallel, with the contents of the output register
controlled by the instruction sent to the ALU.

For software we use a dict that holds function pointers for every function, so only one math function is executed for
every call to the ALU

Supported Commands are:
ADD -- Add Registers A&B
OR -- OR Registers A&B
XOR -- XOR Registers A&B
AND -- AND Registers A&B
SHR -- Shift Register A right one bit

"""

from enum import IntEnum
import numpy as np

np.seterr(over="ignore")

class OpCode(IntEnum):
    ADD = 0 # Addition
    OR = 1 # bitwise OR
    XOR = 2 # bitwise XOR
    AND = 3 # bitwise AND
    SHR = 4 # Logical shift right

class ALU():

    def __init__(self):
        self._A = np.ubyte(0x00)  # A Register
        self._B = np.ubyte(0x00)  # B Register
        self._O = np.ubyte(0x00)  # Output Register
        self._overflow = False   # Overflow/Underflow flag

        # tuple of ALU operations responsible for calling functions
        self._op_set = (
            self._add,
            self._or,
            self._xor,
            self._and,
            self._shift_right
        )

    def run(self, a_reg, b_reg, operation):
        """
        executes the ALU operation with the given input registers

        :param a_reg:
        :param b_reg:
        :param operation:
        :return:
        """
        # load the register values into the instance
        self._A = a_reg
        self._B = b_reg

        self._overflow = False  # Clear the overflow flag
        self._op_set[operation]()  # Call the operation
        return self._O, self._overflow  # return the result of the operation and whether the overflow bit was set

    def _add(self):
        """
        Adds two numbers together, sets overflow flag in event of over/underflow

        :return:
        """
        self._O = self._A + self._B
        # overflow checks if 2x negatives results in a positive or visa versa
        a_msb = self._A >= 0x80
        b_msb = self._B >= 0x80
        o_msb = self._O >= 0x80
        self._overflow = (not a_msb) and (not b_msb) and o_msb or (a_msb and b_msb and not o_msb)

    def _or(self):
        # Bitwise Or Operation
        self._O = np.bitwise_or(self._A, self._B)

    def _xor(self):
        # Bitwise Exclusive OR
        self._O = np.bitwise_xor(self._A, self._B)

    def _and(self):
        # Bitwise AND
        self._O = np.bitwise_and(self._A, self._B)

    def _shift_right(self):
        # Shift right 1 bit
        self._O = np.right_shift(self._A, 1)







