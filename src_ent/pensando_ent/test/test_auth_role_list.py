"""
    Auth API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_list_meta import ApiListMeta
from pensando_ent.psm.model.auth_role import AuthRole
globals()['ApiListMeta'] = ApiListMeta
globals()['AuthRole'] = AuthRole
from pensando_ent.psm.psm.model.auth_role_list import AuthRoleList


class TestAuthRoleList(unittest.TestCase):
    """AuthRoleList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAuthRoleList(self):
        """Test AuthRoleList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AuthRoleList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
