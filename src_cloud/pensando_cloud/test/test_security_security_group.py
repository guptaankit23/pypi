"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.security_security_group_spec import SecuritySecurityGroupSpec
from pensando_cloud.psm_cloud.model.security_security_group_status import SecuritySecurityGroupStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['SecuritySecurityGroupSpec'] = SecuritySecurityGroupSpec
globals()['SecuritySecurityGroupStatus'] = SecuritySecurityGroupStatus
from pensando_cloud.psm_cloud.psm_cloud.model.security_security_group import SecuritySecurityGroup


class TestSecuritySecurityGroup(unittest.TestCase):
    """SecuritySecurityGroup unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecuritySecurityGroup(self):
        """Test SecuritySecurityGroup"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecuritySecurityGroup()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()