#TEST
import unittest
from solutions.PY import even_fibonacci_numbers;

class TestFib(unittest.TestCase):

    def test_even_fib(self):
        evens =  even_fibonacci_numbers();
        self.assertEqual(evens,4613732,'Should be 4613732');

if __name__=='__main__':
    unittest.main();