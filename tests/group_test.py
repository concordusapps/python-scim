from scim import group
import unittest
import json


class GroupTestCase(unittest.TestCase):
    def setUp(self):

        self.s = group.Group()
        self.s.id = "235"
        self.s.name = "some name"
        self.s.members = [
            group.Group.Members(
                value='666',
                display='babs jensen'
            ),
            group.Group.Members(
                value='977',
                display='mandy pepperidge'
            )
        ]
        self.testJson = """{"displayName": "some name", "id": "235", "members": [{"display": "babs jensen", "value": "666"}, {"display": "mandy pepperidge", "value": "977"}], "schemas": ["urn:scim:schemas:core:1.0"]}"""

    def runTest(self):

        self.groupJson = json.dumps(group.Group.serialize(self.s))
        print self.groupJson

        self.assertEqual(self.groupJson, self.testJson, "JSON's don't match")


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(GroupTestCase))
    return test_suite

