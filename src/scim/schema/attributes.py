# -*- coding: utf-8 -*-
""" \file scim/schema/attributes.py
\brief Defines the different types of attributes.

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
import abc
import inspect


class Attribute(object):
    """TODO"""
    @classmethod
    @abc.abstractmethod
    def serialize(cls, obj):
        """TODO"""
        pass

    @classmethod
    @abc.abstractmethod
    def deserialize(cls, data):
        """TODO"""
        pass

    @property
    @abc.abstractmethod
    def _name(self):
        """TODO"""
        pass


class Singular(Attribute):
    """TODO"""
    @classmethod
    def serialize(cls, obj):
        """TODO"""
        return obj

    @classmethod
    def deserialize(cls, data):
        """TODO"""
        return data

    def __init__(self, name):
        """TODO"""
        ## Name of the attribute in the schema.
        self.name = name

    @property
    def _name(self):
        """TODO"""
        return self.name


class Complex(Attribute):
    """TODO"""
    class Meta:
        """TODO"""
        pass

    @classmethod
    def serialize(cls, obj):
        """TODO"""
        values = {}
        # Iterate over -every- class member of this class
        for name, value in inspect.getmembers(cls):
            # Ensure that the class member inherits from Attribute
            if not isinstance(value, Attribute):
                continue

            # Was this member provided in the instance dictionary ?
            if name in obj.__dict__:
                # Yes; serialize it and update it in the resultant dictionary
                values[value._name] = value.serialize(obj.__dict__[name])

        # Return serialized values
        return values

    @classmethod
    def deserialize(cls, data):
        """TODO"""
        pass

    def __init__(self, **kwargs):
        """TODO"""
        ## Metadata information about the attribute.
        self._meta = self.__class__.Meta()

        # Parse arguments
        for key, value in kwargs.items():
            segments = key.split('__')
            if segments[0] == 'meta':
                # Is a metadata argument; set in _meta
                setattr(self._meta, segments[1], value)
            else:
                # Is a normal argument; set in self
                self.__dict__[key] = value

    @property
    def _name(self):
        """TODO"""
        return self._meta.name


class MultiValue(Complex):
    """TODO"""
    ## A label indicating the attribute's function; e.g., "work" or "home".
    type = Singular("type")

    ## A Boolean value indicating the 'primary' or preferred attribute value
    ## for this attribute.
    primary = Singular("type")

    ## A human readable name, primarily used for display purposes.
    display = Singular("display")

    ## The operation to perform on the multi-valued attribute during
    ## a PATCH request.
    operation = Singular("type")

    @classmethod
    def serialize(cls, obj):
        """TODO"""
        # Serialize list as complex items
        return [super(MultiValue, cls).serialize(item) for item in obj]

    @classmethod
    def deserialize(cls, data):
        """TODO"""
        pass
