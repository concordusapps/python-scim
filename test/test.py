from scim import user
from scim import usertest

u = user.User(
    name=user.User.Name(
        formatted="Sir Jones",
        given="Jones"
    ),
)

u.username = "blob"

u.emails = [
    user.User.Email(
        primary=True,
        type='home',
        value='leckey.ryan@gmail.com'
    ),
    user.User.Email('rleckey@concordusapps.com')
]

u.addresses = [
    user.User.Address(
        primary=True,
        type="Work",
        street="123 Nowhere Ave.",
        locality="Fruit"
    )
]

import json
d = json.dumps(user.User.serialize(u), indent=2)
print(d)
print('-----------------')

d = """
{
  "userName": "blob",
  "schemas": [
    "urn:scim:schemas:core:1.0"
  ],
  "addresses": [
    {
      "type": "Work",
      "primary": true,
      "streetAddress": "123 Nowhere Ave.",
      "locality": "Fruit"
    }
  ],
  "name": {
    "givenName": "Jones",
    "formatted": "Sir Jones"
  },
  "emails": [
    {
      "type": "home",
      "primary": true,
      "value": "leckey.ryan@gmail.com"
    },
    "rleckey@concordusapps.com"
  ]
}
"""


e = json.loads(d)
x = user.User.deserialize(e)

assert x is not None
print(vars(x))
print('-----------------')
y = json.dumps(user.User.serialize(x), indent=2)
print(y)
