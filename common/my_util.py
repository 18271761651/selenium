import unittest

class Myutil(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('类开始执行一次')

    def setUp(self):
        print('每个用例开始前执行')

    def tearDown(self):
        print('每个用例结束后执行')

    @classmethod
    def tearDownClass(cls) -> None:
        print('类结束前执行一次')