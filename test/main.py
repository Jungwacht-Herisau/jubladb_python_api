import os
import unittest

import jubladb_api.client
import jubladb_api.metamodel

class TestBasic(unittest.TestCase):
    def setUp(self):
        self.client = jubladb_api.client.create(url=jubladb_api.metamodel.API_INFO.default_server_url,
                                                api_key=os.environ["JUBLADB_API_KEY"])
    def test_request_person(self):
        self.client.get_person(4, include=["primary_group"])