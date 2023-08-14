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
import datetime

import openapi_client
from openapi_client.models.mail_blocks import MailBlocks  # noqa: E501
from openapi_client.rest import ApiException

class TestMailBlocks(unittest.TestCase):
    """MailBlocks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MailBlocks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MailBlocks`
        """
        model = openapi_client.models.mail_blocks.MailBlocks()  # noqa: E501
        if include_optional :
            return MailBlocks(
                local = [
                    {"date":"2023-08-07","from":"user@domain.com","messageId":"pFaRqFUEWkucjhTuIzYuoAgWU@domain.com","subject":"Test Email","to":"['client@site.com']"}
                    ], 
                mbtrap = [
                    {"date":"2023-08-07","from":"user@domain.com","messageId":"pFaRqFUEWkucjhTuIzYuoAgWU@domain.com","subject":"Test Email","to":"['client@site.com']"}
                    ], 
                subject = [
                    {"from":"user@domain.com","subject":"Test email"}
                    ]
            )
        else :
            return MailBlocks(
                local = [
                    {"date":"2023-08-07","from":"user@domain.com","messageId":"pFaRqFUEWkucjhTuIzYuoAgWU@domain.com","subject":"Test Email","to":"['client@site.com']"}
                    ],
                mbtrap = [
                    {"date":"2023-08-07","from":"user@domain.com","messageId":"pFaRqFUEWkucjhTuIzYuoAgWU@domain.com","subject":"Test Email","to":"['client@site.com']"}
                    ],
                subject = [
                    {"from":"user@domain.com","subject":"Test email"}
                    ],
        )
        """

    def testMailBlocks(self):
        """Test MailBlocks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
