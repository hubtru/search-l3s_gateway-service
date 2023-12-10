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

class GroupJsonldGroupRead(object):
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
        'id': 'int',
        'title': 'str',
        'organization': 'AnyOfGroupJsonldGroupReadOrganization',
        'users': 'list[str]',
        'shared_directories': 'list[str]',
        'shared_documents': 'list[str]',
        'mls1_id': 'int'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'title': 'title',
        'organization': 'organization',
        'users': 'users',
        'shared_directories': 'sharedDirectories',
        'shared_documents': 'sharedDocuments',
        'mls1_id': 'mls1Id'
    }

    def __init__(self, id=None, type=None, id=None, title=None, organization=None, users=None, shared_directories=None, shared_documents=None, mls1_id=None):  # noqa: E501
        """GroupJsonldGroupRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._id = None
        self._title = None
        self._organization = None
        self._users = None
        self._shared_directories = None
        self._shared_documents = None
        self._mls1_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        self.title = title
        self.organization = organization
        if users is not None:
            self.users = users
        if shared_directories is not None:
            self.shared_directories = shared_directories
        if shared_documents is not None:
            self.shared_documents = shared_documents
        if mls1_id is not None:
            self.mls1_id = mls1_id

    @property
    def id(self):
        """Gets the id of this GroupJsonldGroupRead.  # noqa: E501


        :return: The id of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupJsonldGroupRead.


        :param id: The id of this GroupJsonldGroupRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupJsonldGroupRead.  # noqa: E501


        :return: The type of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupJsonldGroupRead.


        :param type: The type of this GroupJsonldGroupRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this GroupJsonldGroupRead.  # noqa: E501


        :return: The id of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupJsonldGroupRead.


        :param id: The id of this GroupJsonldGroupRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this GroupJsonldGroupRead.  # noqa: E501


        :return: The title of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this GroupJsonldGroupRead.


        :param title: The title of this GroupJsonldGroupRead.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def organization(self):
        """Gets the organization of this GroupJsonldGroupRead.  # noqa: E501


        :return: The organization of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: AnyOfGroupJsonldGroupReadOrganization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this GroupJsonldGroupRead.


        :param organization: The organization of this GroupJsonldGroupRead.  # noqa: E501
        :type: AnyOfGroupJsonldGroupReadOrganization
        """
        if organization is None:
            raise ValueError("Invalid value for `organization`, must not be `None`")  # noqa: E501

        self._organization = organization

    @property
    def users(self):
        """Gets the users of this GroupJsonldGroupRead.  # noqa: E501


        :return: The users of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this GroupJsonldGroupRead.


        :param users: The users of this GroupJsonldGroupRead.  # noqa: E501
        :type: list[str]
        """

        self._users = users

    @property
    def shared_directories(self):
        """Gets the shared_directories of this GroupJsonldGroupRead.  # noqa: E501


        :return: The shared_directories of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_directories

    @shared_directories.setter
    def shared_directories(self, shared_directories):
        """Sets the shared_directories of this GroupJsonldGroupRead.


        :param shared_directories: The shared_directories of this GroupJsonldGroupRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_directories = shared_directories

    @property
    def shared_documents(self):
        """Gets the shared_documents of this GroupJsonldGroupRead.  # noqa: E501


        :return: The shared_documents of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_documents

    @shared_documents.setter
    def shared_documents(self, shared_documents):
        """Sets the shared_documents of this GroupJsonldGroupRead.


        :param shared_documents: The shared_documents of this GroupJsonldGroupRead.  # noqa: E501
        :type: list[str]
        """

        self._shared_documents = shared_documents

    @property
    def mls1_id(self):
        """Gets the mls1_id of this GroupJsonldGroupRead.  # noqa: E501


        :return: The mls1_id of this GroupJsonldGroupRead.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this GroupJsonldGroupRead.


        :param mls1_id: The mls1_id of this GroupJsonldGroupRead.  # noqa: E501
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
        if issubclass(GroupJsonldGroupRead, dict):
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
        if not isinstance(other, GroupJsonldGroupRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
