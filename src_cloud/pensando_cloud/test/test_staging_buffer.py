"""
    Staging API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_cloud.psm.model.api_object_meta import ApiObjectMeta
from pensando_cloud.psm.model.staging_buffer_spec import StagingBufferSpec
from pensando_cloud.psm.model.staging_buffer_status import StagingBufferStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['StagingBufferSpec'] = StagingBufferSpec
globals()['StagingBufferStatus'] = StagingBufferStatus
from pensando_cloud.psm.psm.model.staging_buffer import StagingBuffer


class TestStagingBuffer(unittest.TestCase):
    """StagingBuffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStagingBuffer(self):
        """Test StagingBuffer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StagingBuffer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
