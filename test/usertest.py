from scim import user
from scim import config
from scim import core
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


class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.u = user.User(
            name=user.User.Name(
                formatted="Ms. Barbara J Jensen III",
                given="Barbara",
                family="Jensen",
                middle="Jane",
                prefix="Ms.",
                suffix="III"
            ),
        )
        self.u.username = "bjensen@example.com"
        self.u.display = "Babs Jensen"
        self.u.nick_name = "Babs"
        self.u.profile = "https://login.example.com/bjensen"
        self.u.emails = [
            user.User.Email(
                primary=True,
                type='work',
                value='bejensen@example.com'
            ),
            user.User.Email(
                 type='home',
                 value='babs@jensen.org'
            )
        ]
        self.u.addresses = [
            user.User.Address(
                primary=True,
                type='work',
                street='100 Universal City Plaza',
                locality='Hollywood',
                region='CA',
                code='91608',
                country='USA',
                fomrated='100 Universal City Plaza Hollywood, CA 91608 USA'
            ),
            user.User.Address(
                type='home',
                street='456 Hollywood Blvd',
                locality='Hollywood',
                region='CA',
                code='91608',
                country='USA',
                formatted="456 Hollywood Blvd Hollywood, CA 91608 USA"
            )
        ]
        self.u.phones = [
            user.User.PhoneNumber(
                value="555-555-5555",
                type='work'
            ),
            user.User.PhoneNumber(
                value='444-444-4444',
                type='mobile'
            )
        ]
        self.u.messengers = [
            user.User.Messanger(
                value='someaimhandle',
                type='aim'
            )
        ]
        self.u.photos = [
            user.User.Photo(
                value='https://photos.example.com/profilephoto/72930000000Ccne/F',
                type='photo'
            ),
            user.User.Photo(
                value='https://photos.example.com/profilephoto/72930000000Ccne/T',
                type='thumbnail'
            )
        ]
        self.u.user_type = 'Employee'
        self.u.title = 'Tour Guide'
        self.u.language = 'en_US'
        self.u.locale = 'en_US'
        self.u.timezone = 'America/Los_Angeles'

        self.u.password = 't1meMa$heen'
        self.u.groups = [
            user.User.Group(
                display='Tour Guides',
                value='00300000005N2Y6AA'
            ),
            user.User.Group(
                display='Employees',
                value='00300000005N34H78'
            ),
            user.User.Group(
                display="US Employees",
                value='00300000005N98YT1'
            )
        ]
        self.u.certs = [
            user.User.Certificate(
                value="""333"""
            )
        ]
        self.u.meta = (
            core.Core.Metadata(
                created="2010-01-23T04:56:22Z",
                modified="2011-05-13T04:42:34Z",
                version="1",
                location="https://example.com/v1/Users/2819c223-7f76-453a-919d-413861904646"
            )
        )
        self.u.id = "2819c223-7f76-453a-919d-413861904646"
        self.u.external_id = "701984"
        self.testJson = """{"phoneNumbers": [{"type": "work", "value": "555-555-5555"}, {"type": "mobile", "value": "444-444-4444"}], "addresses": [{"type": "work", "primary": true, "value": {"postalCode": "91608", "country": "USA", "region": "CA", "streetAddress": "100 Universal City Plaza", "locality": "Hollywood"}}, {"type": "home", "value": {"locality": "Hollywood", "country": "USA", "region": "CA", "formatted": "456 Hollywood Blvd Hollywood, CA 91608 USA", "streetAddress": "456 Hollywood Blvd", "postalCode": "91608"}}], "x509Certificates": [{"value": "333"}], "userType": "Employee", "meta": {"lastModified": "2011-05-13T04:42:34Z", "version": "1", "location": "https://example.com/v1/Users/2819c223-7f76-453a-919d-413861904646", "created": "2010-01-23T04:56:22Z"}, "timezone": "America/Los_Angeles", "id": "2819c223-7f76-453a-919d-413861904646", "schemas": ["urn:scim:schemas:core:1.0"], "title": "Tour Guide", "preferredLanguage": "en_US", "locale": "en_US", "ims": [{"type": "aim", "value": "someaimhandle"}], "externalId": "701984", "nickName": "Babs", "photos": [{"type": "photo", "value": "https://photos.example.com/profilephoto/72930000000Ccne/F"}, {"type": "thumbnail", "value": "https://photos.example.com/profilephoto/72930000000Ccne/T"}], "groups": [{"display": "Tour Guides", "value": "00300000005N2Y6AA"}, {"display": "Employees", "value": "00300000005N34H78"}, {"display": "US Employees", "value": "00300000005N98YT1"}], "password": "t1meMa$heen", "emails": [{"type": "work", "primary": true, "value": "bejensen@example.com"}, {"type": "home", "value": "babs@jensen.org"}], "userName": "bjensen@example.com", "displayName": "Babs Jensen", "name": {"honorificPrefix": "Ms.", "middleName": "Jane", "familyName": "Jensen", "formatted": "Ms. Barbara J Jensen III", "givenName": "Barbara", "honorificSuffix": "III"}, "profileUrl": "https://login.example.com/bjensen"}"""

    def runTest(self):

        self.userJson = json.dumps(user.User.serialize(self.u))
        print self.userJson

        #deJson = json.dumps(json.loads(self.testJson))

        self.assertEqual(self.userJson, self.testJson, "JSON's don't match")
