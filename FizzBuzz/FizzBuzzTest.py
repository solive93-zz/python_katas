import unittest
from FizzBuzz import FizzBuzz


class FizzBuzzTest(unittest.TestCase):
    def test_fizz_condition(self):
        fizzbuzz = FizzBuzz()
        response = fizzbuzz.calculate(3)
        self.assertEqual('Fizz', response)

    def test_buzz_condition(self):
        fizzbuzz = FizzBuzz()
        response = fizzbuzz.calculate(5)
        self.assertEqual('Buzz', response)

    def test_fizzbuzz_condition(self):
        fizzbuzz = FizzBuzz()
        response = fizzbuzz.calculate(15)
        self.assertEqual('FizzBuzz', response)
        self.assertEqual('FizzBuzz', fizzbuzz.calculate(30))

    def test_any_condition_met(self):
        fizzbuzz = FizzBuzz()
        self.assertEqual(7, fizzbuzz.calculate(7))


if __name__ == '__main__':
    unittest.main()
