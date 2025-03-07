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

from jubladb_api.models.event_kinds_request import EventKindsRequest

class TestEventKindsRequest(unittest.TestCase):
    """EventKindsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EventKindsRequest:
        """Test EventKindsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EventKindsRequest`
        """
        model = EventKindsRequest()
        if include_optional:
            return EventKindsRequest(
                data = jubladb_api.models.event_kinds_resource.event_kinds_resource(
                    id = '74', 
                    type = 'event_kinds', 
                    attributes = jubladb_api.models.event_kinds.event_kinds(
                        label = '', 
                        short_name = '', 
                        general_information = '', 
                        application_conditions = '', 
                        minimum_age = 56, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), ), 
                    relationships = jubladb_api.models.event_kinds_relationships.event_kinds_relationships(
                        kind_category = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(
                            links = { }, 
                            data = jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                                type = 'additional_emails', 
                                meta = { }, 
                                id = '44', ), 
                            meta = { }, ), ), 
                    links = {
                        'key' : null
                        }, )
            )
        else:
            return EventKindsRequest(
        )
        """

    def testEventKindsRequest(self):
        """Test EventKindsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
