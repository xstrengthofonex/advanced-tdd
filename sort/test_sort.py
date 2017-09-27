import unittest


class SortTest(unittest.TestCase):
    def assertSorted(self, expected, input_array):
        self.assertEqual(expected, self.sort(input_array))

    def test_null_input(self):
        self.assertSorted([], None)

    def test_empty_array(self):
        self.assertSorted([], [])

    @staticmethod
    def sort(input_array):
        if input_array:
            return input_array
        return []
