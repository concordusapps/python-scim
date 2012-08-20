# -*- coding: utf-8 -*-
""" \file "scim/enterprise.py"
\brief "Provides schemas and methods needed to interact with a Groups endpoint"

\author Adam Voliva (avoliva) adamvoliva@gmail.com

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

import requests
from . import user
from . import attributes
from .core import Core


class Enterprise(object):
    """Defines the Enterprise User
    """

    class Enterprise(attributes.Complex):

        class Meta:
            name = 'urn:scim:schemas:extension:enterprise:1.0'

        ## Numeric or alphanumeric identifier assigned to a person
        employee_no = attributes.Singular('employeeNumber')

        ## Identifies the name of a cost center.
        cost_center = attributes.Singular('costCenter')

        ## Identifies the name of an organization.
        organization = attributes.Singular('organization')

        ## Identifies the name of a division
        division = attributes.Singular('division')

        ## Identifies the name of a department.
        department = attributes.Singular('department')

        class Manager(attributes.Complex):
            """The user's manager
            """

            class Meta:
                name = 'manager'

            ## The id of the SCIM resource representing the manager
            manager_id = attributes.Singular('managerId')

            ## The displayName of the User's manager
            name = attributes.Singular('displayName')

        manager = Manager()

    enterprise = Enterprise()


class EnterpriseUser(user.User, Enterprise):
    """Defines the Enterprise User
    """
    pass
