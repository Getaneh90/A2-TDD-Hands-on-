from check_pwd import check_pwd
import random
import unittest

class MyTestCase(unittest.TestCase):
    def test1(self):

       input = ''
       self.assertFalse(check_pwd(input))

    def test2(self):



if __name__ == '__main__':
    unittest.main()
