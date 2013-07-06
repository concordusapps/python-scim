# -*- coding: utf-8 -*-
from dateutil.parser import parse as parse_datetime


class Base:

    def serialize(self, value):
        return str(value)

    def deserialize(self, text):
        if text is not None:
            return text


class String(Base):
    """A sequence of characters (v1.1 § 3.1.1).
    """


class Boolean(Base):
    """The literal "true" or "false" (v1.1 § 3.1.2).
    """

    def serialize(self, value):
        return 'true' if value else 'false'

    def deserialize(self, text):
        if text is not None:
            return text == 'true'


class Decimal(Base):
    """A Decimal number with no fractional digits (v1.1 § 3.1.3).
    """

    def deserialize(self, text):
        if text is not None:
            return float(text)


class Integer(Base):
    """A Decimal number with no fractional digits (v1.1 § 3.1.4).
    """

    def deserialize(self, text):
        if text is not None:
            return int(text)


class DateTime(Base):
    """
    An ISO 8601 formatted (eg. 2008-01-23T04:56:22Z)
    date-time (v1.1 § 3.1.5).
    """

    def serialize(self, value):
        return value.isoformat()

    def deserialize(self, text):
        if text is not None:
            return parse_datetime(text, fuzzy=False)
