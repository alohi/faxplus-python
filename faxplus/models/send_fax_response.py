# coding: utf-8

"""
    FAX.PLUS REST API

    Visit https://apidoc.fax.plus for more information.

    © Alohi SA (Geneva, Switzerland)

    https://www.alohi.com
    Contact: info@fax.plus
"""

import pprint
import re  # noqa: F401

import six
from faxplus.models import *


class SendFaxResponse(object):

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'ids': 'dict(str, object)'
    }

    attribute_map = {
        'ids': 'ids'
    }

    def __init__(self, ids=None):  # noqa: E501
        """SendFaxResponse - a model defined in Swagger

        :param dict(str, object) ids: Destination-to-ID mapping
        """  # noqa: E501
        self._ids = None
        self.discriminator = None
        if ids is not None:
            self.ids = ids

    @property
    def ids(self):
        """Gets the ids of this SendFaxResponse.  # noqa: E501

        Destination-to-ID mapping  # noqa: E501

        :return: The ids of this SendFaxResponse.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this SendFaxResponse.

        Destination-to-ID mapping  # noqa: E501

        :param ids: The ids of this SendFaxResponse.  # noqa: E501
        :type: dict(str, object)
        """

        self._ids = ids

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
        if issubclass(SendFaxResponse, dict):
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
        if not isinstance(other, SendFaxResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

