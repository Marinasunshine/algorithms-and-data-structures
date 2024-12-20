import unittest
from lab4.task13.src.task13_2 import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue(capacity=3)

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty())

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.head.data, 10)
        self.queue.enqueue(20)
        self.assertEqual(self.queue.tail.data, 20)

    def test_dequeue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)
        self.assertEqual(self.queue.dequeue(), 10)
        self.assertEqual(self.queue.dequeue(), 20)
        self.assertEqual(self.queue.dequeue(), 30)
        self.assertTrue(self.queue.is_empty())
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_is_full(self):
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue(30)
        self.assertTrue(self.queue.is_full())

    def test_enqueue_full_queue(self):
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.enqueue(30)


    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.dequeue()

    def test_display(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        #print("\nExpected: 1 2 3 None")
        self.queue.display()