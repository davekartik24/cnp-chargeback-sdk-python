# # -*- coding: utf-8 -*-
# # Copyright (c) 2017 Vantiv eCommerce
# #
# # Permission is hereby granted, free of charge, to any person
# # obtaining a copy of this software and associated documentation
# # files (the 'Software'), to deal in the Software without
# # restriction, including without limitation the rights to use,
# # copy, modify, merge, publish, distribute, sublicense, and/or sell
# # copies of the Software, and to permit persons to whom the
# # Software is furnished to do so, subject to the following
# # conditions:
# #
# # The above copyright notice and this permission notice shall be
# # included in all copies or substantial portions of the Software.
# #
# # THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# # EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# # OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# # NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# # HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# # WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# # FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# # OTHER DEALINGS IN THE SOFTWARE.
#
import os
import sys
import unittest2

from vantivsdk import fields_chargebackDocument, utils, online, parameters
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

conf = utils.Configuration()


class TestUploadeDocument(unittest2.TestCase):
    def test_upload_chargebackDocument(self):
        merchant_param = fields_chargebackDocument.Merchant()
        merchant_param.id = u'01333078'
        case_param = fields_chargebackDocument.ChargebackCase()
        case_param.id = u'01333078001'
        document_param = fields_chargebackDocument.Document()
        document_param.id = u'image136'
        param= parameters.Parameters()
        param.type = u'image'
        param.extension = u'jpeg'
        response = online._upload_document(merchant_param.id, case_param.id, document_param.id, param.type, param.extension)
        self.assertEquals('000', response['Document']['ResponseCode'])


if __name__ == '__main__':
    unittest2.main()
