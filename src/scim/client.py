import requests



class Request(object):
    """Defines a basic request object
    """

    ##


    def __init__(self, **kwargs):
        """set random default arguments
        \var verb
            The type of method, ex: GET, POST, PUT, etc.

        \var url
            The fully qualified url of the endpoint being used
            ex: for Users, http://example.com/Users

        \var data
            The schema object to send to the server
        """
        for key, value in kwargs:
            if not key in ['verb', 'url', 'data']:
                raise ValueError('Invalid argument: {}'.format(key))
            setattr(self, key, value)

    def ready(self):
        """Returns true if object is ready to be sent, raises otherwise.
        TODO: Its weird that it raises on failure, consider other ways of
        preparation
        """
        for item in ['verb', 'url', 'data']:
            if not item in self.__dict__:
                raise AssertionError('Missng required data: {}'.format(item))
        verb = self.verb.lower()
        if not verb in ['get', 'post', 'put', 'delete', 'patch']:
            raise AssertionError('Unsupported verb: {}'.format(verb))
        return True

    def send(self):
        """Send the request
        """
        # Make sure we're ready
        self.ready()
        data = self.data.serialize()
        response = getattr(requests, self.verb)(self.url, data=data)
        self.response = response
