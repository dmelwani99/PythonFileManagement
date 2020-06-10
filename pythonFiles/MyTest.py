import unittest

def add(x):
    return x + 1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(add(0), 1)