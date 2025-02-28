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

from jubladb_api.models.courses import Courses

class TestCourses(unittest.TestCase):
    """Courses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Courses:
        """Test Courses
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Courses`
        """
        model = Courses()
        if include_optional:
            return Courses(
                group_ids = 56,
                type = '',
                kind_id = 56,
                name = '',
                description = '',
                application_conditions = '',
                motto = '',
                cost = '',
                location = '',
                application_opening_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                application_closing_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                application_contact_id = 56,
                external_application_link = '',
                maximum_participants = 56,
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                state = '',
                training_days = 1.337,
                applicant_count = 56,
                participant_count = 56,
                minimum_participants = 56,
                number = '',
                teamer_count = 56
            )
        else:
            return Courses(
        )
        """

    def testCourses(self):
        """Test Courses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
