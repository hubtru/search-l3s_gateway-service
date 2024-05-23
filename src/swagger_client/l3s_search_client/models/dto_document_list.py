# coding: utf-8

"""
    L3S Search Service for SEARCH

    Welcome to the Swagger UI documentation site test!  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DtoDocumentList(object):
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
        'secret': 'str',
        'documents': 'list[DtoDocument]'
    }

    attribute_map = {
        'secret': 'secret',
        'documents': 'documents'
    }

    def __init__(self, secret=None, documents=None):  # noqa: E501
        """DtoDocumentList - a model defined in Swagger"""  # noqa: E501
        self._secret = None
        self._documents = None
        self.discriminator = None
        if secret is not None:
            self.secret = secret
        if documents is not None:
            self.documents = documents

    @property
    def secret(self):
        """Gets the secret of this DtoDocumentList.  # noqa: E501


        :return: The secret of this DtoDocumentList.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this DtoDocumentList.


        :param secret: The secret of this DtoDocumentList.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def documents(self):
        """Gets the documents of this DtoDocumentList.  # noqa: E501


        :return: The documents of this DtoDocumentList.  # noqa: E501
        :rtype: list[DtoDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this DtoDocumentList.


        :param documents: The documents of this DtoDocumentList.  # noqa: E501
        :type: list[DtoDocument]
        """

        self._documents = documents

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
        if issubclass(DtoDocumentList, dict):
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
        if not isinstance(other, DtoDocumentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
