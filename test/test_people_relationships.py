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

from jubladb_api.models.people_relationships import PeopleRelationships

class TestPeopleRelationships(unittest.TestCase):
    """PeopleRelationships unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeopleRelationships:
        """Test PeopleRelationships
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeopleRelationships`
        """
        model = PeopleRelationships()
        if include_optional:
            return PeopleRelationships(
                primary_group = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(
                    links = { }, 
                    data = jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                        type = 'additional_emails', 
                        meta = { }, 
                        id = '44', ), 
                    meta = { }, ),
                layer_group = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(
                    links = { }, 
                    data = jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                        type = 'additional_emails', 
                        meta = { }, 
                        id = '44', ), 
                    meta = { }, ),
                roles = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(
                    links = { }, 
                    data = [
                        jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                            type = 'additional_emails', 
                            meta = { }, 
                            id = '44', )
                        ], 
                    meta = { }, ),
                phone_numbers = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(
                    links = { }, 
                    data = [
                        jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                            type = 'additional_emails', 
                            meta = { }, 
                            id = '44', )
                        ], 
                    meta = { }, ),
                social_accounts = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(
                    links = { }, 
                    data = [
                        jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                            type = 'additional_emails', 
                            meta = { }, 
                            id = '44', )
                        ], 
                    meta = { }, ),
                additional_emails = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(
                    links = { }, 
                    data = [
                        jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                            type = 'additional_emails', 
                            meta = { }, 
                            id = '44', )
                        ], 
                    meta = { }, )
            )
        else:
            return PeopleRelationships(
        )
        """

    def testPeopleRelationships(self):
        """Test PeopleRelationships"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
