import os
import unittest

import jubladb_api.client
import jubladb_api.const
import jubladb_api.metamodel
from test import test_base


class TestBasic(unittest.TestCase):
    def setUp(self):
        self.client = test_base.test_create_api_client()

    def test_request_schar(self):
        schar = self.client.get_group(test_base.TEST_SCHAR_ID)
        self.assertEqual(test_base.TEST_SCHAR_ID, schar.id)
        self.assertEqual("Testschar jubladb_python_api", schar.name)

    def test_request_roles(self):
        roles = self.client.get_roles_list(filter_group_id_eq=test_base.TEST_SCHAR_ID)
        flock_leader_roles = list(filter(lambda ro: ro.type==jubladb_api.const.ROLE_FLOCK_LEADER.id, roles))
        self.assertEqual(1, len(flock_leader_roles))

    def test_request_events(self):
        events = self.client.get_events_list(filter_group_id_eq=test_base.TEST_SCHAR_ID)
        self.assertEqual(200, len(events))