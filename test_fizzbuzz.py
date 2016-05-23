from fizzbuzz import FizzBuzz
from itertools import islice

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

    def test_overwrite_default_rules(self):
        new_rules = { 5: 'Bozz' }
        self.assertEqual(FizzBuzz(new_rules).value_for(3), '3')
        self.assertEqual(FizzBuzz(new_rules).value_for(5), 'Bozz')

    def test_iterator_starts_from_default_1(self):
        iterator = FizzBuzz().iterator()
        self.assertEqual(next(iterator), '1')

    def test_iterator_starts_from_custom_start(self):
        iterator = FizzBuzz().iterator(start = 7)
        self.assertEqual(next(iterator), '7')

    def test_iterator_stops_at_default_100(self):
        iterator = FizzBuzz().iterator()
        for last in iterator:
            pass
        self.assertEqual(last, 'Buzz')

    def test_iterator_stops_at_custom_stop(self):
        iterator = FizzBuzz().iterator(stop = 98)
        for last in iterator:
            pass
        self.assertEqual(last, '98')

    def test_iterator_applies_fizz_buzz_rules(self):
        iterator = FizzBuzz().iterator(start = 1, stop = 10)
        first10 = list(iterator)
        self.assertEqual(first10, ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz'])

    def test_infinite_iterator_is_loooong(self):
        iterator = FizzBuzz().iterator(stop = -1)
        loong = next(islice(iterator, 96831, None))
        self.assertEqual(loong, '96832')

if __name__ == '__main__':
    unittest.main()
