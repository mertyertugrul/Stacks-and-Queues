import unittest
from Queue import *

class MyTestCase(unittest.TestCase):
    def test_something(self):
        a = Queue(10)
        a.enqueue(20)
        a.enqueue(30)
        a.enqueue(40)
        self.assertEqual('first: 10=> 20=> 30=> last: 40', str(a))

        a.dequeue()
        self.assertEqual('first: 20=> 30=> last: 40', str(a))

        self.assertEqual(20, a.peek())


if __name__ == '__main__':
    unittest.main()
