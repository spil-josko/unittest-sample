import os
import sys
import json
import datetime

import unittest
from unittest import mock

import sample
from sample.construct_query import construct_query


class ConstructQueryTestCase(unittest.TestCase):
    """Test cases for construct_query """

    def test_fields_table_group(self):
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

    def test_fields_table_nogroup(self):
        """Test the normal behaviour of the function"""

        fields = ["field1", "field2"]
        table = "table1"

        query = construct_query(
            fields=fields,
            table=table
        )

        for field in fields:
            assert field in query

        assert table in query

    def test_fields_table_faulty_field(self):
        """Test the normal behaviour of the function"""

        fields = True
        table = "table1"
        group = ["group1", "group2"]
        with self.assertRaises(AssertionError):
            query = construct_query(
                fields=fields,
                table=table,
                group=group
            )

    def test_fields_table_faulty_table(self):
        """Test the normal behaviour of the function"""

        fields = ["field1"]
        table = True
        group = ["group1", "group2"]
        with self.assertRaises(AssertionError):
            query = construct_query(
                fields=fields,
                table=table,
                group=group
            )

    def test_fields_table_faulty_group(self):
        """Test the normal behaviour of the function"""

        fields = ["field1"]
        table = "table1"
        group = True
        with self.assertRaises(AssertionError):
            query = construct_query(
                fields=fields,
                table=table,
                group=group
            )
