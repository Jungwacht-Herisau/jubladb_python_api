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

from jubladb_api.models.invoices import Invoices

class TestInvoices(unittest.TestCase):
    """Invoices unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Invoices:
        """Test Invoices
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Invoices`
        """
        model = Invoices()
        if include_optional:
            return Invoices(
                title = '',
                description = '',
                state = '',
                group_id = 56,
                recipient_id = 56,
                due_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                issued_at = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                recipient_email = '',
                payment_information = '',
                payment_purpose = '',
                hide_total = True
            )
        else:
            return Invoices(
        )
        """

    def testInvoices(self):
        """Test Invoices"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
