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

class DirectoriesDirectoryItemWrite(object):
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
        'name': 'str',
        'owner': 'str',
        'parent': 'AnyOfDirectoriesDirectoryItemWriteParent',
        'directories': 'list[DirectoriesDirectoryItemWrite]',
        'documents': 'list[str]',
        'is_common': 'bool',
        'organization': 'str',
        'is_restricted': 'bool',
        'position': 'int',
        'shared_for_groups': 'list[str]',
        'shared_for_users': 'list[str]',
        'is_group': 'bool',
        'mls1_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'owner': 'owner',
        'parent': 'parent',
        'directories': 'directories',
        'documents': 'documents',
        'is_common': 'isCommon',
        'organization': 'organization',
        'is_restricted': 'isRestricted',
        'position': 'position',
        'shared_for_groups': 'sharedForGroups',
        'shared_for_users': 'sharedForUsers',
        'is_group': 'isGroup',
        'mls1_id': 'mls1Id'
    }

    def __init__(self, name=None, owner=None, parent=None, directories=None, documents=None, is_common=True, organization=None, is_restricted=None, position=None, shared_for_groups=None, shared_for_users=None, is_group=None, mls1_id=None):  # noqa: E501
        """DirectoriesDirectoryItemWrite - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._owner = None
        self._parent = None
        self._directories = None
        self._documents = None
        self._is_common = None
        self._organization = None
        self._is_restricted = None
        self._position = None
        self._shared_for_groups = None
        self._shared_for_users = None
        self._is_group = None
        self._mls1_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if owner is not None:
            self.owner = owner
        if parent is not None:
            self.parent = parent
        if directories is not None:
            self.directories = directories
        if documents is not None:
            self.documents = documents
        if is_common is not None:
            self.is_common = is_common
        if organization is not None:
            self.organization = organization
        if is_restricted is not None:
            self.is_restricted = is_restricted
        if position is not None:
            self.position = position
        if shared_for_groups is not None:
            self.shared_for_groups = shared_for_groups
        if shared_for_users is not None:
            self.shared_for_users = shared_for_users
        if is_group is not None:
            self.is_group = is_group
        if mls1_id is not None:
            self.mls1_id = mls1_id

    @property
    def name(self):
        """Gets the name of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The name of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DirectoriesDirectoryItemWrite.


        :param name: The name of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def owner(self):
        """Gets the owner of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The owner of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DirectoriesDirectoryItemWrite.


        :param owner: The owner of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def parent(self):
        """Gets the parent of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The parent of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: AnyOfDirectoriesDirectoryItemWriteParent
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DirectoriesDirectoryItemWrite.


        :param parent: The parent of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: AnyOfDirectoriesDirectoryItemWriteParent
        """

        self._parent = parent

    @property
    def directories(self):
        """Gets the directories of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The directories of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: list[DirectoriesDirectoryItemWrite]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this DirectoriesDirectoryItemWrite.


        :param directories: The directories of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: list[DirectoriesDirectoryItemWrite]
        """

        self._directories = directories

    @property
    def documents(self):
        """Gets the documents of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The documents of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this DirectoriesDirectoryItemWrite.


        :param documents: The documents of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._documents = documents

    @property
    def is_common(self):
        """Gets the is_common of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The is_common of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """Sets the is_common of this DirectoriesDirectoryItemWrite.


        :param is_common: The is_common of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: bool
        """

        self._is_common = is_common

    @property
    def organization(self):
        """Gets the organization of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The organization of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this DirectoriesDirectoryItemWrite.


        :param organization: The organization of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def is_restricted(self):
        """Gets the is_restricted of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The is_restricted of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        """Sets the is_restricted of this DirectoriesDirectoryItemWrite.


        :param is_restricted: The is_restricted of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: bool
        """

        self._is_restricted = is_restricted

    @property
    def position(self):
        """Gets the position of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The position of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DirectoriesDirectoryItemWrite.


        :param position: The position of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def shared_for_groups(self):
        """Gets the shared_for_groups of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The shared_for_groups of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_for_groups

    @shared_for_groups.setter
    def shared_for_groups(self, shared_for_groups):
        """Sets the shared_for_groups of this DirectoriesDirectoryItemWrite.


        :param shared_for_groups: The shared_for_groups of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._shared_for_groups = shared_for_groups

    @property
    def shared_for_users(self):
        """Gets the shared_for_users of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The shared_for_users of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_for_users

    @shared_for_users.setter
    def shared_for_users(self, shared_for_users):
        """Sets the shared_for_users of this DirectoriesDirectoryItemWrite.


        :param shared_for_users: The shared_for_users of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._shared_for_users = shared_for_users

    @property
    def is_group(self):
        """Gets the is_group of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The is_group of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this DirectoriesDirectoryItemWrite.


        :param is_group: The is_group of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: bool
        """

        self._is_group = is_group

    @property
    def mls1_id(self):
        """Gets the mls1_id of this DirectoriesDirectoryItemWrite.  # noqa: E501


        :return: The mls1_id of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this DirectoriesDirectoryItemWrite.


        :param mls1_id: The mls1_id of this DirectoriesDirectoryItemWrite.  # noqa: E501
        :type: int
        """

        self._mls1_id = mls1_id

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
        if issubclass(DirectoriesDirectoryItemWrite, dict):
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
        if not isinstance(other, DirectoriesDirectoryItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
