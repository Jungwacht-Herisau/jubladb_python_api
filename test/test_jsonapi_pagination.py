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

from jubladb_api.models.jsonapi_pagination import JsonapiPagination

class TestJsonapiPagination(unittest.TestCase):
    """JsonapiPagination unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonapiPagination:
        """Test JsonapiPagination
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonapiPagination`
        """
        model = JsonapiPagination()
        if include_optional:
            return JsonapiPagination(
                first = None,
                last = None,
                prev = None,
                next = None
            )
        else:
            return JsonapiPagination(
        )
        """

    def testJsonapiPagination(self):
        """Test JsonapiPagination"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
