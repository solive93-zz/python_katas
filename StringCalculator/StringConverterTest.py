import unittest
from StringConverter import StringConverter

class MyTestCase(unittest.TestCase):
    def test_returns_0_when_empty_string_given(self):
        converter = StringConverter()
        output = converter.add("")
        self.assertEqual(0, output)

    def test_returns_same_number_as_int(self):
        converter = StringConverter()
        output = converter.add("3")
        self.assertEqual(3, output)
        self.assertEqual(100, converter.add("100"))

    def test_returns_sum_when_2_numbers_given(self):
        converter = StringConverter()
        self.assertEqual(5, converter.add("3, 2"))
        self.assertEqual(2000000, converter.add("1999999, 1"))

    def test_returns_sum_when_3_or_more_numbers_given(self):
        converter = StringConverter()
        self.assertEqual(6, converter.add("3, 2, 1"))
        self.assertEqual(400, converter.add("299, 1, 98, 2"))
        self.assertEqual(10, converter.add("1, 1, 1, 1, 1, 1, 1, 1, 1, 1"))




if __name__ == '__main__':
    unittest.main()
