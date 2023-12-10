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

class GuestRoleRequestGuestRoleRequestItemRead(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'organization': 'str',
        'requester': 'str',
        'approved': 'bool',
        'apprentice': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'organization': 'organization',
        'requester': 'requester',
        'approved': 'approved',
        'apprentice': 'apprentice'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, organization=None, requester=None, approved=None, apprentice=None):  # noqa: E501
        """GuestRoleRequestGuestRoleRequestItemRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._organization = None
        self._requester = None
        self._approved = None
        self._apprentice = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if organization is not None:
            self.organization = organization
        if requester is not None:
            self.requester = requester
        if approved is not None:
            self.approved = approved
        if apprentice is not None:
            self.apprentice = apprentice

    @property
    def created_at(self):
        """Gets the created_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The created_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GuestRoleRequestGuestRoleRequestItemRead.


        :param created_at: The created_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The updated_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GuestRoleRequestGuestRoleRequestItemRead.


        :param updated_at: The updated_at of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The id of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GuestRoleRequestGuestRoleRequestItemRead.


        :param id: The id of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def organization(self):
        """Gets the organization of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The organization of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this GuestRoleRequestGuestRoleRequestItemRead.


        :param organization: The organization of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def requester(self):
        """Gets the requester of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The requester of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: str
        """
        return self._requester

    @requester.setter
    def requester(self, requester):
        """Sets the requester of this GuestRoleRequestGuestRoleRequestItemRead.


        :param requester: The requester of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: str
        """

        self._requester = requester

    @property
    def approved(self):
        """Gets the approved of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The approved of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this GuestRoleRequestGuestRoleRequestItemRead.


        :param approved: The approved of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: bool
        """

        self._approved = approved

    @property
    def apprentice(self):
        """Gets the apprentice of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501


        :return: The apprentice of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :rtype: str
        """
        return self._apprentice

    @apprentice.setter
    def apprentice(self, apprentice):
        """Sets the apprentice of this GuestRoleRequestGuestRoleRequestItemRead.


        :param apprentice: The apprentice of this GuestRoleRequestGuestRoleRequestItemRead.  # noqa: E501
        :type: str
        """

        self._apprentice = apprentice

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
        if issubclass(GuestRoleRequestGuestRoleRequestItemRead, dict):
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
        if not isinstance(other, GuestRoleRequestGuestRoleRequestItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
