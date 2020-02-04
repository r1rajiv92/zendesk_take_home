"""
This is mainly responsible to parsing the query into a more structured format
for easy of execution
"""
from enum import Enum


class QueryParser(object):

    class QueryType(Enum):
        SEARCH_QUERY = 1
        LIST_QUERY = 2
        EXIT_QUERY = 3
        HELP_QUERY = 4
        INVALID_QUERY = 5

    def __init__(self):
        # references for query types
        self.list_query_references = ["list", "lst"]
        self.exit_query_references = ["exit", "quit", "q"]
        self.search_query_references = ["search"]
        self.help_query_references = ["help"]

        self.help_query_output = self.get_help_query_information()

    @staticmethod
    def split_query_into_arguments(query):
        """
        Split query into arguments
        :param query:
        :return: arguments
        """

        return query.split(" ")

    def get_type_of_query(self, query_args):
        """
        Get the type of the query
        :param query_args: list of query arguments
        :return: query type (enum)
        """

        if len(query_args) > 0:
            query_type_reference = query_args[0].lower()
            if query_type_reference in self.list_query_references:
                return self.QueryType.LIST_QUERY
            elif query_type_reference in self.exit_query_references:
                return self.QueryType.EXIT_QUERY
            elif query_type_reference in self.search_query_references:
                return self.QueryType.SEARCH_QUERY
            elif query_type_reference in self.help_query_references:
                return self.QueryType.HELP_QUERY

        return self.QueryType.INVALID_QUERY

    @staticmethod
    def get_field_name_value_from_query_args(query_args):
        """
        Extract the field name and value from query args.
        This is currently used only for search queries

        :param query_args: query arguments
        :return: field_name, value
        """

        if len(query_args) > 3:
            return query_args[2], query_args[3]
        else:
            return None, None

    @staticmethod
    def get_underlying_data_reference_from_query(query_args):
        """
        Extract the underlying data reference name from the query.
        :param query_args: query arguments
        :return: data reference name
        """

        if len(query_args) > 1:
            return query_args[1]
        else:
            return None

    @staticmethod
    def get_help_query_information():

        return "We currently facilitate 2 types of commands.\n" + \
               "1. LIST {data} which will list all the field names in the data.\n" + \
               "2. SEARCH {data} {field_name} {value} which will search for all rows in data" \
               " where the field_name is equal to value.\n\n" + \
               "Also, we currently facilitate these commands only on USERS, ORGANIZATIONS and TICKETS\n\n"

    def get_help_query_output(self):

        return self.help_query_output
