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
from pensando_cloud.psm_cloud.model.monitoring_alert_spec import MonitoringAlertSpec
from pensando_cloud.psm_cloud.model.monitoring_alert_status import MonitoringAlertStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringAlertSpec'] = MonitoringAlertSpec
globals()['MonitoringAlertStatus'] = MonitoringAlertStatus
from pensando_cloud.psm_cloud.psm_cloud.model.monitoring_alert import MonitoringAlert


class TestMonitoringAlert(unittest.TestCase):
    """MonitoringAlert unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringAlert(self):
        """Test MonitoringAlert"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringAlert()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()