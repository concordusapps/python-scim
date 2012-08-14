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
    """BANANA"""
    @classmethod
    @abc.abstractmethod
    def serialize(cls, obj):
        """BANANA"""
        pass

    @classmethod
    @abc.abstractmethod
    def deserialize(cls, data):
        """BANANA"""
        pass

    @property
    @abc.abstractmethod
    def _name(self):
        """BANANA"""
        pass


class Singular(Attribute):
    """BANANA"""
    @classmethod
    def serialize(cls, obj):
        """BANANA"""
        return obj

    @classmethod
    def deserialize(cls, data):
        """BANANA"""
        return data

    def __init__(self, name):
        """BANANA"""
        ## Name of the attribute in the schema.
        self.name = name

    @property
    def _name(self):
        """BANANA"""
        return self.name


class Complex(Attribute):
    """BANANA"""
    class Meta:
        """BANANA"""
        pass

    @staticmethod
    def _serialize(members, obj):
        """BANANA"""
        values = {}
        # Iterate over -every- class member of this class
        for name, value in members:
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
    def serialize(cls, obj):
        """BANANA"""
        return cls._serialize(inspect.getmembers(cls), obj)

    @classmethod
    def deserialize(cls, data):
        """BANANA"""
        pass

    def __init__(self, **kwargs):
        """BANANA"""
        # Parse arguments
        self.__dict__.update(**kwargs)

    @property
    def _name(self):
        """BANANA"""
        return self.__class__.Meta.name


class MultiValue(Complex):
    """BANANA"""
    ## A label indicating the attribute's function; e.g., "work" or "home".
    type = Singular("type")

    ## A Boolean value indicating the 'primary' or preferred attribute value
    ## for this attribute.
    primary = Singular("primary")

    ## A human readable name, primarily used for display purposes.
    display = Singular("display")

    ## The operation to perform on the multi-valued attribute during
    ## a PATCH request.
    operation = Singular("type")

    ## The value of the specific attribute
    value = Singular("value")

    def __init__(self, value=None, **kwargs):
        """BANANA"""
        # convenience to allow first positional argument to be the value
        kwargs["value"] = value
        super(MultiValue, self).__init__(**kwargs)

    @classmethod
    def serialize(cls, obj):
        """BANANA"""
        # Serialize list as complex items
        values = []
        for item in obj:
            if item.value is None:
                # FIXME: This will break if there is more than one layer of
                #        inheritance.
                item.value = Complex._serialize(cls.__dict__.items(), item)

            # Serialize the remaining portion as a complex object
            values.append(Complex._serialize(
                inspect.getmembers(MultiValue),
                item
            ))

        # Return the serialized object
        return values

    @classmethod
    def deserialize(cls, data):
        """BANANA"""
        pass
