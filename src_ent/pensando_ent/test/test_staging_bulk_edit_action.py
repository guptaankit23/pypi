"""
    Staging API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.bulkedit_bulk_edit_action_spec import BulkeditBulkEditActionSpec
from pensando_ent.psm.model.staging_bulk_edit_action_status import StagingBulkEditActionStatus
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['BulkeditBulkEditActionSpec'] = BulkeditBulkEditActionSpec
globals()['StagingBulkEditActionStatus'] = StagingBulkEditActionStatus
from pensando_ent.psm.psm.model.staging_bulk_edit_action import StagingBulkEditAction


class TestStagingBulkEditAction(unittest.TestCase):
    """StagingBulkEditAction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStagingBulkEditAction(self):
        """Test StagingBulkEditAction"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StagingBulkEditAction()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
