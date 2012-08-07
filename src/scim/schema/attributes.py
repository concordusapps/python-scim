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
import collections
import types
from abc import abstractmethod
import inspect


class Attribute(object):
    _meta = None

    class Meta:
        """
        contains metadata about the attribute
        """
        pass

    def __init__(self, **kwargs):
        # set metadata
        self._meta = self.__class__.Meta()

        # parse extra metadata arguments
        for key, value in kwargs:
            segments = key.split('__')
            if segments[0] == 'meta':
                setattr(self._meta, segments[1], value)
            else:
                self.__dict__[key] = value

        # make sure we actually got a name?
        if self._meta['name'] is not None:
            raise ValueError('Attribute requires name')

    @abstractmethod
    def devitalize(self):
        """
        This returns a list/dict representation of the attribute
        """
        pass


#    @abstractmethod
#    def vitalize(self):
#        """
#        Takes a list/dict representation of an attribute tree and constructs
#        an actual attribute tree out of it
#        """


class Singular(Attribute):
    """
    A singular name->value attribute
    """

    def devitalize(self, mess):
        return mess


class Complex(Attribute, collections.MutableMapping):
    """
    A complex attribute comprising of many singular attributes
    """

    def devitalize(self, mess):
        items = dict()
        for name, item in inspect.getmembers(self.__class__):
            if name in self.__dict__:
                items[item.name] = item.devitalize(self.__dict__[name])

        items = dict()
        for key, item in inspect.getmembers(self.__class__):
            exists = None
            try:
                exists = key in mess.__dict__
            except:
                exists = key in mess
            if exists:
                items[item.name] = item.devitalize()
        return items



#class MultiValue(Attribute, collections.MutableSequence):
#    """
#    A multivalue attribute comprising of many same-typed attributes
#    """
#
#    ## Contains the index of the primary attribute, if one exists
#    primary = None
#    members = []
#
#    def _memberize(self, val):
#        """
#        checks if val is an instance of MultiValueValue and wrapps it in an
#        instance of one if it isn't
#        """
#        return val
##        if isinstance(val, MultiValueValue):
##            return val
##        else:
##            return MultiValueValue(val)
#
#    def primary_member(self, index, primary=None):
#        if primary:
#            self.primary = index
#        return self.primary
#
#    def __getitem__(self, index):
#        return self.members[index]
#
#    def __setitem__(self, index, value):
#        self.members[index] = self._memberize(value)
#        return self.members[index]
#
#    def __delitem__(self, index):
#        if self.primary == index:
#            self.primary = None
#        return self.members.__delitem__(index)
#
#    def insert(self, index, value):
#        return self.members.insert(index, self._memberize(value))
#
#    def __len__(self):
#        return self.members.__len__()
#
#    def __contains__(self, value):
#        for item in self.members:
#            if item.value == value:
#                return True
#        return False
#
#    def __iter__(self):
#        return self.members.__iter__()
#
#    def __reversed__(self):
#        return self.members.__reversed__()
#
#    def append(self, value):
#        return self.members.append(self._memberize(value))
#
#    def devitalize(self, mess):
#        """
#        formats construct into a sequence for encoding
#        """
#        if not isinstance(mess, ListType):
#            raise AttributeError('{} is not of type List'.format(mess))
#        # TODO: we can flatten the array here if no special attributes are present
#        return mess


class MultiValue(Attribute):

    def devitalize(self, mess):
        primary = None
        items = list()
        for item in mess:
            itemdict = dict()
            for x in ['type', 'operation', 'display']:
                getattr()
            if item.primary and not primary:
                primary =
        Attribute.devitalize(self)

class MultiValueValue(Attribute):
    class Meta:
        type = None
        primary = False
        value = None
        operation = None
        display = ''
    def getdynamic(self, key):
        if key in self.__dict__


#class MultiValueValue():
#    """
#    A value in a multi-value attribute
#    """
#
#    def __init__(self, value, **kwargs):
#        """
#        Initializes MultiValueValue with any kwargs sent
#        """
#        self.value = value
#        for key, val in kwargs:
#            if hasattr(MultiValueValue, key):
#                setattr(self, key, val)
#
#    def devitalize(self, primary=None):
#        """
#        Devitalizes the value into an array for preparation
#        """
#        shrivled = dict()
#        for prop in ['type', 'display', 'operation']:
#            shrivled[prop] = getattr(self, prop)
#        if primary:
#            shrivled['primary'] = primary
#        try:
#            shrivled['value'] = self.value.devitalize()
#        except AttributeError:
#            shrivled['value'] = self.value
#        return shrivled
#
#    ## The type of attribute.
#    ## Ex for phones: work, home, mobile, etc.
#    type = None
#
#    ## The value of the attribute
#    ## Ex for phones: the phone number itself
#    value = None
#
#    ## A read-only human readable version of the value
#    display = None
#
#    ## The operation to be performed during a PATCH request.
#    ## The only value supported here is 'delete'
#    operation = None
