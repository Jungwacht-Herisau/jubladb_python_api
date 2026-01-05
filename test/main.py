import os
import unittest

import jubladb_api.client
import jubladb_api.metamodel

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.client = jubladb_api.client.create(url=jubladb_api.metamodel.API_INFO.default_server_url,
                                                api_key=os.environ["JUBLADB_API_KEY"])
    def test_request_person(self):
        person: jubladb_api.client.Person = self.client.get_person(40822, include=["primary_group"])
        group = self.client.get_group(person.primary_group)
        print(person.first_name, person.last_name, "is in", group.name)

        self.assertFalse(person.is_relation_loaded("phone_numbers"))

        person = self.client.get_person(40822, include=["phone_numbers"])

        self.assertTrue(person.is_relation_loaded("primary_group"))
        self.assertTrue(person.is_relation_loaded("phone_numbers"))

        self.assertGreater(len(person.phone_numbers), 0)