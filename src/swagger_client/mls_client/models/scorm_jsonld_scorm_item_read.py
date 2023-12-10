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

class ScormJsonldScormItemRead(object):
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
        'context': 'OneOfScormJsonldScormItemReadContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'path': 'str',
        'organization': 'str',
        'version': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'path': 'path',
        'organization': 'organization',
        'version': 'version'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, title=None, path=None, organization=None, version=None):  # noqa: E501
        """ScormJsonldScormItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._path = None
        self._organization = None
        self._version = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if path is not None:
            self.path = path
        if organization is not None:
            self.organization = organization
        if version is not None:
            self.version = version

    @property
    def context(self):
        """Gets the context of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The context of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: OneOfScormJsonldScormItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ScormJsonldScormItemRead.


        :param context: The context of this ScormJsonldScormItemRead.  # noqa: E501
        :type: OneOfScormJsonldScormItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The id of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScormJsonldScormItemRead.


        :param id: The id of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The type of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScormJsonldScormItemRead.


        :param type: The type of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The created_at of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ScormJsonldScormItemRead.


        :param created_at: The created_at of this ScormJsonldScormItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The updated_at of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ScormJsonldScormItemRead.


        :param updated_at: The updated_at of this ScormJsonldScormItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The id of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScormJsonldScormItemRead.


        :param id: The id of this ScormJsonldScormItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The title of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ScormJsonldScormItemRead.


        :param title: The title of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def path(self):
        """Gets the path of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The path of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ScormJsonldScormItemRead.


        :param path: The path of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def organization(self):
        """Gets the organization of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The organization of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this ScormJsonldScormItemRead.


        :param organization: The organization of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def version(self):
        """Gets the version of this ScormJsonldScormItemRead.  # noqa: E501


        :return: The version of this ScormJsonldScormItemRead.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ScormJsonldScormItemRead.


        :param version: The version of this ScormJsonldScormItemRead.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if issubclass(ScormJsonldScormItemRead, dict):
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
        if not isinstance(other, ScormJsonldScormItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
