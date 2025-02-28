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

from jubladb_api.models.roles_single import RolesSingle

class TestRolesSingle(unittest.TestCase):
    """RolesSingle unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RolesSingle:
        """Test RolesSingle
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RolesSingle`
        """
        model = RolesSingle()
        if include_optional:
            return RolesSingle(
                data = jubladb_api.models.roles_resource.roles_resource(
                    id = '93', 
                    type = 'roles', 
                    attributes = jubladb_api.models.roles.roles(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        start_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        end_on = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        person_id = 56, 
                        group_id = 56, 
                        type = '', 
                        label = '', ), 
                    relationships = jubladb_api.models.roles_relationships.roles_relationships(
                        person = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(
                            links = { }, 
                            data = jubladb_api.models.jsonapi_linkage.jsonapi_linkage(
                                type = 'additional_emails', 
                                meta = { }, 
                                id = '44', ), 
                            meta = { }, ), 
                        group = jubladb_api.models.courses_relationships_contact.courses_relationships_contact(), 
                        layer_group = , ), 
                    links = {
                        'key' : null
                        }, ),
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
            return RolesSingle(
        )
        """

    def testRolesSingle(self):
        """Test RolesSingle"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
