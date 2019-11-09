import unittest
from StackArrays import *


class StackLinkedArrayTest(unittest.TestCase):
    def test_(self):
        a = StackArray(10)
        a.push(20)
        a.push(30)
        a.push(40)
        self.assertEqual('[10, 20, 30, 40]', str(a))

        self.assertEqual('40', str(a.peek()))

        a.push(50)
        self.assertEqual('[10, 20, 30, 40, 50]', str(a))
        a.pop()
        self.assertEqual('[10, 20, 30, 40]', str(a))


if __name__ == '__main__':
    unittest.main()
