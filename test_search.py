import unittest

from search import Search


class TestSearch(unittest.TestCase):
    test_search = Search()

    def setup_data(self):
        self.test_data = []
        self.test_data.append({"_id": 1,
                               "name": "Tom",
                               "company": "zendesk",
                               "age": 28})

        self.test_data.append({"_id": 2,
                               "name": "Mark",
                               "company": "zendesk",
                               "age": 55})

        self.test_data.append({"_id": 3,
                               "name": "Mark",
                               "company": "zendesk",
                               "age": 30})

    def test_search_data(self):
        self.setup_data()
        search_results = self.test_search.search_data(self.test_data, "_id", 4)
        self.assertEqual(len(search_results), 0)

        search_results = self.test_search.search_data(self.test_data, "_id", 3)
        self.assertEqual(len(search_results), 1)
        self.assertEqual(search_results[0]["name"], "Mark")

        search_results = self.test_search.search_data(self.test_data, "name", "Mark")
        self.assertEqual(len(search_results), 2)

    def test_list_data(self):
        self.setup_data()
        list_results = self.test_search.list_data_fields(self.test_data)
        self.assertEqual(len(list_results), 4)
        self.assertEqual(list_results, {"_id", "name", "age", "company"})

        list_results = self.test_search.list_data_fields([])
        self.assertEqual(len(list_results), 0)


if __name__ == '__main__':
    unittest.main()
