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

class InlineResponse200Hydraview(object):
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
        'hydrafirst': 'str',
        'hydralast': 'str',
        'hydraprevious': 'str',
        'hydranext': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'hydrafirst': 'hydra:first',
        'hydralast': 'hydra:last',
        'hydraprevious': 'hydra:previous',
        'hydranext': 'hydra:next'
    }

    def __init__(self, id=None, type=None, hydrafirst=None, hydralast=None, hydraprevious=None, hydranext=None):  # noqa: E501
        """InlineResponse200Hydraview - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._hydrafirst = None
        self._hydralast = None
        self._hydraprevious = None
        self._hydranext = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if hydrafirst is not None:
            self.hydrafirst = hydrafirst
        if hydralast is not None:
            self.hydralast = hydralast
        if hydraprevious is not None:
            self.hydraprevious = hydraprevious
        if hydranext is not None:
            self.hydranext = hydranext

    @property
    def id(self):
        """Gets the id of this InlineResponse200Hydraview.  # noqa: E501


        :return: The id of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse200Hydraview.


        :param id: The id of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this InlineResponse200Hydraview.  # noqa: E501


        :return: The type of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse200Hydraview.


        :param type: The type of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def hydrafirst(self):
        """Gets the hydrafirst of this InlineResponse200Hydraview.  # noqa: E501


        :return: The hydrafirst of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._hydrafirst

    @hydrafirst.setter
    def hydrafirst(self, hydrafirst):
        """Sets the hydrafirst of this InlineResponse200Hydraview.


        :param hydrafirst: The hydrafirst of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._hydrafirst = hydrafirst

    @property
    def hydralast(self):
        """Gets the hydralast of this InlineResponse200Hydraview.  # noqa: E501


        :return: The hydralast of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._hydralast

    @hydralast.setter
    def hydralast(self, hydralast):
        """Sets the hydralast of this InlineResponse200Hydraview.


        :param hydralast: The hydralast of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._hydralast = hydralast

    @property
    def hydraprevious(self):
        """Gets the hydraprevious of this InlineResponse200Hydraview.  # noqa: E501


        :return: The hydraprevious of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._hydraprevious

    @hydraprevious.setter
    def hydraprevious(self, hydraprevious):
        """Sets the hydraprevious of this InlineResponse200Hydraview.


        :param hydraprevious: The hydraprevious of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._hydraprevious = hydraprevious

    @property
    def hydranext(self):
        """Gets the hydranext of this InlineResponse200Hydraview.  # noqa: E501


        :return: The hydranext of this InlineResponse200Hydraview.  # noqa: E501
        :rtype: str
        """
        return self._hydranext

    @hydranext.setter
    def hydranext(self, hydranext):
        """Sets the hydranext of this InlineResponse200Hydraview.


        :param hydranext: The hydranext of this InlineResponse200Hydraview.  # noqa: E501
        :type: str
        """

        self._hydranext = hydranext

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
        if issubclass(InlineResponse200Hydraview, dict):
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
        if not isinstance(other, InlineResponse200Hydraview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
