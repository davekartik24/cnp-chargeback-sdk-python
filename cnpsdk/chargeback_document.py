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

from cnpsdk import (utils, communication)

conf = utils.Configuration()

SERVICE_ROUTE = "/services/chargebacks"


"""
/////////////////////////////////////////////////////
            ChargebackRetrieval API:
/////////////////////////////////////////////////////
"""


def upload_document(case_id, document_path, config=conf):
    document_id = document_path.split("/")[-1]
    url_suffix = SERVICE_ROUTE + "/upload/" + str(case_id) + "/" + str(document_id)
    return communication.http_post_document_request(url_suffix, document_path, config=config)
    

def retrieve_document(case_id, document_id, document_path, config=conf):
    url_suffix = SERVICE_ROUTE + "/retrieve/" + str(case_id) + "/" + str(document_id)
    communication.http_get_document_request(url_suffix, document_path, config=config)


def replace_document(case_id, document_id, document_path, config=conf):
    url_suffix = SERVICE_ROUTE + "/replace/" + case_id + "/" + document_id
    return communication.http_put_document_request(url_suffix, document_path, config=config)


def delete_document(case_id, document_id, config=conf):
    url_suffix = SERVICE_ROUTE + "/delete/" + str(case_id) + "/" + str(document_id)
    return communication.http_delete_document_response(url_suffix, config=config)


def list_documents(case_id, config=conf):
    url_suffix = SERVICE_ROUTE + "/list/" + str(case_id)
    return communication.http_get_document_list_request(url_suffix, config=config)
