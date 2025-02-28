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

from jubladb_api.models.jsonapi_data import JsonapiData

class TestJsonapiData(unittest.TestCase):
    """JsonapiData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonapiData:
        """Test JsonapiData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonapiData`
        """
        model = JsonapiData()
        if include_optional:
            return JsonapiData(
                id = '90',
                type = 'social_accounts',
                attributes = jubladb_api.models.social_accounts.social_accounts(
                    label = '', 
                    public = True, 
                    contactable_id = 56, 
                    contactable_type = '', 
                    name = '', ),
                relationships = jubladb_api.models.relationships.relationships(),
                links = {
                    'key' : null
                    }
            )
        else:
            return JsonapiData(
        )
        """

    def testJsonapiData(self):
        """Test JsonapiData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
