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

class InterfaceTopicJsonldInterfaceTopicItemRead(object):
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
        'context': 'OneOfInterfaceTopicJsonldInterfaceTopicItemReadContext',
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'area': 'str',
        'title': 'str',
        'interface_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'area': 'area',
        'title': 'title',
        'interface_id': 'interfaceId',
        'type': 'type'
    }

    def __init__(self, context=None, id=None, type=None, id=None, area=None, title=None, interface_id=None, type=None):  # noqa: E501
        """InterfaceTopicJsonldInterfaceTopicItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._id = None
        self._area = None
        self._title = None
        self._interface_id = None
        self._type = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if area is not None:
            self.area = area
        if title is not None:
            self.title = title
        if interface_id is not None:
            self.interface_id = interface_id
        if type is not None:
            self.type = type

    @property
    def context(self):
        """Gets the context of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The context of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: OneOfInterfaceTopicJsonldInterfaceTopicItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param context: The context of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: OneOfInterfaceTopicJsonldInterfaceTopicItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param id: The id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param type: The type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param id: The id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def area(self):
        """Gets the area of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The area of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param area: The area of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def title(self):
        """Gets the title of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The title of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param title: The title of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def interface_id(self):
        """Gets the interface_id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The interface_id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._interface_id

    @interface_id.setter
    def interface_id(self, interface_id):
        """Sets the interface_id of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param interface_id: The interface_id of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._interface_id = interface_id

    @property
    def type(self):
        """Gets the type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501


        :return: The type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterfaceTopicJsonldInterfaceTopicItemRead.


        :param type: The type of this InterfaceTopicJsonldInterfaceTopicItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(InterfaceTopicJsonldInterfaceTopicItemRead, dict):
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
        if not isinstance(other, InterfaceTopicJsonldInterfaceTopicItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
