"""
    Auth API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.auth_role_binding_spec import AuthRoleBindingSpec
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['AuthRoleBindingSpec'] = AuthRoleBindingSpec
from pensando_ent.psm.psm.model.auth_role_binding import AuthRoleBinding


class TestAuthRoleBinding(unittest.TestCase):
    """AuthRoleBinding unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthRoleBinding(self):
        """Test AuthRoleBinding"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthRoleBinding()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
