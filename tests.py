import random
import unittest
from check_pwd import check_pwd


class MyTestCase(unittest.TestCase):
    def test1(self):

       input = '  1   '
       expected = False
       self.assertEqual(check_pwd(input), expected)


if __name__ == '__main__':
    unittest.main()
