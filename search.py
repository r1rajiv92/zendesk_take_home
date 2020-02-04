class Search(object):
    """
    Class that defines functions to enable search
    on a given data
    """

    @staticmethod
    def search_data(data, field_name, value):
        """
        Search the data based on the given field name and value

        :param data: data passed
        :param field_name: field name for search
        :param value: field value for search
        :return: results
        """

        if data is None:
            return []

        search_results = []
        for row in data:
            if field_name in row.keys():
                # simple string to string comparison
                if str(row[field_name]) == str(value):
                    search_results.append(row)

        return search_results

    @staticmethod
    def list_data_fields(data):
        """
        List the field names in the data

        :param data: data passed
        :return: an array of field name
        """
        if data is None:
            return []

        search_fields = set()
        for row in data:
            search_fields = search_fields.union(row.keys())

        return search_fields

    @staticmethod
    def pretty_print_search_result(search_result):
        """
        Pretty print the search result passed
        :param search_result: list of searched data
        """
        if len(search_result) == 0:
            print(" No results for the given search criteria")
        else:
            for row in search_result:
                print("\n")
                for key in row:
                    print(key + " : " + str(row[key]))
        print("\n")

    @staticmethod
    def pretty_print_list_result(list_result):
        """
        Pretty print the list passed
        :param list_result: list
        """
        if len(list_result) == 0:
            print(" There are no fields in this data")
        else:
            print("\n")
            for val in list_result:
                print(val)

        print("\n")

    def get_and_print_search_data(self, data, field_name, value):
        """
        Search the data and pretty print the results
        :param data: data passed
        :param field_name: field name for search
        :param value: field value for search
        """

        search_results = self.search_data(data, field_name, value)
        self.pretty_print_search_result(search_results)

    def get_and_print_list_data(self, data):
        """
        list the data fields and print the results
        :param data: data passed
        """

        list_results = self.list_data_fields(data)
        self.pretty_print_list_result(list_results)
