# -*- coding: utf-8 -*-
""" \file "scim/core.py"
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

from . import Schema
from . import attributes
from .attributes import Singular, Complex


class Core(Schema):
    """
    Defines the core scim schema
    """
    class Metadata(Complex):
        """
        The complex attribute for metadata
        """

        class Meta:
            name = 'meta'

        ## The time that this entity was created
        created = Singular('created')

        ## The last time this entity was modified
        modified = Singular('lastModified')

        ## Simply the url that is being accessed during this request
        url = Singular('location')

        ## Version of the attribute being returned.  This value should also be
        ## in the HTTP header during the response
        version = Singular('version')

        ## Attributes that need to be removed during a PATCH request
        delete = Singular('attributes')

    ## The external primary key for the resource being accessed
    id = Singular('id')

    ## The internal primary key for the resource being accessed.  if set,
    ## forces the foreign endpoint to provide mapping between the external id
    ## and their internal id
    external_id = Singular('externalId')

    ## Metadata present during a request
    meta = Metadata('meta')

    ## The schemas attribute is a special case scenario which looks like it
    ## should be a multi-value attribute, but is actually simply a list of
    ## strings containing the schemas implemented in the request or response
    class SchemaAttribute(attributes.Attribute):
        """
        Special case attribute for the core schema
        """

        def devitalize(self, mess):
            return mess

    schemas = SchemaAttribute('schemas')

    def __init__(self):
        """
        Add entries to schema listing
        """
        # add core schema specification to our schema listing
        self.schemas = ['urn:scim:schemas:core:1.0']
