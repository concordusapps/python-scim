# -*- coding: utf-8 -*-
""" \file "scim/schema.py"
\brief "Provides schemas and methods needed to interact with a Users endpoint"

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
from . import attributes
from .core import Core


endpoint_format = '{}/Schema/{}'


class Schema(Core):
    """Defines the schema mapping configuration.
    """

    class CommonAttributes(object):
        """Common attributes in the Schema
        """

        ## The attribute's or resource's name.
        name = attributes.Singular('name')

        ## The attribute's or resource's data type.
        type = attributes.Singular('type')

        ## The attribute's or resource's human readable description.
        description = attributes.Singular('description')

        ## A Boolean value that specifies if the attribute is mutable.
        read_only = attributes.Singular('readOnly')

        ## A Boolean value that specifies if the attribute is required.
        required = attributes.Singular('required')

        ## A Boolean that specifies if the String attribute is case sensitive.
        case_exact = attributes.Singular('caseExact')

        ## The attribute's or resource's associated schema.
        schema = attributes.Singular('schema')

    class Attributes(attributes.Complex, CommonAttributes):
        """A complex type that specifies the set of Resource attributes.
        """

        class Meta:
            name = 'attributes'

        ## Boolean value indicating the attribute's plurality.
        multi_valued = attributes.Singular('multiValued')

        ## String value specifying the child XML element name;
        ## e.g., the 'emails' attribute value is 'email'.
        ## REQUIRED when the multiValued attribute value is true
        ## otherwise this attribute MUST be omitted.
        multi_valued_child_name = attributes.Singular(
            'multiValuedAttributeChildName'
        )

        class SubAttributes(attributes.MultiValue):

            class Meta:
                name = 'subAttributes'

            ## A collection of canonical values. When applicable Service
            ## Providers MUST specify the canonical types specified in the core
            ## schema specification.
            canonical_values = attributes.Singular('canonicalValues')

        sub_attributes = SubAttributes()

    attributes = Attributes()
