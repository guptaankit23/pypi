"""
    Monitoring API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.monitoring_event_policy_spec import MonitoringEventPolicySpec
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['MonitoringEventPolicySpec'] = MonitoringEventPolicySpec
from pensando_ent.psm.psm.model.monitoring_event_policy import MonitoringEventPolicy


class TestMonitoringEventPolicy(unittest.TestCase):
    """MonitoringEventPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testMonitoringEventPolicy(self):
        """Test MonitoringEventPolicy"""
        # FIXME: construct object with mandatory attributes with example values
        # model = MonitoringEventPolicy()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
