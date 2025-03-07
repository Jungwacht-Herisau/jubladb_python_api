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

from jubladb_api.models.people_collection import PeopleCollection

class TestPeopleCollection(unittest.TestCase):
    """PeopleCollection unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PeopleCollection:
        """Test PeopleCollection
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeopleCollection`
        """
        model = PeopleCollection()
        if include_optional:
            return PeopleCollection(
                data = [
                    jubladb_api.models.people_resource.people_resource(
                        id = '99', 
                        type = 'people', 
                        attributes = jubladb_api.models.people.people(
                            first_name = '', 
                            last_name = '', 
                            nickname = '', 
                            company_name = '', 
                            company = True, 
                            email = '', 
                            address = '', 
                            zip_code = '', 
                            town = '', 
                            country = '', 
                            primary_group_id = 56, 
                            gender = '', 
                            birthday = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                            language = '', ), 
                        relationships = jubladb_api.models.people_relationships.people_relationships(
                            primary_group = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(
                                links = { }, 
                                data = jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                                    type = 'additional_emails', 
                                    meta = { }, 
                                    id = '44', ), 
                                meta = { }, ), 
                            layer_group = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(), 
                            roles = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(), 
                            phone_numbers = jubladb_api.models.courses_relationships_dates.courses_relationships_dates(), 
                            social_accounts = , 
                            additional_emails = , ), 
                        links = {
                            'key' : null
                            }, )
                    ],
                included = [
                    jubladb_api.models.jsonapi_resource.jsonapi_resource()
                    ],
                meta = { },
                links = None,
                jsonapi = jubladb_api.models.jsonapi_jsonapi.jsonapi_jsonapi(
                    version = '1.0', 
                    meta = { }, )
            )
        else:
            return PeopleCollection(
        )
        """

    def testPeopleCollection(self):
        """Test PeopleCollection"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
