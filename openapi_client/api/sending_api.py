# coding: utf-8

"""
    MailBaby Email Delivery and Management Service API

    **Send emails fast and with confidence through our easy to use [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) API interface.** # Overview This is the API interface to the [Mail Baby](https//mail.baby/) Mail services provided by [InterServer](https://www.interserver.net). To use this service you must have an account with us at [my.interserver.net](https://my.interserver.net). # Authentication In order to use most of the API calls you must pass credentials from the [my.interserver.net](https://my.interserver.net/) site. We support several different authentication methods but the preferred method is to use the **API Key** which you can get from the [Account Security](https://my.interserver.net/account_security) page. 

    The version of the OpenAPI document: 1.1.0
    Contact: support@interserver.net
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr, conlist

from typing import Optional

from openapi_client.models.email_address_name import EmailAddressName
from openapi_client.models.generic_response import GenericResponse
from openapi_client.models.mail_attachment import MailAttachment

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SendingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def send_adv_mail(self, subject : Annotated[StrictStr, Field(..., description="The subject or title of the email")], body : Annotated[StrictStr, Field(..., description="The main email contents.")], var_from : EmailAddressName, to : Annotated[conlist(EmailAddressName), Field(..., description="A list of destionation email addresses to send this to")], replyto : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) A list of email addresses that specify where replies to the email should be sent instead of the _from_ address.")] = None, cc : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) A list of email addresses to carbon copy this message to.  They are listed on the email and anyone getting the email can see this full list of Contacts who received the email as well.")] = None, bcc : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) list of email addresses that should receive copies of the email.  They are hidden on the email and anyone gettitng the email would not see the other people getting the email in this list.")] = None, attachments : Annotated[Optional[conlist(MailAttachment)], Field(description="(optional) File attachments to include in the email.  The file contents must be base64 encoded!")] = None, id : Annotated[Optional[StrictInt], Field(description="(optional)  ID of the Mail order within our system to use as the Mail Account.")] = None, **kwargs) -> GenericResponse:  # noqa: E501
        """Sends an Email with Advanced Options  # noqa: E501

        Sends An email through one of your mail orders allowing additional options such as file attachments, cc, bcc, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_adv_mail(subject, body, var_from, to, replyto, cc, bcc, attachments, id, async_req=True)
        >>> result = thread.get()

        :param subject: The subject or title of the email (required)
        :type subject: str
        :param body: The main email contents. (required)
        :type body: str
        :param var_from: (required)
        :type var_from: EmailAddressName
        :param to: A list of destionation email addresses to send this to (required)
        :type to: List[EmailAddressName]
        :param replyto: (optional) A list of email addresses that specify where replies to the email should be sent instead of the _from_ address.
        :type replyto: List[EmailAddressName]
        :param cc: (optional) A list of email addresses to carbon copy this message to.  They are listed on the email and anyone getting the email can see this full list of Contacts who received the email as well.
        :type cc: List[EmailAddressName]
        :param bcc: (optional) list of email addresses that should receive copies of the email.  They are hidden on the email and anyone gettitng the email would not see the other people getting the email in this list.
        :type bcc: List[EmailAddressName]
        :param attachments: (optional) File attachments to include in the email.  The file contents must be base64 encoded!
        :type attachments: List[MailAttachment]
        :param id: (optional)  ID of the Mail order within our system to use as the Mail Account.
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GenericResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the send_adv_mail_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.send_adv_mail_with_http_info(subject, body, var_from, to, replyto, cc, bcc, attachments, id, **kwargs)  # noqa: E501

    @validate_arguments
    def send_adv_mail_with_http_info(self, subject : Annotated[StrictStr, Field(..., description="The subject or title of the email")], body : Annotated[StrictStr, Field(..., description="The main email contents.")], var_from : EmailAddressName, to : Annotated[conlist(EmailAddressName), Field(..., description="A list of destionation email addresses to send this to")], replyto : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) A list of email addresses that specify where replies to the email should be sent instead of the _from_ address.")] = None, cc : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) A list of email addresses to carbon copy this message to.  They are listed on the email and anyone getting the email can see this full list of Contacts who received the email as well.")] = None, bcc : Annotated[Optional[conlist(EmailAddressName)], Field(description="(optional) list of email addresses that should receive copies of the email.  They are hidden on the email and anyone gettitng the email would not see the other people getting the email in this list.")] = None, attachments : Annotated[Optional[conlist(MailAttachment)], Field(description="(optional) File attachments to include in the email.  The file contents must be base64 encoded!")] = None, id : Annotated[Optional[StrictInt], Field(description="(optional)  ID of the Mail order within our system to use as the Mail Account.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Sends an Email with Advanced Options  # noqa: E501

        Sends An email through one of your mail orders allowing additional options such as file attachments, cc, bcc, etc.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_adv_mail_with_http_info(subject, body, var_from, to, replyto, cc, bcc, attachments, id, async_req=True)
        >>> result = thread.get()

        :param subject: The subject or title of the email (required)
        :type subject: str
        :param body: The main email contents. (required)
        :type body: str
        :param var_from: (required)
        :type var_from: EmailAddressName
        :param to: A list of destionation email addresses to send this to (required)
        :type to: List[EmailAddressName]
        :param replyto: (optional) A list of email addresses that specify where replies to the email should be sent instead of the _from_ address.
        :type replyto: List[EmailAddressName]
        :param cc: (optional) A list of email addresses to carbon copy this message to.  They are listed on the email and anyone getting the email can see this full list of Contacts who received the email as well.
        :type cc: List[EmailAddressName]
        :param bcc: (optional) list of email addresses that should receive copies of the email.  They are hidden on the email and anyone gettitng the email would not see the other people getting the email in this list.
        :type bcc: List[EmailAddressName]
        :param attachments: (optional) File attachments to include in the email.  The file contents must be base64 encoded!
        :type attachments: List[MailAttachment]
        :param id: (optional)  ID of the Mail order within our system to use as the Mail Account.
        :type id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GenericResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'subject',
            'body',
            'var_from',
            'to',
            'replyto',
            'cc',
            'bcc',
            'attachments',
            'id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_adv_mail" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['subject']:
            _form_params.append(('subject', _params['subject']))

        if _params['body']:
            _form_params.append(('body', _params['body']))

        if _params['var_from']:
            _form_params.append(('from', _params['var_from']))

        if _params['to']:
            _form_params.append(('to', _params['to']))
            _collection_formats['to'] = 'csv'

        if _params['replyto']:
            _form_params.append(('replyto', _params['replyto']))
            _collection_formats['replyto'] = 'csv'

        if _params['cc']:
            _form_params.append(('cc', _params['cc']))
            _collection_formats['cc'] = 'csv'

        if _params['bcc']:
            _form_params.append(('bcc', _params['bcc']))
            _collection_formats['bcc'] = 'csv'

        if _params['attachments']:
            _form_params.append(('attachments', _params['attachments']))
            _collection_formats['attachments'] = 'csv'

        if _params['id']:
            _form_params.append(('id', _params['id']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded', 'application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['apiKeyAuth']  # noqa: E501

        _response_types_map = {
            '200': "GenericResponse",
            '400': "GetMailOrders401Response",
            '401': "GetMailOrders401Response",
            '404': "GetMailOrders401Response",
        }

        return self.api_client.call_api(
            '/mail/advsend', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def send_mail(self, to : Annotated[StrictStr, Field(..., description="The Contact whom is the primary recipient of this email.")], var_from : Annotated[StrictStr, Field(..., description="The contact whom is the this email is from.")], subject : Annotated[StrictStr, Field(..., description="The subject or title of the email")], body : Annotated[StrictStr, Field(..., description="The main email contents.")], **kwargs) -> GenericResponse:  # noqa: E501
        """Sends an Email  # noqa: E501

        Sends an email through one of your mail orders.  *Note*: If you want to send to multiple recipients or use file attachments use the advsend (Advanced Send) call instead.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_mail(to, var_from, subject, body, async_req=True)
        >>> result = thread.get()

        :param to: The Contact whom is the primary recipient of this email. (required)
        :type to: str
        :param var_from: The contact whom is the this email is from. (required)
        :type var_from: str
        :param subject: The subject or title of the email (required)
        :type subject: str
        :param body: The main email contents. (required)
        :type body: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GenericResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the send_mail_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.send_mail_with_http_info(to, var_from, subject, body, **kwargs)  # noqa: E501

    @validate_arguments
    def send_mail_with_http_info(self, to : Annotated[StrictStr, Field(..., description="The Contact whom is the primary recipient of this email.")], var_from : Annotated[StrictStr, Field(..., description="The contact whom is the this email is from.")], subject : Annotated[StrictStr, Field(..., description="The subject or title of the email")], body : Annotated[StrictStr, Field(..., description="The main email contents.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Sends an Email  # noqa: E501

        Sends an email through one of your mail orders.  *Note*: If you want to send to multiple recipients or use file attachments use the advsend (Advanced Send) call instead.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_mail_with_http_info(to, var_from, subject, body, async_req=True)
        >>> result = thread.get()

        :param to: The Contact whom is the primary recipient of this email. (required)
        :type to: str
        :param var_from: The contact whom is the this email is from. (required)
        :type var_from: str
        :param subject: The subject or title of the email (required)
        :type subject: str
        :param body: The main email contents. (required)
        :type body: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GenericResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'to',
            'var_from',
            'subject',
            'body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_mail" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['to']:
            _form_params.append(('to', _params['to']))

        if _params['var_from']:
            _form_params.append(('from', _params['var_from']))

        if _params['subject']:
            _form_params.append(('subject', _params['subject']))

        if _params['body']:
            _form_params.append(('body', _params['body']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded', 'application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['apiKeyAuth']  # noqa: E501

        _response_types_map = {
            '200': "GenericResponse",
            '400': "GetMailOrders401Response",
            '401': "GetMailOrders401Response",
            '404': "GetMailOrders401Response",
        }

        return self.api_client.call_api(
            '/mail/send', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))