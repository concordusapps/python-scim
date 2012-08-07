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
from . import core, Extension
from .attributes import Singular, MultiValue, Complex


class User(core.Core):
    """
    Defines the schema mapping for a User
    """

    class Name(Complex):
        """
        Contains attributes for a fully expanded name
        """

        ## The fully formatted name containing every other name attribute
        formatted = Singular('formatted')

        ## The family name for the user.  Sometimes referred to as one's Last
        ## Name
        family = Singular('familyName')

        ## The user's given name.  Sometimes referred to as one's First Name
        given = Singular('givenName')

        ## The user's middle name
        middle = Singular('middleName')

        ## Any honorific prefixes someone might have.  Ex: Dr., Prof., Mr., etc
        prefix = Singular('honorificPrefix')

        ## Honorific suffixes.  Ex: III, Jr., Sr., etc.
        suffix = Singular('honorificSuffix')

    ## The username/login name represented in the system
    username = Singular('userName')

    ## User's proper name
    name = Name('name')

    ## formatted name ready for display.  This should be the primary way that a
    ## user is displayed
    display = Singular('displayName')

    ## User's nickname.  This doesn't have to be the same as username
    ## Ex: name = james -> display = jim

    ## Fully qualified URL pointing to user's profile
    profile = Singular('profileUrl')

    ## User's proper title.  Ex: Professor, Vice President
    title = Singular('title')

    ## identifies what sort of user this is.  Ex: Contractor, Employee, etc.
    user_type = Singular('userType')

    ## concatination of ISO 639-1, an underscore, and ISO 3166-1.  Ex: en_US
    language = Singular('preferredLanguage')

    ## concatination of ISO 639-1, an underscore, and ISO 3166-1.  Ex: en_US
    locale = Singular('locale')

    ## Timezone according to tz/IANA database.  Ex: America/Los_Angeles
    timezone = Singular('timezone')

    ## Boolean flag denoting user's admin status.  True means user is admin.
    admin = Singular('status')

    ## Password field. This really only ought to be set during a POST operation
    password = Singular('password')

    # Multi-value attributes.  These are pluralized to make it more obvious
    # that these are multi-value attribues

    ## Emails the user has registered with them
    emails = MultiValue('emails')

    ## phone numbers!
    phones = MultiValue('phoneNumbers')

    ## usernames for instant messaging services
    messengers = MultiValue('ims')

    ## urls for photos of the user.  Should point directly to an image
    photos = MultiValue('photos')

    ## Groups that the user is in
    groups = MultiValue('groups')

    ## Roles that the user has
    roles = MultiValue('roles')

    ## Entitlements that the user has
    entitlements = MultiValue('entitlements')

    ## Certificates belonging to the user
    certs = MultiValue('x509Certificates')

    ## physical addresses belonging to the user
    class Address(Complex):
        """
        Contains address attributes
        """

        ## The fully formatted address
        formatted = Singular('formatted')

        ## Street, house number, apartment number, po box, etc.
        street = Singular('streetAddress')

        ## City or locality that the location is in
        city = Singular('locality')

        ## state or region that the location is in
        state = Singular('region')

        ## Zip or postal code
        zip = Singular('postalCode')

        ## Country that the address is in in ISO 3166-1 format
        country = Singular('country')

    addresses = MultiValue('addresses')


class Enterprise(Extension):
    """
    Defines enterprise user extensions
    schema: urn:scim:schemas:extension:enterprise:1.0
    """

    class Manager(Complex):
        """
        User's Manager's primary key and name
        """

        class Meta:
            name = 'manager'

        ## Primary Key for manager
        id = Singular('managerId')

        ## Manager's name, for convenience purposes
        name = Singular('displayName')

    ## User's Employee number
    employee_id = Singular('employeeNumber')

    ## User's Cost Center (?)
    cost_center = Singular('costCenter')

    ## Organization
    organization = Singular('organization')

    ## Division of organizations
    division = Singular('division')

    ## Department of division
    department = Singular('department')

    ## User's manager
    # TODO: allow stuff like so:
    # x.enterprise.manager = Manager(id=32423, name="dsfsdf")
    manager = Manager('manager')
