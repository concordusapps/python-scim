# -*- coding: utf-8 -*-
from .core import Base
from . import attributes, types


class Tenant(Base):

    class Meta:
        schema = 'urn:scim:schemas:extension:tenant:1.0'

    #! The name of the tenant, suitable for display to end-users.
    display_name = attributes.Singular(types.String)

    #! Indicates the tenant's preferred written or spoken language.
    preferred_language = attributes.Singular(types.String)

    #! Used to indicate the tenant's default location for purposes of
    #! localizing items such as currency, date time format,
    #! numerical representations, etc.
    locale = attributes.Singular(types.String)

    #! The tenant's time zone in the "Olson" timezone database
    #! format; e.g.,'America/Los_Angeles'.
    timezone = attributes.Singular(types.String)

    #! A Boolean value indicating the tenant's administrative status.
    active = attributes.Singular(types.Boolean)
