"""
    Sysruntime API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_dss.psm.model.sysruntime_conn_track_info import SysruntimeConnTrackInfo
from pensando_dss.psm.model.sysruntime_flow_info import SysruntimeFlowInfo
from pensando_dss.psm.model.sysruntime_telemetry_info import SysruntimeTelemetryInfo
globals()['SysruntimeConnTrackInfo'] = SysruntimeConnTrackInfo
globals()['SysruntimeFlowInfo'] = SysruntimeFlowInfo
globals()['SysruntimeTelemetryInfo'] = SysruntimeTelemetryInfo
from pensando_dss.psm.psm.model.sysruntime_flow_data import SysruntimeFlowData


class TestSysruntimeFlowData(unittest.TestCase):
    """SysruntimeFlowData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSysruntimeFlowData(self):
        """Test SysruntimeFlowData"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SysruntimeFlowData()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()