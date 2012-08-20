from scim import user
from scim import core
from scim import group
from scim import attributes
from scim import config
#import usertest
import unittest
import json




class ConfigTestCase(unittest.TestCase):
    def setUp(self):

        self.s = config.Config()
        self.s.doc_url = 'http://example.com/help/scim.html'
        self.s.patch = config.Config.Patch(
            supported=True
        )
        self.s.bulk = config.Config.Bulk(
            supported=True,
            max_operations=1000,
            max_payload=1048576
        )
        self.s.filter = config.Config.Filter(
            supported=True,
            max_results=200
        )
        self.s.change_pass = config.Config.ChangePassword(
            supported=True
        )
        self.s.sort = config.Config.Sort(
            supported=True
        )
        self.s.etag = config.Config.ETag(
            supported=True
        )
        self.s.xml_format = config.Config.XMLDataFormat(
            supported=True
        )
        self.s.auth = [
            config.Config.AuthenticationScheme(
                name='OAuth Bearer Token',
                description='Authentication Scheme',
                spec_url='http://example.com',
                doc_url='http://example.com',
                type='oauthbearertoken',
                primary=True
            ),
            config.Config.AuthenticationScheme(
                name="HTTP Basic",
                description='Authentication Scheme',
                spec_url='http://example2.com',
                doc_url='http://example2.com',
                type='httpbasic'
            )
        ]
        self.testJson = """{"sort": {"supported": true}, "filter": {"supported": true, "maxResults": 200}, "xmlDataFormat": {"supported": true}, "documentationUrl": "http://example.com/help/scim.html", "patch": {"supported": true}, "bulk": {"maxPayloadSize": 1048576, "supported": true, "maxOperations": 1000}, "etag": {"supported": true}, "authenticationSchemes": [{"type": "oauthbearertoken", "primary": true, "value": {"documentationUrl": "http://example.com", "specUrl": "http://example.com", "description": "Authentication Scheme", "name": "OAuth Bearer Token"}}, {"type": "httpbasic", "value": {"documentationUrl": "http://example2.com", "specUrl": "http://example2.com", "description": "Authentication Scheme", "name": "HTTP Basic"}}], "schemas": ["urn:scim:schemas:core:1.0"], "changePassword": {"supported": true}}"""

    def runTest(self):

        self.configJson = json.dumps(config.Config.serialize(self.s))
        print self.configJson

        #deJson = json.dumps(json.loads(self.testJson))

        self.assertEqual(self.configJson, self.testJson, "JSON's don't match")


def suite():
    """
        Gather all the tests from this module in a test suite.
    """
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(ConfigTestCase))
    test_suite.addTest(unittest.makeSuite(usertest.UserTestCase))
    return test_suite

