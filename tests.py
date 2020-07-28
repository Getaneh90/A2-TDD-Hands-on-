import random
import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    def test1(self):

       input = ''
       self.assertFalse(check_pwd(input))


if __name__ == '__main__':
    unittest.main()
