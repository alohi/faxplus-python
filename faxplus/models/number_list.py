# coding: utf-8

"""
    FAX.PLUS REST API

    OpenAPI spec version: 1.2.0
    Contact: info@fax.plus
"""

import pprint
import re  # noqa: F401

import six
from faxplus.models import *


class NumberList(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'numbers': 'list[Number]'
    }

    attribute_map = {
        'numbers': 'numbers'
    }

    def __init__(self, numbers=None):  # noqa: E501
        """NumberList - a model defined in Swagger

        :param list[Number] numbers: (required)
        """  # noqa: E501
        self._numbers = None
        self.discriminator = None
        self.numbers = numbers

    @property
    def numbers(self):
        """Gets the numbers of this NumberList.  # noqa: E501


        :return: The numbers of this NumberList.  # noqa: E501
        :rtype: list[Number]
        """
        return self._numbers

    @numbers.setter
    def numbers(self, numbers):
        """Sets the numbers of this NumberList.


        :param numbers: The numbers of this NumberList.  # noqa: E501
        :type: list[Number]
        """
        if numbers is None:
            raise ValueError("Invalid value for `numbers`, must not be `None`")  # noqa: E501

        self._numbers = numbers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NumberList, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NumberList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
