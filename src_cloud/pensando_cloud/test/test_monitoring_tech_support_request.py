"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm_cloud
from pensando_cloud.psm_cloud.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm_cloud.model.monitoring_tech_support_request_spec import MonitoringTechSupportRequestSpec
from pensando_cloud.psm_cloud.model.monitoring_tech_support_request_status import MonitoringTechSupportRequestStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringTechSupportRequestSpec'] = MonitoringTechSupportRequestSpec
globals()['MonitoringTechSupportRequestStatus'] = MonitoringTechSupportRequestStatus
from pensando_cloud.psm_cloud.psm_cloud.model.monitoring_tech_support_request import MonitoringTechSupportRequest


class TestMonitoringTechSupportRequest(unittest.TestCase):
    """MonitoringTechSupportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringTechSupportRequest(self):
        """Test MonitoringTechSupportRequest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringTechSupportRequest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()