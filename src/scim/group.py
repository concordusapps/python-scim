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
from .core import Core
from .attributes import Singular, MultiValue


class Group(Core):
    """Provides schemas for interacting with a group
    """

    ## A human readable name for the group
    name = Singular('displayName')

    class Members(MultiValue):
        class Meta:
            name = 'members'

    ## A list of group members
    # TODO: types 'User' and 'Group' are canonical types and therefore
    # the type attribute of a member is read-only.  the idea being to allow
    # nested groups
    members = Members()
