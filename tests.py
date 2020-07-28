from check_pwd import check_pwd
import random
import unittest
import string

class MyTestCase(unittest.TestCase):
    def test1(self):

       input = ''
       self.assertFalse(check_pwd(input))

    def test2(self):
       lowerCase = string.ascii_lowercase
       self.assertFalse(check_pwd((lowerCase)))



if __name__ == '__main__':
    unittest.main()
