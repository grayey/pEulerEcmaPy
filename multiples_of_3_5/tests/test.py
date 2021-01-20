#TEST
import unittest
from solutions.PY import multiples



class TestMultiples(unittest.TestCase):

    def test_3_and_5(self):
        try:
            print('Running test for limit=1000 and args=(3,5)');
            self.assertEqual(multiples(), 233168, "Should be 233168");
        except NameError:
            raise Exception('Skipped test_3_and_5 due to name error.');

    def test_limit_10(self):
        try:
            print('Running test for limit=10 and args=(3,5)');
            limit_10 = multiples(limit=10);
            self.assertEqual(limit_10, 23, "Should be 23");
        except NameError:
            raise Exception('Skipped test_limit_10 due to name error.');

if __name__ == '__main__':
    unittest.main()