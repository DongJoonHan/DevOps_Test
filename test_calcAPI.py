import unittest
from unittest.mock import MagicMock, patch
import calc


class testSum2(unittest.TestCase):
    @patch("calc.api", return_value=2)
    def testsum2(self, mock):

        result = calc.api()
        self.assertEquals(result, 2)


class testSum3(unittest.TestCase):
    @patch("calc.api")
    def testsum3(self, mock):

        mock.return_value = 2
        result = calc.sumWithApi(5)
        self.assertEquals(result, 7)
