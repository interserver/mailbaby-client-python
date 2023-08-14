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
from openapi_client.models.mail_log_entry import MailLogEntry  # noqa: E501
from openapi_client.rest import ApiException

class TestMailLogEntry(unittest.TestCase):
    """MailLogEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MailLogEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MailLogEntry`
        """
        model = openapi_client.models.mail_log_entry.MailLogEntry()  # noqa: E501
        if include_optional :
            return MailLogEntry(
                id = 103172, 
                id = '17c7eda538e0005d03', 
                var_from = 'person@mysite.com', 
                to = 'client@isp.com', 
                subject = 'sell 0.005 shares', 
                message_id = '<vmiLEebsuCbSpUxD7oN3REpaN4VbN6BrdCAbNKIrdAo@relay0.mailbaby.net>', 
                created = '2021-10-14 08:50:10', 
                time = 1634215809, 
                user = 'mb5658', 
                transtype = 'ESMTPSA', 
                origin = '199.231.189.154', 
                interface = 'feeder', 
                sending_zone = 'interserver', 
                body_size = 63, 
                seq = 1, 
                recipient = 'client@isp.com', 
                domain = 'interserver.net', 
                locked = 1, 
                lock_time = 1634215818533, 
                assigned = 'relay1', 
                queued = '2021-10-14T12:50:15.487Z', 
                mx_hostname = 'mx.j.is.cc', 
                response = '250 2.0.0 Ok queued as C91D83E128C'
            )
        else :
            return MailLogEntry(
                id = 103172,
                id = '17c7eda538e0005d03',
                var_from = 'person@mysite.com',
                to = 'client@isp.com',
                subject = 'sell 0.005 shares',
                created = '2021-10-14 08:50:10',
                time = 1634215809,
                user = 'mb5658',
                transtype = 'ESMTPSA',
                origin = '199.231.189.154',
                interface = 'feeder',
                sending_zone = 'interserver',
                body_size = 63,
                seq = 1,
                recipient = 'client@isp.com',
                domain = 'interserver.net',
                locked = 1,
                lock_time = 1634215818533,
                assigned = 'relay1',
                queued = '2021-10-14T12:50:15.487Z',
                mx_hostname = 'mx.j.is.cc',
                response = '250 2.0.0 Ok queued as C91D83E128C',
        )
        """

    def testMailLogEntry(self):
        """Test MailLogEntry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
