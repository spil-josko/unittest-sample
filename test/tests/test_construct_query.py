import os
import sys
import json
import datetime

import unittest
from unittest import mock

import container  
from container import construct_query

class ConstructQueryTestCase(unittest.TestCase):
    """Test cases for construct_query """

    def test_fields_table(self):
        """Test the normal behaviour of the function"""

        fields = ["field1", "field2"]
        table = "table1"
        group = ["group1", "group2"]

        query = construct_query(
            fields=fields,
            table=table,
            group=group
        )

        for field in fields:
            assert field in query

        assert table in query

        for field in group:
            assert field in query