# coding: utf-8

"""
    Hitobito JSON:API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: info@hitobito.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from jubladb_api.models.additional_emails_single_links import AdditionalEmailsSingleLinks

class TestAdditionalEmailsSingleLinks(unittest.TestCase):
    """AdditionalEmailsSingleLinks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AdditionalEmailsSingleLinks:
        """Test AdditionalEmailsSingleLinks
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AdditionalEmailsSingleLinks`
        """
        model = AdditionalEmailsSingleLinks()
        if include_optional:
            return AdditionalEmailsSingleLinks(
                first = None,
                last = None,
                prev = None,
                next = None
            )
        else:
            return AdditionalEmailsSingleLinks(
        )
        """

    def testAdditionalEmailsSingleLinks(self):
        """Test AdditionalEmailsSingleLinks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
