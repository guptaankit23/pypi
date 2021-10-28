"""
    Search API reference

    Service name    # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import psm
from pensando_cloud.psm.api.search_v1_api import SearchV1Api  # noqa: E501


class TestSearchV1Api(unittest.TestCase):
    """SearchV1Api unit test stubs"""

    def setUp(self):
        self.api = SearchV1Api()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_policy_query1(self):
        """Test case for get_policy_query1

        Security Policy Query  # noqa: E501
        """
        pass

    def test_get_query1(self):
        """Test case for get_query1

        Structured or free-form search  # noqa: E501
        """
        pass

    def test_post_policy_query(self):
        """Test case for post_policy_query

        Security Policy Query  # noqa: E501
        """
        pass

    def test_post_query(self):
        """Test case for post_query

        Structured or free-form search  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
