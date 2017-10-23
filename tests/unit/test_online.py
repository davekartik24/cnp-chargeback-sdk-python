# -*- coding: utf-8 -*-
# Copyright (c) 2017 Vantiv eCommerce
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import os
import sys
import unittest
from unittest import mock
from vantivsdk import (utils, online, fields_chargebackDocument, fields_chargeback, contentTypeEnum,  parameters)
import six

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)
conf = utils.Configuration()


class TestOnline(unittest.TestCase):
    # @mock.patch.object(online, '_get_response')
    @unittest.skipIf(conf.url == 'http://prelive-pl-app1.litle.com:8048/services/chargebacks/',
                     "VantivException not raised by _get_response")
    @mock.patch.object(online, '_get_case_id')
    def test_request_get_response(self, mock_get_case_id):
        param = fields_chargeback.chargebackApiCase()
        param.caseId = u'1304283001'
        self.assertRaises(utils.VantivException, online._get_response, param.caseId, "")
        mock_get_case_id.return_value = ""
        self.assertRaises(utils.VantivException, online._get_response, param.caseId, "")

    def test_get_response_status(self):
        param = fields_chargeback.chargebackApiCase()
        self.assertRaises(utils.VantivException, online._get_response, param.caseId, "")

    @unittest.skipIf(conf.url == 'http://prelive-pl-app1.litle.com:8048/services/chargebacks/',
                     "VantivException not raised by _get_response")
    def test_request_get_responses(self):
        param = parameters.Parameters()
        param.expiration_date = u'0150'
        param.card_number = u'6500102010004006'
        self.assertRaises(utils.VantivException, online._get_responses, param.card_number, "cardNumber",
                          param.expiration_date, "expirationDate")

    def test_get_responses_status(self):
        param = parameters.Parameters()
        param.card_number = u'6500102010004006'
        self.assertRaises(utils.VantivException, online._get_responses, param.card_number, "", param.expiration_date,
                          "expirationDate")

    @unittest.skipIf(conf.url == 'http://prelive-pl-app1.litle.com:8048/services/chargebacks/',
                     "VantivException not raised by _get_response")
    def test_request_put_response(self):
        param = fields_chargeback.chargebackApiCase()
        param.caseId = u'1304283003'
        request_body = fields_chargeback.chargebackUpdateRequest()
        request_body.activityType = "ADD_NOTE"
        request_body.note = "note333"
        self.assertRaises(utils.VantivException, online._put_chargeback_update, param.caseId, request_body)

    @unittest.skipIf(conf.url == 'http://prelive-pl-app1.litle.com:8048/services/chargebacks/',
                     "VantivException not raised by _put_response")
    def test_request_post_response(self):
        param = fields_chargebackDocument.Merchant();
        param.id = u'01333078'
        param1 = fields_chargebackDocument.ChargebackCase();
        param1.id = u'01333078001'
        param2 = fields_chargebackDocument.Document()
        param2.id = u'test6_7'
        path = package_root + "/samples/000_puppy_picture.jpg"
        headertype = contentTypeEnum.ContentType.JPEG
        self.assertRaises(utils.VantivException, online._post_responses, param, param1, param2, path, headertype)


if __name__ == '__main__':
    unittest.main()
