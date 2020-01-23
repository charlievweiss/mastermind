import unittest
from mastermind import compare_codes

class TestMastermind(unittest.TestCase):
    def test_compare_codes1(self):
        code = ['r', 'o', 'y', 'g']
        guess = ['r', 'o', 'o', 'o']
        self.assertEqual(compare_codes(code, guess), [2, 0])

    def test_compare_codes2(self):
        code = ['r', 'o', 'o', 'o']
        guess = ['r', 'o', 'y', 'g']
        self.assertEqual(compare_codes(code, guess), [2, 0])

    def test_compare_codes3(self):
        code = ['r', 'o', 'y', 'g']
        guess = ['b', 'b', 'o', 'o']
        self.assertEqual(compare_codes(code, guess), [0, 1])

    def test_compare_codes4(self):
        code = ['r', 'o', 'y', 'g']
        guess = ['b', 'b', 'b', 'b']
        self.assertEqual(compare_codes(code, guess), [0, 0])

    def test_compare_codes5(self):
        code = ['r', 'o', 'y', 'g']
        guess = ['r', 'o', 'y', 'g']
        self.assertEqual(compare_codes(code, guess), [4, 0])

    def test_compare_codes6(self):
        code = ['r', 'o', 'y', 'g']
        guess = ['g', 'r', 'o', 'y']
        self.assertEqual(compare_codes(code, guess), [0, 4])

if __name__ == '__main__':
    unittest.main()