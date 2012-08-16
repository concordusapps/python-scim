from scim import user
from scim import core
from scim import group
from scim import attributes
import unittest
import json




class JSONTestCase(unittest.TestCase):
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
        self.u.user_type='Employee'
        self.u.title='Tour Guide'
        self.u.language='en_US'
        self.u.locale='en_US'
        self.u.timezone='America/Los_Angeles'
        
        self.u.password='t1meMa$heen'
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
        self.u.meta= (
            core.Core.Metadata(
                created="2010-01-23T04:56:22Z",
                modified="2011-05-13T04:42:34Z",
                version="1",
                location="https://example.com/v1/Users/2819c223-7f76-453a-919d-413861904646"
            )
        )
        self.u.id="2819c223-7f76-453a-919d-413861904646"
        self.u.external_id="701984"
        self.testJson = """{"phoneNumbers": [{"type": "work", "value": "555-555-5555"}, {"type": "mobile", "value": "444-444-4444"}], "addresses": [{"type": "work", "primary": true, "value": {"postalCode": "91608", "country": "USA", "region": "CA", "streetAddress": "100 Universal City Plaza", "locality": "Hollywood"}}, {"type": "home", "value": {"locality": "Hollywood", "country": "USA", "region": "CA", "formatted": "456 Hollywood Blvd Hollywood, CA 91608 USA", "streetAddress": "456 Hollywood Blvd", "postalCode": "91608"}}], "x509Certificates": [{"value": "333"}], "userType": "Employee", "meta": {"lastModified": "2011-05-13T04:42:34Z", "version": "1", "location": "https://example.com/v1/Users/2819c223-7f76-453a-919d-413861904646", "created": "2010-01-23T04:56:22Z"}, "timezone": "America/Los_Angeles", "id": "2819c223-7f76-453a-919d-413861904646", "schemas": ["urn:scim:schemas:core:1.0"], "title": "Tour Guide", "preferredLanguage": "en_US", "locale": "en_US", "ims": [{"type": "aim", "value": "someaimhandle"}], "externalId": "701984", "nickName": "Babs", "photos": [{"type": "photo", "value": "https://photos.example.com/profilephoto/72930000000Ccne/F"}, {"type": "thumbnail", "value": "https://photos.example.com/profilephoto/72930000000Ccne/T"}], "groups": [{"display": "Tour Guides", "value": "00300000005N2Y6AA"}, {"display": "Employees", "value": "00300000005N34H78"}, {"display": "US Employees", "value": "00300000005N98YT1"}], "password": "t1meMa$heen", "emails": [{"type": "work", "primary": true, "value": "bejensen@example.com"}, {"type": "home", "value": "babs@jensen.org"}], "userName": "bjensen@example.com", "displayName": "Babs Jensen", "name": {"honorificPrefix": "Ms.", "middleName": "Jane", "familyName": "Jensen", "formatted": "Ms. Barbara J Jensen III", "givenName": "Barbara", "honorificSuffix": "III"}, "profileUrl": "https://login.example.com/bjensen"}"""

    def runTest(self):
        
        self.userJson = json.dumps(user.User.serialize(self.u))
        print self.userJson
        
        #deJson = json.dumps(json.loads(self.testJson))
        
        self.assertEqual(self.userJson, self.testJson,"JSON's don't match")
