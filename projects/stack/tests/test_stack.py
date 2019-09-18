import unittest

from stack.stack import Stack


class TestStack(unittest.TestCase):

    def setUp(self) -> None:
        self.st = Stack()

    def test_is_empty(self):
        self.assertTrue(self.st.is_empty(), "The stack is not empty")
        self.assertRaises(IndexError, self.st.pop)

    def test_repr(self):
        self.assertEqual("Stack()", repr(self.st), "The repr method does not work properly")

    def test_push_one_item(self):
        self.st.push(2)
        self.assertFalse(self.st.is_empty())
        self.assertEqual("Stack(2)", str(self.st))

    def test_push_multiple_items(self):
        self.st.push(3)
        self.st.push(10)
        self.assertEqual("Stack(3, 10)", str(self.st))
        popped_item = self.st.pop()
        self.assertEqual(10, popped_item)

    def test_is_full(self):
        for i in range(10):
            self.st.push(i)
        self.assertTrue(self.st.is_full())
        self.assertRaises(OverflowError, self.st.push, 12)

    def test_pop_one_item(self):
        self.st.push(3)
        popped_item = self.st.pop()
        self.assertEqual(3, popped_item)

    def test_pop_multiple_items(self):
        self.st.push(3)
        self.st.push(10)
        popped_item = self.st.pop()
        self.assertEqual(10, popped_item)
        popped_item = self.st.pop()
        self.assertEqual(3, popped_item)

    def test_type(self):
        self.assertRaises(TypeError, self.st.push, "3")
        self.assertRaises(TypeError, self.st.push, 3.1)
        self.assertRaises(TypeError, self.st.push, True)

    def test_top_non_empty_stack(self):
        self.st.push(3)
        self.st.push(10)
        self.assertEqual(10, self.st.top())

    def test_top_empty_stack(self):
        self.assertRaises(IndexError, self.st.top)


if __name__ == '__main__':
    unittest.main()
