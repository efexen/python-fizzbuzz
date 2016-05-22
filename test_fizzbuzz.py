from fizzbuzz import FizzBuzz

import unittest

class FizzBuzzTestSuite(unittest.TestCase):

    def test_default_fizz_rule(self):
        self.assertEqual(FizzBuzz().value_for(3), 'Fizz')

    def test_default_buzz_rule(self):
        self.assertEqual(FizzBuzz().value_for(5), 'Buzz')

    def test_rule_combination(self):
        self.assertEqual(FizzBuzz().value_for(15), 'FizzBuzz')

    def test_non_matching(self):
        self.assertEqual(FizzBuzz().value_for(7), '7')

    def test_new_rules(self):
        new_rules = { 7: 'Bazz' }
        self.assertEqual(FizzBuzz(new_rules).value_for(7), 'Bazz')

if __name__ == '__main__':
    unittest.main()
