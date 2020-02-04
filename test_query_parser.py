import unittest

from query_parser import QueryParser


class TestQueryParser(unittest.TestCase):
    test_query_parser = QueryParser()

    def test_split_query_into_arguments(self):
        query = "search user field value"
        query_args = QueryParser.split_query_into_arguments(query)

        self.assertEqual(query_args[0], "search")
        self.assertEqual(query_args[1], "user")
        self.assertEqual(query_args[2], "field")
        self.assertEqual(query_args[3], "value")

    def test_type_of_query(self):
        query_args = ["search", "user", "field", "value"]
        query_type = self.test_query_parser.get_type_of_query(query_args)
        self.assertEqual(query_type, QueryParser.QueryType.SEARCH_QUERY)

        query_args = ["list", "user"]
        query_type = self.test_query_parser.get_type_of_query(query_args)
        self.assertEqual(query_type, QueryParser.QueryType.LIST_QUERY)

        query_args = ["help"]
        query_type = self.test_query_parser.get_type_of_query(query_args)
        self.assertEqual(query_type, QueryParser.QueryType.HELP_QUERY)


if __name__ == '__main__':
    unittest.main()
