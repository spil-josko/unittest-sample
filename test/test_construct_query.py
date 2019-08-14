import os
import sys
import json
import datetime

import unittest
from unittest import mock

from zendesk_importer.readers import ZendeskReaderBase, AuthException
from importerlib.reader import ReaderRequestError
from lib_utilities.test.request_mock import mocked_requests


def credentials_test_callback(request_url, kwargs):
    """ This is a callback function to check url and credentials. It is given to the mock request,
        which will call it. No return value is required, as the process expects you to raise your
        own exceptions. """

    # Check if the correct url was asked for
    assert("/api/v2/incremental/tickets.json" in request_url)

    # Split url, as the required format is url?start_time=...
    splitter = request_url.split("=")

    # Check if we can convert the unix time in the url to an integer.
    unix_time = int(splitter[1])
    assert isinstance(unix_time, int)

    # Was basic auth used with the correct parameters (mocked)?
    assert('auth' in kwargs)
    assert("unittest@spilgames.com" in kwargs["auth"])
    assert("thisismyapitoken" in kwargs["auth"])


class ZendeskReaderBaseTestCase(unittest.TestCase):
    """Test cases for ZendeskReaderBase """

    def get_reader(self):

        # Fake credentials for the reader object
        credentials_value = {
            "user": "unittest@spilgames.com",
            "api_token": "thisismyapitoken"
        }
        # Instantiate reader, tell it the date
        reader = ZendeskReaderBase()
        reader.start_date = datetime.date(2018, 9, 10)

        return reader, credentials_value

    @mock.patch.object(ZendeskReaderBase, 'credentials')
    @mock.patch("requests.get", mocked_requests)
    def test_get_auth_exception(self, mocked_credentials):
        mocked_requests.argument_test_callback = credentials_test_callback

        mocked_requests.return_value = {'status_code': '401',
                                        'text': json.dumps({'response': 'Auth error'})}

        reader, credentials_value = self.get_reader()
        mocked_credentials.return_value = credentials_value
        with self.assertRaises(AuthException):
            result = reader.get_api_data_inner()

    @mock.patch.object(ZendeskReaderBase, 'credentials')
    @mock.patch("requests.get", mocked_requests)
    def test_reader_exception(self, mocked_credentials):
        mocked_requests.argument_test_callback = credentials_test_callback

        mocked_requests.return_value = {'status_code': '500',
                                        'text': json.dumps({'response': 'Internal error'})}

        reader, credentials_value = self.get_reader()
        mocked_credentials.return_value = credentials_value
        with self.assertRaises(ReaderRequestError):
            result = reader.get_api_data_inner()

    @mock.patch.object(ZendeskReaderBase, 'credentials')
    @mock.patch("requests.get", mocked_requests)
    def test_reader_data(self, mocked_credentials):
        # Data to be tested
        actual_data = {
            "count": 2,
            "next_page": "notreallyanextpage",
            "tickets": [{"key": "lock", "key2": {"subkey1": "lock1", "subkey2": "lock2"}},
                        {"key": "lock", "key2": {"subkey1": "lock1", "subkey2": "lock2"}}]
        }

        mocked_requests.argument_test_callback = credentials_test_callback

        mocked_requests.return_value = {'status_code': '200',
                                        'text': json.dumps(actual_data)}

        reader, credentials_value = self.get_reader()
        mocked_credentials.return_value = credentials_value

        result = [item for item in reader.get_api_data_inner()]

        # I.e. a list?
        assert isinstance(result, list)

        # Are there more items in there, as we prescribed?
        assert len(result) > 0

        # Check if Transform logic (key[subkey] to key_subkey) is applied,
        # and if these have the correct values.
        for record in result:
            assert "key" in record
            assert record["key"] == "lock"

            assert "key2_subkey1" in record
            assert record["key2_subkey1"] == "lock1"

            assert "key2_subkey2" in record
            assert record["key2_subkey2"] == "lock2"

        return True
