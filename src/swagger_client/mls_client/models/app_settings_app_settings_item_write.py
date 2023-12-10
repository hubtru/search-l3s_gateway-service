# coding: utf-8

"""
    MLS2 API

    Central API  # noqa: E501

    OpenAPI spec version: 0.7.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AppSettingsAppSettingsItemWrite(object):
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
        'update_today': 'bool'
    }

    attribute_map = {
        'update_today': 'updateToday'
    }

    def __init__(self, update_today=None):  # noqa: E501
        """AppSettingsAppSettingsItemWrite - a model defined in Swagger"""  # noqa: E501
        self._update_today = None
        self.discriminator = None
        if update_today is not None:
            self.update_today = update_today

    @property
    def update_today(self):
        """Gets the update_today of this AppSettingsAppSettingsItemWrite.  # noqa: E501


        :return: The update_today of this AppSettingsAppSettingsItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._update_today

    @update_today.setter
    def update_today(self, update_today):
        """Sets the update_today of this AppSettingsAppSettingsItemWrite.


        :param update_today: The update_today of this AppSettingsAppSettingsItemWrite.  # noqa: E501
        :type: bool
        """

        self._update_today = update_today

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
        if issubclass(AppSettingsAppSettingsItemWrite, dict):
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
        if not isinstance(other, AppSettingsAppSettingsItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
