# !/usr/bin/env python
# _*_ conding:utf-8 _*_

# author: super

# from module import *
# from package.module import *

'''unittest 案例'''

import unittest


class Test(unittest.TestCase):
    def setup(self):
        print("this is setup")

    def test01(self):
        print("this is tesecase 1")

    def tearDown(self):
        print("this is tearDown")


if __name__ == '__main__':
    unittest.main()
    print("this is __name__")