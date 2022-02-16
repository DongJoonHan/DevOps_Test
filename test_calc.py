import unittest
import calc


class sumtest(unittest.TestCase):
    def testSum(self):
        result = calc.sum(3, 5)
        self.assertEquals(8, result)

    def testMinus(self):
        result = calc.minus(5, 3)
        self.assertEquals(2, result)
