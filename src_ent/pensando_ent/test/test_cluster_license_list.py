"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_list_meta import ApiListMeta
from pensando_ent.psm.model.cluster_license import ClusterLicense
globals()['ApiListMeta'] = ApiListMeta
globals()['ClusterLicense'] = ClusterLicense
from pensando_ent.psm.psm.model.cluster_license_list import ClusterLicenseList


class TestClusterLicenseList(unittest.TestCase):
    """ClusterLicenseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterLicenseList(self):
        """Test ClusterLicenseList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterLicenseList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
