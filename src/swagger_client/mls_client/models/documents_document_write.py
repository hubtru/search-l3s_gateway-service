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

class DocumentsDocumentWrite(object):
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
        'owner': 'str',
        'parent': 'str',
        'is_common': 'bool',
        'organization': 'str',
        'is_restricted': 'bool',
        'is_group': 'bool',
        'custom_filename': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'parent': 'parent',
        'is_common': 'isCommon',
        'organization': 'organization',
        'is_restricted': 'isRestricted',
        'is_group': 'isGroup',
        'custom_filename': 'customFilename'
    }

    def __init__(self, owner=None, parent=None, is_common=True, organization=None, is_restricted=None, is_group=None, custom_filename=None):  # noqa: E501
        """DocumentsDocumentWrite - a model defined in Swagger"""  # noqa: E501
        self._owner = None
        self._parent = None
        self._is_common = None
        self._organization = None
        self._is_restricted = None
        self._is_group = None
        self._custom_filename = None
        self.discriminator = None
        if owner is not None:
            self.owner = owner
        if parent is not None:
            self.parent = parent
        if is_common is not None:
            self.is_common = is_common
        if organization is not None:
            self.organization = organization
        if is_restricted is not None:
            self.is_restricted = is_restricted
        if is_group is not None:
            self.is_group = is_group
        if custom_filename is not None:
            self.custom_filename = custom_filename

    @property
    def owner(self):
        """Gets the owner of this DocumentsDocumentWrite.  # noqa: E501


        :return: The owner of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DocumentsDocumentWrite.


        :param owner: The owner of this DocumentsDocumentWrite.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def parent(self):
        """Gets the parent of this DocumentsDocumentWrite.  # noqa: E501


        :return: The parent of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DocumentsDocumentWrite.


        :param parent: The parent of this DocumentsDocumentWrite.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def is_common(self):
        """Gets the is_common of this DocumentsDocumentWrite.  # noqa: E501


        :return: The is_common of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """Sets the is_common of this DocumentsDocumentWrite.


        :param is_common: The is_common of this DocumentsDocumentWrite.  # noqa: E501
        :type: bool
        """

        self._is_common = is_common

    @property
    def organization(self):
        """Gets the organization of this DocumentsDocumentWrite.  # noqa: E501


        :return: The organization of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this DocumentsDocumentWrite.


        :param organization: The organization of this DocumentsDocumentWrite.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def is_restricted(self):
        """Gets the is_restricted of this DocumentsDocumentWrite.  # noqa: E501


        :return: The is_restricted of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        """Sets the is_restricted of this DocumentsDocumentWrite.


        :param is_restricted: The is_restricted of this DocumentsDocumentWrite.  # noqa: E501
        :type: bool
        """

        self._is_restricted = is_restricted

    @property
    def is_group(self):
        """Gets the is_group of this DocumentsDocumentWrite.  # noqa: E501


        :return: The is_group of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this DocumentsDocumentWrite.


        :param is_group: The is_group of this DocumentsDocumentWrite.  # noqa: E501
        :type: bool
        """

        self._is_group = is_group

    @property
    def custom_filename(self):
        """Gets the custom_filename of this DocumentsDocumentWrite.  # noqa: E501


        :return: The custom_filename of this DocumentsDocumentWrite.  # noqa: E501
        :rtype: str
        """
        return self._custom_filename

    @custom_filename.setter
    def custom_filename(self, custom_filename):
        """Sets the custom_filename of this DocumentsDocumentWrite.


        :param custom_filename: The custom_filename of this DocumentsDocumentWrite.  # noqa: E501
        :type: str
        """

        self._custom_filename = custom_filename

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
        if issubclass(DocumentsDocumentWrite, dict):
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
        if not isinstance(other, DocumentsDocumentWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
