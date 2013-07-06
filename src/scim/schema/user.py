# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class Username(attributes.Base):
    """The components of the User's real name.
    """

    #! The full name, including all middle names, titles, and suffixes as
    #! appropriate, formatted for display (e.g. Ms. Barbara Jane Jensen, III.).
    formatted = attributes.Singular(types.String)

    #! The family name of the User, or "Last Name" in
    #! most Western languages (e.g. Jensen given the full name Ms.
    #! Barbara Jane Jensen, III.).
    family_name = attributes.Singular(types.String)

    #! The given name of the User, or "First Name" in most Western
    #! languages (e.g. Barbara given the full name
    #! Ms. Barbara Jane Jensen, III.).
    given_name = attributes.Singular(types.String)

    #! The middle name(s) of the User (e.g. Jane given the full
    #! name Ms. Barbara Jane Jensen, III.).
    middle_name = attributes.Singular(types.String)

    #! The honorific prefix(es) of the User, or "Title" in most
    #! Western languages (e.g. Ms. given the full name
    #! Ms. Barbara Jane Jensen, III.).
    honorific_prefix = attributes.Singular(types.String)

    #! The honorific suffix(es) of the User, or "Suffix" in most
    #! Western languages (e.g. III. given the full name
    #! Ms. Barbara Jane Jensen, III.).
    honorific_suffix = attributes.Singular(types.String)


class User(Base):
    """SCIM provides a schema for representing Users (v1.1 § 6).
    """

    #! Unique identifier for the User, typically used by the user to directly
    #! authenticate to the service provider.
    username = attributes.Singular(types.String, 'userName')

    #! The components of the User's real name.
    name = attributes.Complex(Username)
