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

class TaskStepCategoryJsonld(object):
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
        'context': 'OneOfTaskStepCategoryJsonldContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'color': 'str',
        'organization': 'str',
        'icon': 'str',
        'position': 'int'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'color': 'color',
        'organization': 'organization',
        'icon': 'icon',
        'position': 'position'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, title=None, color=None, organization=None, icon=None, position=None):  # noqa: E501
        """TaskStepCategoryJsonld - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._color = None
        self._organization = None
        self._icon = None
        self._position = None
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
        if color is not None:
            self.color = color
        if organization is not None:
            self.organization = organization
        if icon is not None:
            self.icon = icon
        if position is not None:
            self.position = position

    @property
    def context(self):
        """Gets the context of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The context of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: OneOfTaskStepCategoryJsonldContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TaskStepCategoryJsonld.


        :param context: The context of this TaskStepCategoryJsonld.  # noqa: E501
        :type: OneOfTaskStepCategoryJsonldContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The id of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStepCategoryJsonld.


        :param id: The id of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The type of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskStepCategoryJsonld.


        :param type: The type of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The created_at of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskStepCategoryJsonld.


        :param created_at: The created_at of this TaskStepCategoryJsonld.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The updated_at of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskStepCategoryJsonld.


        :param updated_at: The updated_at of this TaskStepCategoryJsonld.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The id of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStepCategoryJsonld.


        :param id: The id of this TaskStepCategoryJsonld.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The title of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskStepCategoryJsonld.


        :param title: The title of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def color(self):
        """Gets the color of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The color of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this TaskStepCategoryJsonld.


        :param color: The color of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def organization(self):
        """Gets the organization of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The organization of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TaskStepCategoryJsonld.


        :param organization: The organization of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def icon(self):
        """Gets the icon of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The icon of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this TaskStepCategoryJsonld.


        :param icon: The icon of this TaskStepCategoryJsonld.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def position(self):
        """Gets the position of this TaskStepCategoryJsonld.  # noqa: E501


        :return: The position of this TaskStepCategoryJsonld.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskStepCategoryJsonld.


        :param position: The position of this TaskStepCategoryJsonld.  # noqa: E501
        :type: int
        """

        self._position = position

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
        if issubclass(TaskStepCategoryJsonld, dict):
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
        if not isinstance(other, TaskStepCategoryJsonld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
