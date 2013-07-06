# -*- coding: utf-8 -*-
from . import attributes, types


class Metadata(attributes.Base):
    """A complex attribute containing resource metadata.
    """

    #! The DateTime the Resource was added to the Service Provider.
    created = attributes.Singular(types.DateTime)

    #! The most recent DateTime the details of this Resource were updated at
    #! the Service Provider. If this Resource has never been modified since
    #! its initial creation, the value MUST be the same as the value of
    #! created.
    last_modified = attributes.Singular(types.DateTime)

    #! The URI of the resource being returned.
    #!
    #! This value MUST be the same as the Location HTTP response header.
    location = attributes.Singular(types.String)

    #! The version of the Resource being returned.
    #!
    #! This value must be the same as the ETag HTTP response header.
    version = attributes.Singular(types.String)

    #! The names of the attributes to remove during a PATCH operation.
    # attributes = attributes.List(types.String)


class Base(attributes.Base):
    """Defines the base SCIM schema (v1.1 § 5.5).

    Contains common attributes that all data models in the SCIM schema have.
    """

    class Meta:
        schema = 'urn:scim:schemas:core:1.0'

    #! Unique identifier for the SCIM Resource as defined by the
    #! Service Provider.
    #!
    #! Each representation of the Resource MUST include a non-empty id value.
    #! This identifier MUST be unique across the Service Provider's entire
    #! set of Resources. It MUST be a stable, non-reassignable identifier
    #! that does not change when the same Resource is returned in
    #! subsequent requests.
    #!
    #! The value of the id attribute is always issued by the Service Provider
    #! and MUST never be specified by the Service Consumer.
    id = attributes.Singular(types.Integer, required=True)

    #! An identifier for the Resource as defined by the Service Consumer.
    #!
    #! The externalId may simplify identification of the Resource between
    #! Service Consumer and Service provider by allowing the Consumer to
    #! refer to the Resource with its own identifier, obviating the need to
    #! store a local mapping between the local identifier of the Resource and
    #! the identifier used by the Service Provider.
    external_id = attributes.Singular(types.Integer)

    #! A complex attribute containing resource metadata.
    meta = attributes.Complex(Metadata, last=True)
