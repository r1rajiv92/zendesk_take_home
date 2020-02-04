This describes how to get started using the Zendesk search application.

# Introduction:
We have built a basic search application that can perform search on underlying data sources

# Data sources:
We currently have 3 data sources that we facilitate search on [Users, Organizations and tickets]. You can find them
in the repository directory.

# Types of queries:
We currently facilitate 2 types of queries:
1. LIST {data} which will list all the field names in the data.
2. SEARCH {data} {field_name} {value} which will search for all rows in data where the field_name is equal to value

In this version of the search, we perform exact matches that is the value should be exactly equal to the field name.

# How to run the application:
Just simply run main.py. This is main python script interface to run search queries
