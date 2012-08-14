# -*- coding: utf-8 -*-
""" \file "scim/client/user.py"
\brief "Provides ways of interacting with a user endpoint"

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
import requests
from ..schema.user import User


endpoint_format = '{}/Users/{}'


def get(endpoint, identifier):
    response = requests.get(endpoint_format.format(endpoint, identifier))
    response.raise_for_status()
    return User.deserialize(response.text)


def post(endpoint, data):
    data = User.serialize(data)
    response = requests.post(endpoint_format.format(endpoint, ''))
    response.raise_for_status()
    return User.deserialize(response.text)


def put(endpoint, identifier, data):
    data = User.serialize(data)
    response = requests.put(
        endpoint_format.format(endpoint, identifier),
        data=data
    )
    response.raise_for_status()
    return User.deserialize(response.text)


def delete(endpoint, identifier):
    response = requests.delete(endpoint_format.format(endpoint, identifier))
    response.raise_for_status
    return User.deserialize(response.text)
