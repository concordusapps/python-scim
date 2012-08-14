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
import collections
import inspect
import json


class Attribute(object):
    """TODO"""
    @abc.abstractmethod
    @classmethod
    def serialize(self, obj):
        """TODO"""
        pass

    @abc.abstractmethod
    @classmethod
    def deserialize(self, data, method='json'):
        """TODO"""
        pass


class Singular(Attribute):
    """TODO"""
    @classmethod
    def serialize(self, obj):
        """TODO"""
        return str(obj)

    @classmethod
    def deserialize(self, data):
        """TODO"""
        return data

    def __init__(self, name):
        """TODO"""
        ## Name of the attribute in the schema.
        self.name = name


class Complex(Attribute):
    """TODO"""
    class Meta:
        """TODO"""
        pass

    @classmethod
    def serialize(self, obj):
        """TODO"""
        return str(obj)

    @classmethod
    def deserialize(self, data):
        """TODO"""
        return data

    def __init__(self, **kwargs):
        """TODO"""
        ## Metadata information about the attribute.
        self._meta = self.__class__.Meta()

        # Parse arguments
        for key, value in kwargs:
            segments = key.split('__')
            if segments[0] == 'meta':
                # Is a metadata argument; set in _meta
                setattr(self._meta, segments[1], value)
            else:
                # Is a normal argument; set in self
                self.__dict__[key] = value



#class Singular(Attribute):
#    """
#    A singular name->value attribute
#    """
#
#    def devitalize(self, mess):
#        return mess
#
#
#class Complex(Attribute, collections.MutableMapping):
#    """
#    A complex attribute comprising of many singular attributes
#    """
#
#    def devitalize(self, mess):
#        ## a complex holds its attributes as members
#        items = dict()
#        for name, master in inspect.getmembers(self.__class__):
#            attr = self.__dict__.get(name)
#            if attr is None:
#                continue
#            try:
#                items[master._meta.name] = attr.devitalize()
#                continue
#            except AttributeError:
#                # its not an attribute object
#                pass
#
#            try:
#                # is it a list of items?
#                flattened = []
#                for item in attr:
#                    flattened.append(item.devitalize())
#                items[master._meta.name] = flattened
#            except TypeError:
#                # Its not a list of items
#                # This should technically never happen
#                raise
#            except AttributeError:
#                # it is a list of items, but those items are not attribute objects
#                items[master._meta.name] = attr
#        return items
#
#
#class MultiValue(Attribute):
#
#    ## MultiValues will never store data in themselves, so do not operate on
#    ## __class__.  For all intents and purposes, a MultiValue will be static
#    ## provided that the mess passed to devitalize is a list
#    def devitalize(self, mess):
#        primary = None
#        items = list()
#        for item in mess:
#            itemdict = dict()
#            for x in ['type', 'operation', 'display']:
#                if getattr(item, x):
#                    itemdict[x] = getattr(item, x)
#            if item.primary and not primary:
#                itemdict['primary'] = True
#                primary = True  # only a single one may be primary
#        Attribute.devitalize(self)
#
#
#class MultiValueValue(Attribute):
#    class Meta:
#        type = None
#        primary = False
#        value = None
#        operation = None
#        display = ''
