
from .attributes import Attribute
import inspect


class Schema(object):
    """
    This defines the base class for all schemas
    """

    def devitalize(self):
        """Exports a schema into an array so that it may be encoded"""
        # this will iterate over every SchemaProperty in the scheme and
        # create an associative array that way
        devitalized = dict()
        for name, master in inspect.getmembers(self.__class__):
            if name in self.__dict__:
                devitalized[master.name] = master.devitalize(self.__dict__[name])
        return devitalized


class Extension(Schema):
    """
    This defines a schema extension base class
    TODO: implement such that schema extensions are added to the object as
    subkeys containing all the extended attributes
    """
    pass
