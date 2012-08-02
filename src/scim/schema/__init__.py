

class Schema():
    """
    This defines the base class for all schemas
    """

    def encode(self):
        """Exports a schema into an array"""
        pass


class Extension(Schema):
    """
    This defines a schema extension base class
    TODO: implement such that schema extensions are added to the object as
    subkeys containing all the extended attributes
    """
    pass
