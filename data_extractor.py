"""
Responsible for extracting the data from the given location.
"""
import json


class DataExtractor(object):
    """
    We don't extract data when this class is instantiated. Only
    when we need to search on a particular data source, we call get_data
    which will extract the data
    """
    data = None

    def __init__(self, name_references, location, base_directory_path):
        self.name_references = name_references
        self.location = base_directory_path + "/" + location

    def get_data(self):
        """
        Get the data from the location
        :return: data extracted
        """

        if self.data is None:
            with open(self.location) as json_file:
                self.data = json.load(json_file)

        return self.data
