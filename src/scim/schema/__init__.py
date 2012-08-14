
from .attributes import Complex
import inspect


class Schema(Complex):
    """
    This defines the base class for all schemas
    """


class Extension(Schema):
    """
    This defines a schema extension base class
    TODO: implement such that schema extensions are added to the object as
    subkeys containing all the extended attributes
    """
    pass
