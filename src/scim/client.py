import requests


class Request(object):
    """Defines a basic request object
    """

    def __init__(self, **kwargs):
        """set random default arguments
        \var verb
            The type of method, ex: GET, POST, PUT, etc.

        \var url
            The fully qualified url of the endpoint being used
            ex: for Users, http://example.com/Users

        \var data
            The schema object to send to the server

        \var format
            The format to send data to the server.  Ex: xml, json
            Valid parameters: json
            More formats will be added in the future
        """
        for key, value in kwargs.items():
            if not key in ['verb', 'url', 'data', 'format']:
                raise ValueError('Invalid argument: {}'.format(key))
            setattr(self, key, value)

    def ready(self):
        """Returns true if object is ready to be sent, raises otherwise.
        TODO: Its weird that it raises on failure, consider other ways of
        preparation
        """
        for item in ['verb', 'url', 'data', 'format']:
            if not item in self.__dict__:
                raise AssertionError('Missng required data: {}'.format(item))
        verb = self.verb.lower()
        if not verb in ['get', 'post', 'put', 'delete', 'patch']:
            raise AssertionError('Unsupported verb: {}'.format(verb))
        # verify format:
        if not self.format.lower() in ['json']:
            raise AssertionError('Unsupported encoding format: {}'.format(self.format))
        return True

    @staticmethod
    def serialize(cls, data):
        # TODO: serialize data using an encoder based on self.format
        pass

    @staticmethod
    def deserialize(cls, data):
        # TODO: deserialize data using an decoder based on self.format
        pass

    def send(self):
        """Send the request
        """
        # Make sure we're ready
        self.ready()
        data = self.serialize(self.data)
        response = getattr(requests, self.verb)(self.url, data=data)

        # Raise if the request went south
        # TODO: scim response codes are not all bad even if they are not in the
        # 200 range, detect if we should actually raise based on
        # response.status_code
        response.raise_for_status()

        # todo, deserialize based on response type
        # Create response object
        self.response = type(self.data)
        self.response.deserialize(response.text)
