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

class ScormGroupJsonldScormGroupItemRead(object):
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
        'context': 'OneOfScormGroupJsonldScormGroupItemReadContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'scorms': 'list[str]',
        'organizations': 'list[str]',
        'owner': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'scorms': 'scorms',
        'organizations': 'organizations',
        'owner': 'owner'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, title=None, scorms=None, organizations=None, owner=None):  # noqa: E501
        """ScormGroupJsonldScormGroupItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._scorms = None
        self._organizations = None
        self._owner = None
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
        self.title = title
        if scorms is not None:
            self.scorms = scorms
        if organizations is not None:
            self.organizations = organizations
        if owner is not None:
            self.owner = owner

    @property
    def context(self):
        """Gets the context of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The context of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: OneOfScormGroupJsonldScormGroupItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ScormGroupJsonldScormGroupItemRead.


        :param context: The context of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: OneOfScormGroupJsonldScormGroupItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScormGroupJsonldScormGroupItemRead.


        :param id: The id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The type of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ScormGroupJsonldScormGroupItemRead.


        :param type: The type of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The created_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ScormGroupJsonldScormGroupItemRead.


        :param created_at: The created_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The updated_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ScormGroupJsonldScormGroupItemRead.


        :param updated_at: The updated_at of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ScormGroupJsonldScormGroupItemRead.


        :param id: The id of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The title of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ScormGroupJsonldScormGroupItemRead.


        :param title: The title of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def scorms(self):
        """Gets the scorms of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The scorms of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._scorms

    @scorms.setter
    def scorms(self, scorms):
        """Sets the scorms of this ScormGroupJsonldScormGroupItemRead.


        :param scorms: The scorms of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: list[str]
        """

        self._scorms = scorms

    @property
    def organizations(self):
        """Gets the organizations of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The organizations of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this ScormGroupJsonldScormGroupItemRead.


        :param organizations: The organizations of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: list[str]
        """

        self._organizations = organizations

    @property
    def owner(self):
        """Gets the owner of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501


        :return: The owner of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ScormGroupJsonldScormGroupItemRead.


        :param owner: The owner of this ScormGroupJsonldScormGroupItemRead.  # noqa: E501
        :type: str
        """

        self._owner = owner

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
        if issubclass(ScormGroupJsonldScormGroupItemRead, dict):
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
        if not isinstance(other, ScormGroupJsonldScormGroupItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
