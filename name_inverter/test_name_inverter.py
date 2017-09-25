import unittest

from name_inverter.name_inverter import NameInverter


class NameInverterTest(unittest.TestCase):
    def setUp(self):
        self.name_inverter = NameInverter()

    def assertInverted(self, original_name, inverted_name):
        self.assertEqual(inverted_name, self.name_inverter.invert_name(original_name))

    def test_given_none_returns_empty_string(self):
        self.assertInverted(None, "")

    def test_given_empty_string_return_empty_string(self):
        self.assertInverted("", "")

    def test_given_simple_name_return_simple_name(self):
        self.assertInverted("Name", "Name")

    def test_given_first_last_return_last_first(self):
        self.assertInverted("First Last", "Last, First")

    def test_given_simple_name_with_spaces_return_simple_name_without_spaces(self):
        self.assertInverted(" Name ", "Name")

    def test_given_first_last_with_extra_spaces_return_last_first(self):
        self.assertInverted("  First   Last  ", "Last, First")

    def test_ignore_honorifics(self):
        self.assertInverted("Mr. First Last", "Last, First")
        self.assertInverted("Mrs. First Last", "Last, First")

    def test_post_nominals_stay_at_end(self):
        self.assertInverted("First Last Sr.", "Last, First Sr.")
        self.assertInverted("First Last BS. Phd.", "Last, First BS. Phd.")

    def test_integration(self):
        self.assertInverted("Mr.  Robert   Martin III esq.", "Martin, Robert III esq.")
