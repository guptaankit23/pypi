"""
    Events API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import psm
from pensando_ent.psm.model.api_object_meta import ApiObjectMeta
from pensando_ent.psm.model.api_object_ref import ApiObjectRef
from pensando_ent.psm.model.events_event_source import EventsEventSource
globals()['ApiObjectMeta'] = ApiObjectMeta
globals()['ApiObjectRef'] = ApiObjectRef
globals()['EventsEventSource'] = EventsEventSource
from pensando_ent.psm.psm.model.events_event import EventsEvent


class TestEventsEvent(unittest.TestCase):
    """EventsEvent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEventsEvent(self):
        """Test EventsEvent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EventsEvent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
