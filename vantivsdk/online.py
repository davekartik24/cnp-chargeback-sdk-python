# -*- coding: utf-8 -*-l
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
from __future__ import absolute_import, print_function, unicode_literals

import requests
import xmltodict
import six
import pyxb
from requests.auth import HTTPBasicAuth
from . import (fields, utils, dict2obj)

conf = utils.Configuration()



# def request(request_type, request_body, param, conf, return_format='dict', timeout=30):
#
#     """Send request to server.
#
#        Args:
#            request_type: defines the type of the request is "GET" or "PUT"
#            request_body: object to be conver
#            param:
#            conf: An instance of utils.Configuration
#            return_format: Return format. The default is 'dict'. Could be one of 'dict', 'object' or 'xml'.
#            timeout: timeout for the request in seconds. timeout is not a time limit on the entire response. It's the time that server has not issued a response.
#
#        Returns:
#            response XML in desired format.
#
#        Raises:
#            VantivExceptions.
#        """
#
#     if not isinstance(conf, utils.Configuration):
#         raise utils.VantivException('conf must be an instance of utils.Configuration')
#
#     if not isinstance(timeout, six.integer_types) or timeout < 0:
#         raise utils.VantivException('timeout must be an positive int')
#
#     response_xml = _http_request(request_type, request_body, conf, param)
#     if request_type == 'GET':
#         response_dict = xmltodict.parse(response_xml)['chargebackRetrievalResponse']
#     elif request_type == 'PUT':
#         response_dict = xmltodict.parse(response_xml)['chargebackUpdateRespolnse']
#
#     if conf.print_xml:
#         import json
#         print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
#         return response_dict
#     else:
#         raise utils.VantivException(response_dict['@message'])

def _get_response(parameter_value, parameter_key):
    if parameter_key != "":
        conf.url = conf.url + "?"
        parameter_key = parameter_key+"="
    try:
        http_response = requests.get(conf.url + parameter_key + str(parameter_value), auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print("Request : ", requests)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')
    return response


def _get_responses(parameter_value1, parameter_key1, parameter_value2, parameter_key2):
    if parameter_key1 != "":
        conf.url = conf.url + "?"
        parameter_key1 = parameter_key1+"="
        parameter_key2 = parameter_key2 + "="
    try:
        http_response = requests.get(conf.url + parameter_key1 + str(parameter_value1) + "&"
                                + parameter_key2 + str(parameter_value2), auth=HTTPBasicAuth(conf.user, conf.password))

    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")
    print(requests)
    print("Response :", http_response)
    _check_response(http_response)
    response = _check_response_dict(http_response, return_format='dict')

    return response



def _create_request_xml(request_body, conf):
    """Create xml string from transaction object

    Args:
        request_body:
        conf: an instance of utils.Configuration

    Returns:
        XML string
    """
    request_xml = utils.obj_to_xml(request_body)

    if conf.print_xml:
        print('Request XML:\n', request_xml.decode('utf-8'), '\n')

    return request_xml


def _check_response(response):
    if response.status_code != 200:
        raise utils.VantivException("Error with Https Response, Status code: ", response.status_code)

    # Check empty response
    if not response:
        raise utils.VantivException("The response is empty, Please call Vantiv eCommerce")



def _print_response(response):
    if conf.print_xml:
        print('Response XML:\n', response.text, '\n')



def _check_response_dict(response, return_format='dict'):
    response_dict = xmltodict.parse(response.text)['chargebackRetrievalResponse']
    if response_dict['@xmlns'] != "":
        return_f_l = return_format.lower()
        if return_f_l == 'xml':
            response_xml = response.text
            return response_xml
        elif return_f_l == 'object':
            return fields.CreateFromDocument(response.text)
        else:
            if conf.print_xml:
                import json
                print('Response Dict:\n', json.dumps(response_dict, indent=4), '\n\n')
            return response_dict
    else:
        raise utils.VantivException("Invalid Format")



def _put_responses(parameter_value1, request_body):
    try:
        response = requests.put(conf.url + str(parameter_value1),
                                headers={"Content-Type": "application/com.vantivcnp.services-v2+xml",
                                         "Accept": "application/com.vantivcnp.services-v2+xml"},
                                auth=HTTPBasicAuth(conf.user, conf.password),
                                data=_create_request_xml(request_body, conf))
        print(requests)
    except requests.RequestException:
        raise utils.VantivException("Error with Https Request, Please Check Proxy and Url configuration")

    return response


def _get_case_id(case_id):
    response = _get_response(case_id, "")
    return response


def _get_token(token):
    response = _get_response(token, "token")
    return response


def _get_card_number(card_number, expiration_date):
    response = _get_responses(card_number, "cardNumber", expiration_date, "expirationDate")
    return response


def _get_arn(arn):
    response = _get_response(arn, "arn")
    return response


def _get_activity_date(activity_date):
    response = _get_response(activity_date.date(), "date")
    return response


def _get_actionable(actionable):
    response = _get_response(actionable, "actionable")
    return response


def _put_chargeback_update(caseId, request_body):
    response = _put_responses(caseId, request_body)
    response_dict = xmltodict.parse(response.text)['chargebackUpdateResponse']
    _check_response(response)
    _print_response(response)
    return response_dict




class VantivException(Exception):
    pass
