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

class TaskSetTranslationTasksetTranslationWrite(object):
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
        'object': 'str',
        'content': 'str',
        'locale': 'str'
    }

    attribute_map = {
        'object': 'object',
        'content': 'content',
        'locale': 'locale'
    }

    def __init__(self, object=None, content=None, locale=None):  # noqa: E501
        """TaskSetTranslationTasksetTranslationWrite - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._content = None
        self._locale = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if content is not None:
            self.content = content
        if locale is not None:
            self.locale = locale

    @property
    def object(self):
        """Gets the object of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501


        :return: The object of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this TaskSetTranslationTasksetTranslationWrite.


        :param object: The object of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def content(self):
        """Gets the content of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501


        :return: The content of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TaskSetTranslationTasksetTranslationWrite.


        :param content: The content of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def locale(self):
        """Gets the locale of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501


        :return: The locale of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this TaskSetTranslationTasksetTranslationWrite.


        :param locale: The locale of this TaskSetTranslationTasksetTranslationWrite.  # noqa: E501
        :type: str
        """

        self._locale = locale

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
        if issubclass(TaskSetTranslationTasksetTranslationWrite, dict):
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
        if not isinstance(other, TaskSetTranslationTasksetTranslationWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
