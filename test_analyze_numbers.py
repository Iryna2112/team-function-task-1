import unittest

from analyze_numbers import analyze_numbers


class AnalyzeNumbersTests(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(
            analyze_numbers([]),
            {
                "count": 0,
                "min": None,
                "max": None,
                "average": None,
                "even_count": 0,
                "odd_count": 0,
            },
        )

    def test_mixed_numbers(self):
        self.assertEqual(
            analyze_numbers([2, 5, 8, -3, 10]),
            {
                "count": 5,
                "min": -3,
                "max": 10,
                "average": 4.4,
                "even_count": 3,
                "odd_count": 2,
            },
        )

    def test_negative_numbers_zero_and_duplicates(self):
        self.assertEqual(
            analyze_numbers([-4, -3, 0, 0, 5, 8]),
            {
                "count": 6,
                "min": -4,
                "max": 8,
                "average": 1.0,
                "even_count": 4,
                "odd_count": 2,
            },
        )

    def test_single_number(self):
        self.assertEqual(
            analyze_numbers([-7]),
            {
                "count": 1,
                "min": -7,
                "max": -7,
                "average": -7.0,
                "even_count": 0,
                "odd_count": 1,
            },
        )


if __name__ == "__main__":
    unittest.main()
