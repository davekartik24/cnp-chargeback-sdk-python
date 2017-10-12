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
from vantivsdk import fields
from vantivsdk import utils
from vantivsdk import online
package_root = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
sys.path.insert(0, package_root)

import pyxb

conf = utils.Configuration()


class TestActivityDate(unittest2.TestCase):
    def test_get_activity_date(self):
        param = fields.chargebackApiActivity()
        param.activityDate = u'2017-10-11'
        response = online._get_activity_date(param.activityDate)
       # self.assertEquals('1304283001', response['chargebackCase']['caseId'])


if __name__ == '__main__':
    unittest2.main()
