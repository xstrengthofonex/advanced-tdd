import unittest

from wrapper.wrapper import Wrapper


class WrapperTest(unittest.TestCase):
    def setUp(self):
        self.wrapper = Wrapper()

    def assertWraps(self, s, width, expected):
        self.assertEqual(expected, self.wrapper.wrap(s, width))
    
    def test_should_wrap(self):
        self.assertWraps(None, 1, "")
        self.assertWraps("", 1, "")
        self.assertWraps("x", 1, "x")
        self.assertWraps("xx", 1, "x\nx")
        self.assertWraps("xxx", 1, "x\nx\nx")
        self.assertWraps("x x", 1, "x\nx")
        self.assertWraps("x xx", 3, "x\nxx")
        self.assertWraps("four score and seven years ago our fathers brought forth upon this continent", 7,
                         "four\nscore\nand\nseven\nyears\nago our\nfathers\nbrought\nforth\nupon\nthis\ncontine\nnt")
