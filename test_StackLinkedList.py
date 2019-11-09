import unittest
from StackLinkedList import *


class StackLinkedListTest(unittest.TestCase):
    def test_(self):
        a = StackLinked(10)
        a.push(20)
        a.push(30)
        a.push(40)
        self.assertEqual('top: 40=> 30=> 20=> bottom: 10', str(a))

        self.assertEqual('40', str(a.peek()))

        a.push(50)
        self.assertEqual('top: 50=> 40=> 30=> 20=> bottom: 10', str(a))
        a.pop()
        self.assertEqual('top: 40=> 30=> 20=> bottom: 10', str(a))


if __name__ == '__main__':
    unittest.main()
