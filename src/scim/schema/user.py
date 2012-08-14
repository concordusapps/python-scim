# -*- coding: utf-8 -*-
""" \file "scim/schema/core.py"
\brief "Defines the core scim schema and all its attributes"

\author Erich Healy (CactusCommander) ErichRHealy@gmail.com

\copyright Copyright © 2012 Concordus Applications, Inc.
           \n \n
           Permission is hereby granted, free of charge, to any person
           obtaining a copy of this software and associated documentation
           files (the "Software"), to deal in the Software without restriction,
           including without limitation the rights to use, copy, modify, merge,
           publish, distribute, sublicense, and/or sell copies of the Software,
           and to permit persons to whom the Software is furnished to do so,
           subject to the following conditions:
           \n \n
           The above copyright notice and this permission notice shall be
           included in all copies or substantial portions of the Software.
           \n \n
           THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
           EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
           MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
           NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
           BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
           ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
           CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
           SOFTWARE.
"""
from . import attributes


class User(attributes.Complex):
    """Defines the schema mapping for a User.
    """

    class Name(attributes.Complex):
        """Contains attributes for a fully expanded name.
        """

        class Meta:
            name = 'name'

        ## The fully formatted name containing every other name attribute
        formatted = attributes.Singular('formatted')

        ## The family name for the user.  Sometimes referred to as one's Last
        ## Name
        family = attributes.Singular('familyName')

        ## The user's given name.  Sometimes referred to as one's First Name
        given = attributes.Singular('givenName')

        ## The user's middle name
        middle = attributes.Singular('middleName')

        ## Any honorific prefixes someone might have.  Ex: Dr., Prof., Mr., etc
        prefix = attributes.Singular('honorificPrefix')

        ## Honorific suffixes.  Ex: III, Jr., Sr., etc.
        suffix = attributes.Singular('honorificSuffix')

    ## The username/login name represented in the system
    username = attributes.Singular('userName')

    ## User's proper name
    name = Name()

    ## formatted name ready for display.  This should be the primary way that a
    ## user is displayed
    display = attributes.Singular('displayName')

    ## User's nickname.  This doesn't have to be the same as username
    ## Ex: name = james -> display = jim
    nick_name = attributes.Singular('nickName')

    ## Fully qualified URL pointing to user's profile
    profile = attributes.Singular('profileUrl')

    ## User's proper title.  Ex: Professor, Vice President
    title = attributes.Singular('title')

    ## Identifies what sort of user this is.  Ex: Contractor, Employee, etc.
    user_type = attributes.Singular('userType')

    ## Concatination of ISO 639-1, an underscore, and ISO 3166-1.  Ex: en_US
    language = attributes.Singular('preferredLanguage')

    ## Concatination of ISO 639-1, an underscore, and ISO 3166-1.  Ex: en_US
    locale = attributes.Singular('locale')

    ## Timezone according to tz/IANA database.  Ex: America/Los_Angeles
    timezone = attributes.Singular('timezone')

    ## Boolean flag denoting user's admin status.  True means user is admin.
    admin = attributes.Singular('status')

    ## Password field. This really only ought to be set during a POST operation
    password = attributes.Singular('password')

    # Multi-value attributes.  These are pluralized to make it more obvious
    # that these are multi-value attribues

    class SimpleMultiValue(attributes.MultiValue):
        """TODO"""

        ## E-mail addresses for the User.
        value = attributes.Singular('value')

        def __init__(self, value=None, **kwargs):
            """TODO"""
            kwargs.update("value", value)
            attributes.MultiValue.__init__(self, **kwargs)

    class Email(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'emails'

    ## Emails the user has registered with them
    emails = Email()

    class PhoneNumber(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'phoneNumbers'

    ## Phone numbers for the User.
    phones = PhoneNumber()

    class Messanger(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'ims'

    ## Instant messaging address for the User.
    messengers = Messanger()

    class Photo(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'photos'

    ## Instant messaging address for the User.
    photos = Photo()

    ## A list of groups that the user belongs to, either thorough direct
    ## membership, nested groups, or dynamically calculated.
    # groups =

    class Role(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'roles'

    ## A list of roles for the User that collectively represent who the
    ## User is; e.g., 'Student', "Faculty".
    roles = Role()

    class Entitlement(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'entitlements'

    ## A list of entitlements for the User that represent a thing the User has.
    entitlements = Entitlement()

    class Certificate(SimpleMultiValue):
        """TODO"""
        class Meta:
            name = 'x509Certificates'

    ## A list of x.509 certificates issued to the User.
    certs = Certificate()

    class Address(attributes.MultiValue):
        """TODO
        """

        class Meta:
            name = 'addresses'

        ## The fully formatted address.
        formatted = attributes.Singular('formatted')

        ## Street, house number, apartment number, po box, etc.
        street = attributes.Singular('streetAddress')

        ## City or locality that the location is in.
        locality = attributes.Singular('locality')

        ## State or region that the location is in.
        region = attributes.Singular('region')

        ## Zip or postal code.
        code = attributes.Singular('postalCode')

        ## Country that the address is in in ISO 3166-1 format
        country = attributes.Singular('country')

    ## A physical mailing address for this User.
    addresses = Address()


#class Enterprise(Extension):
#    """
#    Defines enterprise user extensions
#    schema: urn:scim:schemas:extension:enterprise:1.0
#    """
#
#    class Manager(Complex):
#        """
#        User's Manager's primary key and name
#        """
#
#        class Meta:
#            name = 'manager'
#
#        ## Primary Key for manager
#        id = Singular('managerId')
#
#        ## Manager's name, for convenience purposes
#        name = Singular('displayName')
#
#    ## User's Employee number
#    employee_id = Singular('employeeNumber')
#
#    ## User's Cost Center (?)
#    cost_center = Singular('costCenter')
#
#    ## Organization
#    organization = Singular('organization')
#
#    ## Division of organizations
#    division = Singular('division')
#
#    ## Department of division
#    department = Singular('department')
#
#    ## User's manager
#    # TODO: allow stuff like so:
#    # x.enterprise.manager = Manager(id=32423, name="dsfsdf")
#    manager = Manager('manager')
