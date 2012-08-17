from scim import user
from scim import core
from scim import group
from scim import attributes
from scim import schema
import unittest
import json




class SchemaTestCase(unittest.TestCase):
    def setUp(self):

        self.s = schema.Schema()

        self.s.attributes = [
            schema.Schema.Attributes(
                name='id',
                type='string',
                multi_valued=False,
                description='Unique',
                schema="urn:scim:schemas:core:1.0",
                read_only=True,
                required=True,
                case_exact=True
            ),
            schema.Schema.Attributes(
                name='name',
                type='complex',
                multi_valued=True,
                description='something',
                schema='urn:scim:schemas:core:1.0',
                read_only=False,
                required=False,
                case_exact=False,
                sub_attributes=[
                    schema.Schema.Attributes.SubAttributes(
                        name='value',
                        type='string',
                        multi_valued=False,
                        desciption='Email',
                        read_only=False,
                        required=False,
                        case_exact=False
                    ),
                    schema.Schema.Attributes.SubAttributes(
                        name='display',
                        type='string',
                        multi_valued=False,
                        description='A human readable name',
                        read_only=True,
                        required=False,
                        case_exact=False
                    )
                ]
            )
        ]
        self.testJson = """{"attributes": [{"type": "string", "value": {"description": "Unique", "required": true, "caseExact": true, "readOnly": true, "multiValued": false, "schema": "urn:scim:schemas:core:1.0", "name": "id"}}, {"type": "complex", "value": {"subAttributes": [{"type": "string", "value": {"readOnly": false, "required": false, "caseExact": false, "name": "value"}}, {"type": "string", "value": {"readOnly": true, "required": false, "caseExact": false, "name": "display", "description": "A human readable name"}}], "description": "something", "required": false, "caseExact": false, "readOnly": false, "multiValued": true, "schema": "urn:scim:schemas:core:1.0", "name": "name"}}], "schemas": ["urn:scim:schemas:core:1.0"]}"""

    def runTest(self):

        self.schemaJson = json.dumps(schema.Schema.serialize(self.s))
        print self.schemaJson

        #deJson = json.dumps(json.loads(self.testJson))

        self.assertEqual(self.schemaJson, self.testJson, "JSON's don't match")
