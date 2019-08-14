import os
import sys
import json
import datetime

import unittest
from unittest import mock

import sample
from sample.exec_query import exec_query


class ExecQueryTestCase(unittest.TestCase):
    """Test cases for construct_query """

    @mock.patch("sample.exec_query.get_bq_client")
    @mock.patch("sample.exec_query.get_query_as_array_dict")
    def test_exec_query(self, mocked_as_dict, mocked_bq):
        """This is a unit test that requires mocking. The function should call both mocked objects."""

        exec_query("/opt/container/secret.json", "SELECT 1")

        mocked_as_dict.assert_called()
        mocked_bq.assert_called()
