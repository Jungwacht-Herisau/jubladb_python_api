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

from jubladb_api.models.jsonapi_error_source import JsonapiErrorSource

class TestJsonapiErrorSource(unittest.TestCase):
    """JsonapiErrorSource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonapiErrorSource:
        """Test JsonapiErrorSource
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonapiErrorSource`
        """
        model = JsonapiErrorSource()
        if include_optional:
            return JsonapiErrorSource(
                pointer = '',
                parameter = ''
            )
        else:
            return JsonapiErrorSource(
        )
        """

    def testJsonapiErrorSource(self):
        """Test JsonapiErrorSource"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
