# -*- coding: utf-8 -*-
""" \file "scim/config.py"
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


class Config(Core):
    """Defines the schema mapping configuration.
    """

    ## An URL pointing to the Service Provider's help documentation.
    doc_url = attributes.Singular('documentationUrl')

    class Supported(attributes.Complex):
        #TODO#

        ## Boolean value specifying whether the operation is supported.
        supported = attributes.Singular('supported')

    class Patch(Supported):
        """A complex type that specifies PATCH configuration options.
        """

        class Meta:
            name = 'patch'

    patch = Patch()

    class Bulk(Supported):
        """A complex type that specifies BULK configuration options.
        """

        class Meta:
            name = 'bulk'

        ## An integer value specifying the maximum number of operations.
        max_operations = attributes.Singular('maxOperations')

        ## An integer value specifying the maximum payload size in bytes
        max_payload = attributes.Singular('maxPayloadSize')

    bulk = Bulk()

    class Filter(Supported):
        """A complex type that specifies FILTER options.
        """

        class Meta:
            name = 'filter'

        ## Integer specifying maximum Resources returned in a response.
        max_results = attributes.Singular('maxResults')

    filter = Filter()

    class ChangePassword(Supported):
        """A complex type that specifies Change Password configuration options.
        """

        class Meta:
            name = 'changePassword'

    change_pass = ChangePassword()

    class Sort(Supported):
        """A complex type that specifies Sort configuration options.
        """

        class Meta:
            name = 'sort'

    sort = Sort()

    class ETag(Supported):
        """A complex type that specifies Etag configuration options.
        """

        class Meta:
            name = 'etag'

    etag = ETag()

    class XMLDataFormat(Supported):
        """A complex type that specifies whether the XML data format is
        supported.
        """

        class Meta:
            name = 'xmlDataFormat'

    xml_format = XMLDataFormat()

    class AuthenticationScheme(attributes.MultiValue):
        """A complex type that specifies supported Authentication Scheme
         properties.
         """

        class Meta:
            name = 'authenticationSchemes'

        ## The common authentication scheme name; e.g., HTTP Basic
        name = attributes.Singular('name')

        ## A description of the Authentication Scheme.
        description = attributes.Singular('description')

        ## A URL pointing to the Authentication Scheme's specification.
        spec_url = attributes.Singular('specUrl')

        ## A URL pointing to the Authentication Scheme's usage documentation.
        doc_url = attributes.Singular('documentationUrl')

    auth = AuthenticationScheme()


def get(endpoint, identifier):
    """BANANA"""
    response = requests.get(endpoint_format.format(endpoint, identifier))
    response.raise_for_status()
    return Config.deserialize(response.text)


def post(endpoint, data):
    """BANANA"""
    data = Config.serialize(data)
    response = requests.post(endpoint_format.format(endpoint, ''))
    response.raise_for_status()
    return Config.deserialize(response.text)


def put(endpoint, identifier, data):
    """BANANA"""
    data = Config.serialize(data)
    response = requests.put(
        endpoint_format.format(endpoint, identifier),
        data=data
    )
    response.raise_for_status()
    return Config.deserialize(response.text)


def delete(endpoint, identifier):
    """BANANA"""
    response = requests.delete(endpoint_format.format(endpoint, identifier))
    response.raise_for_status()
    return Config.deserialize(response.text)


def patch(endpoint, identifier, data):
    """BANANA"""
    response = requests.patch(
        endpoint_format.format(endpoint, identifier),
        data=data,
    )
    response.raise_for_status()
    return Config.deserialize(response.text)
