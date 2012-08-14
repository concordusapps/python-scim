import requests
import abc
from .schema import user


class Request(object):
    """Defines a basic request object
    """

    ## Verbs supported by the request object
    supported_verbs = []

    ## Encoding formats supported by the request object
    # TODO: add more
    supported_encodings = ['json']

    def __init__(self, verb, url, data, encoding='json'):
        """set random default arguments
        \var verb
            The type of method, ex: GET, POST, PUT, etc.

        \var url
            The fully qualified url of the endpoint being used
            ex: for Users, http://example.com/Users

        \var data
            The schema object to send to the server

        \var encoding
            The format to send data to the server.  Ex: xml, json
            Valid parameters: json
            More formats will be added in the future
        """
        # verify verb
        assert(verb in self.supported_verbs)
        assert(encoding in self.supported_encodings)
        self.verb = verb
        self.url = url
        self.data = data
        self.encoding = encoding

    def prep_url(self):
        """overridable method to allow extra decoration of url
        """
        return self.url

    @staticmethod
    @abc.abstractmethod
    def serialize(data):
        # TODO: serialize data using an encoder based on self.format
        pass

    @staticmethod
    @abc.abstractmethod
    def deserialize(data):
        # TODO: deserialize data using an decoder based on self.format
        pass

    def send(self):
        """Send the request
        """
        data = self.serialize(self.data)

        # requests object has methods named get, post, etc.
        # fetch method and call it
        response = getattr(
            requests,
            self.verb)(self.prep_url(), data=data)

        # Raise if the request went south
        # TODO: scim response codes are not all bad even if they are not in the
        # 200 range, detect if we should actually raise based on
        # response.status_code
        response.raise_for_status()

        self.response = self.deserialize(response.text)


class User(Request):
    """Defines a request to a user interface
    """

    supported_verbs = ['get', 'post', 'put', 'patch', 'delete']

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

        if not self.verb == 'post':
            # In non-POST operations, the url must have the user id tacked on to
            # the end.
            # Ex: http://example.com/Users/2819c223-7f76-453a-919d-413861904646
            url = Request.prep_url(self)
            url_format = '{}{}' if url[-1:] == '/' else '{}/{}'

            # In user requests, the user ID is stored in data.id
            # TODO: how do ExternalIDs handle this?
            self.url = url_format.format(url, self.data.id)

    @staticmethod
    def deserialize(obj):
        return user.User.deserialize(obj)

    @staticmethod
    def serialize(obj):
        return user.User.serialize(obj)
