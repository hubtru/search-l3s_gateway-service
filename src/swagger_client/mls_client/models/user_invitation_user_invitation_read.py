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

class UserInvitationUserInvitationRead(object):
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
        'code': 'str',
        'invitor': 'str',
        'email': 'str',
        'role': 'str',
        'organization': 'str',
        'groups': 'list[str]',
        'approved': 'bool'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'code': 'code',
        'invitor': 'invitor',
        'email': 'email',
        'role': 'role',
        'organization': 'organization',
        'groups': 'groups',
        'approved': 'approved'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, code=None, invitor=None, email=None, role=None, organization=None, groups=None, approved=None):  # noqa: E501
        """UserInvitationUserInvitationRead - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._code = None
        self._invitor = None
        self._email = None
        self._role = None
        self._organization = None
        self._groups = None
        self._approved = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        self.code = code
        if invitor is not None:
            self.invitor = invitor
        self.email = email
        self.role = role
        self.organization = organization
        if groups is not None:
            self.groups = groups
        if approved is not None:
            self.approved = approved

    @property
    def created_at(self):
        """Gets the created_at of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The created_at of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserInvitationUserInvitationRead.


        :param created_at: The created_at of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The updated_at of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserInvitationUserInvitationRead.


        :param updated_at: The updated_at of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The id of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserInvitationUserInvitationRead.


        :param id: The id of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def code(self):
        """Gets the code of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The code of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this UserInvitationUserInvitationRead.


        :param code: The code of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def invitor(self):
        """Gets the invitor of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The invitor of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: str
        """
        return self._invitor

    @invitor.setter
    def invitor(self, invitor):
        """Sets the invitor of this UserInvitationUserInvitationRead.


        :param invitor: The invitor of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: str
        """

        self._invitor = invitor

    @property
    def email(self):
        """Gets the email of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The email of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserInvitationUserInvitationRead.


        :param email: The email of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def role(self):
        """Gets the role of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The role of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserInvitationUserInvitationRead.


        :param role: The role of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: str
        """
        if role is None:
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501

        self._role = role

    @property
    def organization(self):
        """Gets the organization of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The organization of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this UserInvitationUserInvitationRead.


        :param organization: The organization of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: str
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def groups(self):
        """Gets the groups of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The groups of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserInvitationUserInvitationRead.


        :param groups: The groups of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: list[str]
        """

        self._groups = groups

    @property
    def approved(self):
        """Gets the approved of this UserInvitationUserInvitationRead.  # noqa: E501


        :return: The approved of this UserInvitationUserInvitationRead.  # noqa: E501
        :rtype: bool
        """
        return self._approved

    @approved.setter
    def approved(self, approved):
        """Sets the approved of this UserInvitationUserInvitationRead.


        :param approved: The approved of this UserInvitationUserInvitationRead.  # noqa: E501
        :type: bool
        """

        self._approved = approved

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
        if issubclass(UserInvitationUserInvitationRead, dict):
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
        if not isinstance(other, UserInvitationUserInvitationRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
