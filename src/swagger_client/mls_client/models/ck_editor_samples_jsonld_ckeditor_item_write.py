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

class CKEditorSamplesJsonldCkeditorItemWrite(object):
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
        'context': 'OneOfCKEditorSamplesJsonldCkeditorItemWriteContext',
        'id': 'str',
        'type': 'str',
        'updated_at': 'datetime',
        'title': 'str',
        'simple_text_field': 'str',
        'classic_text_field': 'str',
        'default_text_field': 'str',
        'full_text_field': 'str',
        'chat_text_field': 'str',
        'files': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'updated_at': 'updatedAt',
        'title': 'title',
        'simple_text_field': 'simpleTextField',
        'classic_text_field': 'classicTextField',
        'default_text_field': 'defaultTextField',
        'full_text_field': 'fullTextField',
        'chat_text_field': 'chatTextField',
        'files': 'files'
    }

    def __init__(self, context=None, id=None, type=None, updated_at=None, title=None, simple_text_field=None, classic_text_field=None, default_text_field=None, full_text_field=None, chat_text_field=None, files=None):  # noqa: E501
        """CKEditorSamplesJsonldCkeditorItemWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._updated_at = None
        self._title = None
        self._simple_text_field = None
        self._classic_text_field = None
        self._default_text_field = None
        self._full_text_field = None
        self._chat_text_field = None
        self._files = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if title is not None:
            self.title = title
        if simple_text_field is not None:
            self.simple_text_field = simple_text_field
        if classic_text_field is not None:
            self.classic_text_field = classic_text_field
        if default_text_field is not None:
            self.default_text_field = default_text_field
        if full_text_field is not None:
            self.full_text_field = full_text_field
        if chat_text_field is not None:
            self.chat_text_field = chat_text_field
        if files is not None:
            self.files = files

    @property
    def context(self):
        """Gets the context of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The context of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: OneOfCKEditorSamplesJsonldCkeditorItemWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param context: The context of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: OneOfCKEditorSamplesJsonldCkeditorItemWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The id of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param id: The id of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The type of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param type: The type of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The updated_at of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param updated_at: The updated_at of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def title(self):
        """Gets the title of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The title of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param title: The title of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def simple_text_field(self):
        """Gets the simple_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The simple_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._simple_text_field

    @simple_text_field.setter
    def simple_text_field(self, simple_text_field):
        """Sets the simple_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param simple_text_field: The simple_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._simple_text_field = simple_text_field

    @property
    def classic_text_field(self):
        """Gets the classic_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The classic_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._classic_text_field

    @classic_text_field.setter
    def classic_text_field(self, classic_text_field):
        """Sets the classic_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param classic_text_field: The classic_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._classic_text_field = classic_text_field

    @property
    def default_text_field(self):
        """Gets the default_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The default_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._default_text_field

    @default_text_field.setter
    def default_text_field(self, default_text_field):
        """Sets the default_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param default_text_field: The default_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._default_text_field = default_text_field

    @property
    def full_text_field(self):
        """Gets the full_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The full_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._full_text_field

    @full_text_field.setter
    def full_text_field(self, full_text_field):
        """Sets the full_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param full_text_field: The full_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._full_text_field = full_text_field

    @property
    def chat_text_field(self):
        """Gets the chat_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The chat_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._chat_text_field

    @chat_text_field.setter
    def chat_text_field(self, chat_text_field):
        """Sets the chat_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param chat_text_field: The chat_text_field of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: str
        """

        self._chat_text_field = chat_text_field

    @property
    def files(self):
        """Gets the files of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501


        :return: The files of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this CKEditorSamplesJsonldCkeditorItemWrite.


        :param files: The files of this CKEditorSamplesJsonldCkeditorItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._files = files

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
        if issubclass(CKEditorSamplesJsonldCkeditorItemWrite, dict):
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
        if not isinstance(other, CKEditorSamplesJsonldCkeditorItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
