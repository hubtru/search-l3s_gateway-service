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

class DocumentsJsonldDocumentReadFileReadFileResourceRead(object):
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
        'id': 'str',
        'type': 'str',
        'owner': 'str',
        'parent': 'str',
        'is_common': 'bool',
        'organization': 'str',
        'is_restricted': 'bool',
        'mls1_id': 'int',
        'shared_for_groups': 'list[str]',
        'shared_users': 'list[str]',
        'is_group': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'custom_filename': 'str',
        'file_resource': 'FileResourceJsonldDocumentReadFileReadFileResourceRead'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'owner': 'owner',
        'parent': 'parent',
        'is_common': 'isCommon',
        'organization': 'organization',
        'is_restricted': 'isRestricted',
        'mls1_id': 'mls1Id',
        'shared_for_groups': 'sharedForGroups',
        'shared_users': 'sharedUsers',
        'is_group': 'isGroup',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'custom_filename': 'customFilename',
        'file_resource': 'fileResource'
    }

    def __init__(self, id=None, type=None, owner=None, parent=None, is_common=True, organization=None, is_restricted=None, mls1_id=None, shared_for_groups=None, shared_users=None, is_group=None, created_at=None, updated_at=None, id=None, custom_filename=None, file_resource=None):  # noqa: E501
        """DocumentsJsonldDocumentReadFileReadFileResourceRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._owner = None
        self._parent = None
        self._is_common = None
        self._organization = None
        self._is_restricted = None
        self._mls1_id = None
        self._shared_for_groups = None
        self._shared_users = None
        self._is_group = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._custom_filename = None
        self._file_resource = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
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
        if mls1_id is not None:
            self.mls1_id = mls1_id
        if shared_for_groups is not None:
            self.shared_for_groups = shared_for_groups
        if shared_users is not None:
            self.shared_users = shared_users
        if is_group is not None:
            self.is_group = is_group
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if custom_filename is not None:
            self.custom_filename = custom_filename
        if file_resource is not None:
            self.file_resource = file_resource

    @property
    def id(self):
        """Gets the id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param id: The id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The type of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param type: The type of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def owner(self):
        """Gets the owner of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The owner of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param owner: The owner of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def parent(self):
        """Gets the parent of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The parent of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param parent: The parent of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def is_common(self):
        """Gets the is_common of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The is_common of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_common

    @is_common.setter
    def is_common(self, is_common):
        """Sets the is_common of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param is_common: The is_common of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: bool
        """

        self._is_common = is_common

    @property
    def organization(self):
        """Gets the organization of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The organization of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param organization: The organization of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def is_restricted(self):
        """Gets the is_restricted of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The is_restricted of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_restricted

    @is_restricted.setter
    def is_restricted(self, is_restricted):
        """Sets the is_restricted of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param is_restricted: The is_restricted of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: bool
        """

        self._is_restricted = is_restricted

    @property
    def mls1_id(self):
        """Gets the mls1_id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The mls1_id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param mls1_id: The mls1_id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: int
        """

        self._mls1_id = mls1_id

    @property
    def shared_for_groups(self):
        """Gets the shared_for_groups of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The shared_for_groups of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_for_groups

    @shared_for_groups.setter
    def shared_for_groups(self, shared_for_groups):
        """Sets the shared_for_groups of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param shared_for_groups: The shared_for_groups of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_for_groups = shared_for_groups

    @property
    def shared_users(self):
        """Gets the shared_users of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The shared_users of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_users

    @shared_users.setter
    def shared_users(self, shared_users):
        """Sets the shared_users of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param shared_users: The shared_users of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_users = shared_users

    @property
    def is_group(self):
        """Gets the is_group of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The is_group of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_group

    @is_group.setter
    def is_group(self, is_group):
        """Sets the is_group of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param is_group: The is_group of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: bool
        """

        self._is_group = is_group

    @property
    def created_at(self):
        """Gets the created_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The created_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param created_at: The created_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The updated_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param updated_at: The updated_at of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param id: The id of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def custom_filename(self):
        """Gets the custom_filename of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The custom_filename of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: str
        """
        return self._custom_filename

    @custom_filename.setter
    def custom_filename(self, custom_filename):
        """Sets the custom_filename of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param custom_filename: The custom_filename of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: str
        """

        self._custom_filename = custom_filename

    @property
    def file_resource(self):
        """Gets the file_resource of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501


        :return: The file_resource of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :rtype: FileResourceJsonldDocumentReadFileReadFileResourceRead
        """
        return self._file_resource

    @file_resource.setter
    def file_resource(self, file_resource):
        """Sets the file_resource of this DocumentsJsonldDocumentReadFileReadFileResourceRead.


        :param file_resource: The file_resource of this DocumentsJsonldDocumentReadFileReadFileResourceRead.  # noqa: E501
        :type: FileResourceJsonldDocumentReadFileReadFileResourceRead
        """

        self._file_resource = file_resource

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
        if issubclass(DocumentsJsonldDocumentReadFileReadFileResourceRead, dict):
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
        if not isinstance(other, DocumentsJsonldDocumentReadFileReadFileResourceRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
