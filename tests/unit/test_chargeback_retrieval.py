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
from collections import OrderedDict

import mock

from cnpsdk import (utils, chargeback_retrieval)

package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)
conf = utils.Configuration()


class TestChargebackRetrieval(unittest.TestCase):

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_case_id(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'00000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargeback_by_case_id("123456")
        expected_url_suffix = "/chargebacks/123456"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("123456", response["chargebackCase"][0]["caseId"])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_token(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargebacks_by_token("10000")
        expected_url_suffix = "/chargebacks?token=10000"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("10000", response["chargebackCase"][0]["token"])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_card_number(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargebacks_by_card_number("1111000011110000", "01-18")
        expected_url_suffix = "/chargebacks?cardNumber=1111000011110000&expirationDate=01-18"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("0000", response["chargebackCase"][0]["cardNumberLast4"])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_arn(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'111111'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargebacks_by_arn("111111")
        expected_url_suffix = "/chargebacks?arn=111111"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertEquals("111111", response["chargebackCase"][0]["acquirerReferenceNumber"])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_activity_date(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargebacks_by_date("2018-01-01")
        expected_url_suffix = "/chargebacks?date=2018-01-01"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertTrue("chargebackCase" in response)
        self.assertTrue("caseId" in response["chargebackCase"][0])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_financial_impact(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_chargebacks_by_financial_impact("2018-01-01", True)
        expected_url_suffix = "/chargebacks?date=2018-01-01&financialOnly=True"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertTrue("chargebackCase" in response)
        self.assertTrue("caseId" in response["chargebackCase"][0])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_get_actionable(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.return_value = OrderedDict(
            [(u'@xmlns', u'http://www.vantivcnp.com/chargebacks'), (u'transactionId', u'1234567890'), (
                u'chargebackCase', [OrderedDict(
                    [(u'caseId', u'123456'), (u'merchantId', u'Merchant01'), (u'dayIssuedByBank', u'2018-01-01'),
                     (u'dateReceivedByVantivCnp', u'2018-01-01'), (u'vantivCnpTxnId', u'21200000820903'),
                     (u'cycle', u'First Chargeback'), (u'orderId', u'TEST02.2'), (u'cardNumberLast4', u'0000'),
                     (u'cardType', u'MC'), (u'chargebackAmount', u'2002'), (u'chargebackCurrencyType', u'USD'),
                     (u'originalTxnDay', u'2018-01-01'), (u'chargebackType', u'D'), (u'representedAmount', u'2002'),
                     (u'representedCurrencyType', u'USD'), (u'reasonCode', u'4837'),
                     (u'reasonCodeDescription', u'No Cardholder Authorization'), (u'currentQueue', u'Network Assumed'),
                     (u'fraudNotificationStatus', u'AFTER'), (u'acquirerReferenceNumber', u'000000000'),
                     (u'chargebackReferenceNumber', u'00143789'), (u'merchantTxnId', u'600001'),
                     (u'fraudNotificationDate', u'2018-01-01'), (u'bin', u'532499'), (u'token', u'10000'),
                     (u'historicalWinPercentage', u'80'), (u'customerId', u'123abc'), (u'paymentAmount', u'3099'),
                     (u'replyByDay', u'2018-01-01'), (u'activity', [OrderedDict(
                        [(u'activityDate', u'2018-01-01'), (u'activityType', u'Assign To User'),
                         (u'fromQueue', u'Vantiv'),
                         (u'toQueue', u'Merchant'), (u'settlementAmount', u'2002'), (u'settlementCurrencyType', u'USD'),
                         (u'notes', u'notes on activity')])])])])])
        response = chargeback_retrieval.get_actionable_chargebacks(True)
        expected_url_suffix = "/chargebacks?actionable=True"
        mock_http_get_retrieval_request.assert_called_with(expected_url_suffix, mock.ANY)
        self.assertTrue("chargebackCase" in response)
        self.assertTrue("caseId" in response["chargebackCase"][0])

    @mock.patch('cnpsdk.communication.http_get_retrieval_request')
    def test_error_response(self, mock_http_get_retrieval_request):
        mock_http_get_retrieval_request.side_effect = utils.ChargebackError("Error")
        self.assertRaises(utils.ChargebackError, chargeback_retrieval.get_chargeback_by_case_id, "00")


if __name__ == '__main__':
    unittest.main()