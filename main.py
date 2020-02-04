"""
This is the main application class for the search.
This class interfaces with query_parser, search and data_extractor.
"""
import json
import os

from data_extractor import DataExtractor
from query_parser import QueryParser
from search import Search

DIR_PATH = os.getcwd()
META_DATA_LOC = DIR_PATH + "/meta_data.json"
SEARCH = Search()
QUERY_PARSER = QueryParser()


def setup_data(meta_data_loc):
    """
    Sets up the data so we can facilitate search queries on it.
    :param meta_data_loc: location of the meta data file
    :return: list of all data
    """

    meta_data = []
    with open(meta_data_loc) as json_file:
        meta_data = json.load(json_file)
    data = []

    for row in meta_data:
        data.append(DataExtractor(row["name_references"], row["location"], DIR_PATH))

    return data


def get_data_from_reference_name(reference_name, data_sources):
    """
    Get data based on the reference name
    A particular data source can referenced by many names such as USERS, USER etc.

    :return: corresponding data
    """
    reference_name = reference_name.lower()
    for data in data_sources:
        if reference_name in data.name_references:
            return data.get_data()

    return None


def execute_query(query, data_sources):
    """
    Execute a given query
    :param data_sources: data sources passed that the query will be run against
    :param query: string
    :return: True/False
            False if the query is going to quit the application
            True otherwise
    """

    query_args = QUERY_PARSER.split_query_into_arguments(query)
    query_type = QUERY_PARSER.get_type_of_query(query_args)

    if query_type == query_type.HELP_QUERY:
        print(QUERY_PARSER.get_help_query_output())
    elif query_type == query_type.INVALID_QUERY:
        print(" Invalid query, Please retry or type exit to quit")
    elif query_type == query_type.EXIT_QUERY:
        print(" Quitting the Search Application")
        return False
    else:
        reference = QUERY_PARSER.get_underlying_data_reference_from_query(query_args)

        try:
            data = get_data_from_reference_name(reference, data_sources)
        except FileNotFoundError:
            print("Something went wrong while extracting data")
            return True

        if data is None:
            print(" The given data source does not exist. Please try another query or type exit to quit.\n")
        elif query_type == query_type.LIST_QUERY:
            SEARCH.get_and_print_list_data(data)
        elif query_type == query_type.SEARCH_QUERY:
            field_name, value = QUERY_PARSER.get_field_name_value_from_query_args(query_args)
            SEARCH.get_and_print_search_data(data, field_name, value)

    return True


def get_headers():
    """
    Get header information
    """

    return "\n" + " Welcome to Zendesk Search Application.\n" + \
           " Type help to get a list of commands that can be executed\n" + \
           " Type exit/quit to quit the application\n\n" + \
           " Example queries:\n" + \
           " LIST USERS which will list all the fields in the users data\n" + \
           " SEARCH USERS _id 1 which will search for all users with _id field equal to 1\n\n"


all_data = setup_data(META_DATA_LOC)
headers = get_headers()
continue_execution = True

print(headers)

while continue_execution:
    query_from_user = input("Enter your query : ")
    continue_execution = execute_query(query_from_user, all_data)
