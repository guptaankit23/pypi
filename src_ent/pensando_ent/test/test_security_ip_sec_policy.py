"""
    Security API reference

       # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.security_ip_sec_policy_spec import SecurityIPSecPolicySpec
from pensando_ent.psm.model.security_ip_sec_policy_status import SecurityIPSecPolicyStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['SecurityIPSecPolicySpec'] = SecurityIPSecPolicySpec
globals()['SecurityIPSecPolicyStatus'] = SecurityIPSecPolicyStatus
from pensando_ent.psm.psm.model.security_ip_sec_policy import SecurityIPSecPolicy


class TestSecurityIPSecPolicy(unittest.TestCase):
    """SecurityIPSecPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSecurityIPSecPolicy(self):
        """Test SecurityIPSecPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SecurityIPSecPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
