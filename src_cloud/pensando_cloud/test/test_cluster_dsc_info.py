"""
    Cluster API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.cluster_bios_info import ClusterBiosInfo
from pensando_cloud.psm.model.cluster_cpu_info import ClusterCPUInfo
from pensando_cloud.psm.model.cluster_mem_info import ClusterMemInfo
from pensando_cloud.psm.model.cluster_os_info import ClusterOsInfo
from pensando_cloud.psm.model.cluster_storage_info import ClusterStorageInfo
globals()['ClusterBiosInfo'] = ClusterBiosInfo
globals()['ClusterCPUInfo'] = ClusterCPUInfo
globals()['ClusterMemInfo'] = ClusterMemInfo
globals()['ClusterOsInfo'] = ClusterOsInfo
globals()['ClusterStorageInfo'] = ClusterStorageInfo
from pensando_cloud.psm.psm.model.cluster_dsc_info import ClusterDSCInfo


class TestClusterDSCInfo(unittest.TestCase):
    """ClusterDSCInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testClusterDSCInfo(self):
        """Test ClusterDSCInfo"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ClusterDSCInfo()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
