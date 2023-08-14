# coding: utf-8

"""
    MailBaby Email Delivery and Management Service API

    **Send emails fast and with confidence through our easy to use [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API interface.** # Overview This is the API interface to the [Mail Baby](https//mail.baby/) Mail services provided by [InterServer](https://www.interserver.net). To use this service you must have an account with us at [my.interserver.net](https://my.interserver.net). # Authentication In order to use most of the API calls you must pass credentials from the [my.interserver.net](https://my.interserver.net/) site. We support several different authentication methods but the preferred method is to use the **API Key** which you can get from the [Account Security](https://my.interserver.net/account_security) page. 

    The version of the OpenAPI document: 1.1.0
    Contact: support@interserver.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

import openapi_client
from openapi_client.api.history_api import HistoryApi  # noqa: E501
from openapi_client.rest import ApiException


class TestHistoryApi(unittest.TestCase):
    """HistoryApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.history_api.HistoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_stats(self):
        """Test case for get_stats

        displays a list of blocked email addresses  # noqa: E501
        """
        pass

    def test_view_mail_log(self):
        """Test case for view_mail_log

        displays the mail log  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
