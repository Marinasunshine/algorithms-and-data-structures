import unittest
from lab4.task13.src.task13_1 import Stack

class TestStack(unittest.TestCase):
    def setUp(self):
        self.stack = Stack()

    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_push(self):
        self.stack.push(10)
        self.assertEqual(self.stack.top.data, 10)
        self.stack.push(20)
        self.assertEqual(self.stack.top.data, 20)

    def test_pop(self):
        self.stack.push(10)
        self.stack.push(20)
        self.stack.push(30)
        self.assertEqual(self.stack.pop(), 30)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.pop(), 10)
        self.assertTrue(self.stack.is_empty())

    def test_display(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        #print("\nОжидается: 3 2 1 None")
        self.stack.display()