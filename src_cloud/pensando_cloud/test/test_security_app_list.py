"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_list_meta import ApiListMeta
from pensando_cloud.psm.model.security_app import SecurityApp
globals()['ApiListMeta'] = ApiListMeta
globals()['SecurityApp'] = SecurityApp
from pensando_cloud.psm.psm.model.security_app_list import SecurityAppList


class TestSecurityAppList(unittest.TestCase):
    """SecurityAppList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityAppList(self):
        """Test SecurityAppList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityAppList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
