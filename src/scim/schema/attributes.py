# -*- coding: utf-8 -*-
import collections
import json
import re


def camelize(name):
    name = name.strip()
    pattern = r'[-_\s]+(.)?'
    name = re.sub(pattern, lambda m: m.groups()[0].upper() if m else '', name)
    return name


class Declarative(type):

    @classmethod
    def __prepare__(cls, name, bases):
        return collections.OrderedDict()

    def __new__(cls, name, bases, attrs):
        # Collect declared attributes.
        attrs['_attributes'] = collections.OrderedDict()

        # Collect attributes from base classes.
        for base in bases:
            values = getattr(base, '_attributes', None)
            if values:
                attrs['_attributes'].update(values)

        # Collect attributes from current class.
        for key, attr in attrs.items():
            if isinstance(type(attr), cls):
                # If name reference is null; default to camel-cased name.
                if attr.name is None:
                    attr.name = camelize(key)

                # Store attribute in dictionary.
                attrs['_attributes'][attr.name] = attr

        # Collect schemas names from base classes.
        attrs['_schemas'] = schemas = []
        for base in bases:
            values = getattr(base, '_schemas', None)
            if values:
                schemas.extend(values)

        # Append the current schema.
        options = attrs.get('Meta')
        schema = getattr(options, 'schema', None)
        if schema:
            schemas.append(schema)

        # Continue initialization.
        return super().__new__(cls, name, bases, attrs)


class Base(metaclass=Declarative):
    """
    Represents an attribute wrapper; intended to tie a name, constraints,
    and behavior to a type.
    """

    def __init__(self, last=False):
        #! Instance state of the attribute.
        self._state = {}

        #! Whether to ensure the element is inserted last of not.
        self._last = last

    def serialize(self):
        # Serialize the data in the instance state to the representation
        # specified (only JSON supported as of now).
        data = collections.OrderedDict()

        # Insert the schemas list.
        data['schemas'] = self._schemas

        # Iterate through the non-last declared attributes.
        for name, attr in self._attributes.items():
            if attr._last:
                # Don't add this yet.
                continue

            value = attr.serialize(self)
            if value:
                data[name] = value

        # Iterate through the last declared attributes.
        for name, attr in self._attributes.items():
            if attr._last:
                value = attr.serialize(self)
                if value:
                    data[name] = value

        # Encode the data dictionary as JSON.
        return json.dumps(data)

    @classmethod
    def deserialize(cls, text, instance=None):
        if isinstance(text, str):
            # Decode the data dictionary from JSON.
            text = json.loads(text)

        # Instantiate an instance if one is not provided.
        if instance is None:
            instance = cls()

        # Iterate through the attributes to rebuild the instance state.
        for name, attr in instance._attributes.items():
            value = text.get(name)
            value = attr.deserialize(value)
            if value:
                instance._state[name] = value

        # Return the reconstructed instance.
        return instance


class Singular(Base):

    def __init__(self, type_, name=None, required=False, *args, **kwargs):
        #! The underyling type of the attribute.
        self.type = type_
        if isinstance(type_, type):
            # Instantiate the type reference with no parameters.
            self.type = type_()

        #! The name as the attribute is represented in the serialized form.
        #!
        #! If left as None; this will be set to the camelCased version of
        #! the property name.
        self.name = name

        #! Whether this attribute is required.
        self.required = required

        # Continue initialization.
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner=None):
        if instance is not None:
            # Being accessed as an instance; use the instance state.
            return instance._state.get(self.name)

        # Return ourself.
        return self

    def __set__(self, instance, value):
        if instance is not None:
            # Being accessed as an instance; use the instance state.
            instance._state[self.name] = value
            return

        # Continue along with normal behavior.
        super().__set__(instance, value)

    def __delete__(self, instance):
        if instance is not None:
            # Being accessed as an instance; use the instance state.
            if self.name in instance._state:
                del instance._state[self.name]
                return

        # Continue along with normal behavior.
        super().__delete__(instance)

    def serialize(self, obj):
        if self.name in obj._state:
            return self.type.serialize(obj._state[self.name])

    def deserialize(self, text):
        return self.type.deserialize(text)


class Complex(Base):

    def __init__(self, type_, name=None, *args, **kwargs):
        #! The underyling type of the attribute.
        self.type = type_

        #! The name as the attribute is represented in the serialized form.
        #!
        #! If left as None; this will be set to the camelCased version of
        #! the property name.
        self.name = name

        # Continue initialization.
        super().__init__(*args, **kwargs)

    def __get__(self, instance, owner=None):
        if instance is not None:
            if self.name not in instance._state:
                # Initialize the type.
                instance._state[self.name] = self.type()

            # Being accessed as an instance; use the instance state.
            return instance._state[self.name]

        # Return ourself.
        return self

    def __set__(self, instance, value):
        if instance is not None:
            # Being accessed as an instance; bail.
            raise AttributeError("can't set attribute")

        # Continue along with normal behavior.
        super().__set__(instance, value)

    def __delete__(self, instance):
        if instance is not None:
            # Being accessed as an instance; bail.
            raise AttributeError("can't delete attribute")

        # Continue along with normal behavior.
        super().__delete__(instance)

    def serialize(self, obj):
        # Grab the data object to serialize.
        if self.name in obj._state:
            obj = obj._state[self.name]

        else:
            # No data to serialize.
            return

        # Serialize the data in the instance state to the representation
        # specified (only JSON supported as of now).
        data = collections.OrderedDict()
        for name, attr in obj._attributes.items():
            value = attr.serialize(obj)
            if value:
                data[name] = value

        # Return the serialized data.
        return data

    def deserialize(self, text):
        if text is not None:
            return super().deserialize(text, instance=self.type())
