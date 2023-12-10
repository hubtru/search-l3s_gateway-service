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

class ExternalContentUserExternalContentUserItemRead(object):
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
        'external_content_organization': 'str',
        'user': 'str'
    }

    attribute_map = {
        'external_content_organization': 'externalContentOrganization',
        'user': 'user'
    }

    def __init__(self, external_content_organization=None, user=None):  # noqa: E501
        """ExternalContentUserExternalContentUserItemRead - a model defined in Swagger"""  # noqa: E501
        self._external_content_organization = None
        self._user = None
        self.discriminator = None
        if external_content_organization is not None:
            self.external_content_organization = external_content_organization
        if user is not None:
            self.user = user

    @property
    def external_content_organization(self):
        """Gets the external_content_organization of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501


        :return: The external_content_organization of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._external_content_organization

    @external_content_organization.setter
    def external_content_organization(self, external_content_organization):
        """Sets the external_content_organization of this ExternalContentUserExternalContentUserItemRead.


        :param external_content_organization: The external_content_organization of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501
        :type: str
        """

        self._external_content_organization = external_content_organization

    @property
    def user(self):
        """Gets the user of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501


        :return: The user of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this ExternalContentUserExternalContentUserItemRead.


        :param user: The user of this ExternalContentUserExternalContentUserItemRead.  # noqa: E501
        :type: str
        """

        self._user = user

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
        if issubclass(ExternalContentUserExternalContentUserItemRead, dict):
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
        if not isinstance(other, ExternalContentUserExternalContentUserItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
