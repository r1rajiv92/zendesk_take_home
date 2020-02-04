import unittest

from data_extractor import DataExtractor


class TestDataExtractor(unittest.TestCase):
    def test_data_does_not_exist(self):
        data = DataExtractor("test", "test.json", "/home")
        try:
            data.get_data()
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    unittest.main()
