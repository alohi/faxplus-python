# coding: utf-8

"""
    FAX.PLUS REST API

    This is the fax.plus API v1 developed for third party developers and organizations. In order to have a better coding experience with this API, let's quickly go through some points:<br /><br /> - This API assumes **/accounts** as an entry point with the base url of **https://restapi.fax.plus/v1**. <br /><br /> - This API treats all date and times sent to it in requests as **UTC**. Also, all dates and times returned in responses are in **UTC**<br /><br /> - Once you have an access_token, you can easily send a request to the resource server with the base url of **https://restapi.fax.plus/v1** to access your permitted resources. As an example to get the user's profile info you would send a request to **https://restapi.fax.plus/v1/accounts/self** when **Authorization** header is set to \"Bearer YOUR_ACCESS_TOKEN\" and custom header of **x-fax-clientid** is set to YOUR_CLIENT_ID  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class PayloadOutboxOptionsRetry(object):
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
        'delay': 'int',
        'count': 'int'
    }

    attribute_map = {
        'delay': 'delay',
        'count': 'count'
    }

    def __init__(self, delay=None, count=None):  # noqa: E501
        """PayloadOutboxOptionsRetry - a model defined in Swagger"""  # noqa: E501

        self._delay = None
        self._count = None
        self.discriminator = None

        if delay is not None:
            self.delay = delay
        if count is not None:
            self.count = count

    @property
    def delay(self):
        """Gets the delay of this PayloadOutboxOptionsRetry.  # noqa: E501


        :return: The delay of this PayloadOutboxOptionsRetry.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this PayloadOutboxOptionsRetry.


        :param delay: The delay of this PayloadOutboxOptionsRetry.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def count(self):
        """Gets the count of this PayloadOutboxOptionsRetry.  # noqa: E501


        :return: The count of this PayloadOutboxOptionsRetry.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PayloadOutboxOptionsRetry.


        :param count: The count of this PayloadOutboxOptionsRetry.  # noqa: E501
        :type: int
        """

        self._count = count

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayloadOutboxOptionsRetry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
