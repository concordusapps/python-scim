# -*- coding: utf-8 -*-
""" \file "scim/schema/attributes.py"
\brief "defining the different types of attributes

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


class Attribute(object):
    name = None

    def __init__(self, name):
        self.name = name


class Singular(Attribute):
    """
    A singular name->value attribute
    """
    name = None
    value = None

    def __init__(self, name, value=None):
        super(Singular, self).__init__(name)
        self.value = value


class Complex(Attribute):
    """
    A complex attribute comprising of many singular attributes
    """
    members = []

    pass


class MultiValue(Attribute):
    """
    A multivalue attribute comprising of many same-typed attributes
    """

    ## Contains the index of the primary attribute, if one exists
    primary = None
    members = []

    pass


class MultiValueValue():
    """
    A value in a multi-value attribute
    """

    ## The type of attribute.
    ## Ex for phones: work, home, mobile, etc.
    type = None

    ## The value of the attribute
    ## Ex for phones: the phone number itself
    value = None

    ## A read-only human readable version of the value
    display = None

    ## The operation to be performed during a PATCH request.
    ## The only value supported here is 'delete'
    operation = None
