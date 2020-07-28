from check_pwd import check_pwd
import random
import unittest
import string

class MyTestCase(unittest.TestCase):
    def test1(self):

       input = ''
       self.assertFalse(check_pwd(input))

    def test2(self):
       input = 'DLFKDADEDCVV'
       self.assertFalse(check_pwd((input)))

    def test3(self):
        input = 'asdfghooomjk'
        self.assertFalse(check_pwd(input))

    def test4(self):
        input = 'ALDFJLslds`+='
        self.assertTrue(check_pwd(input))


if __name__ == '__main__':
    unittest.main()