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

class ChatMessageJsonldChatMessageRead(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'content': 'str',
        'sender': 'str',
        'type': 'str',
        'chat': 'str'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'content': 'content',
        'sender': 'sender',
        'type': 'type',
        'chat': 'chat'
    }

    def __init__(self, id=None, type=None, created_at=None, updated_at=None, id=None, content=None, sender=None, type=None, chat=None):  # noqa: E501
        """ChatMessageJsonldChatMessageRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._content = None
        self._sender = None
        self._type = None
        self._chat = None
        self.discriminator = None
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
        if content is not None:
            self.content = content
        if sender is not None:
            self.sender = sender
        if type is not None:
            self.type = type
        if chat is not None:
            self.chat = chat

    @property
    def id(self):
        """Gets the id of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The id of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChatMessageJsonldChatMessageRead.


        :param id: The id of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The type of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChatMessageJsonldChatMessageRead.


        :param type: The type of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The created_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ChatMessageJsonldChatMessageRead.


        :param created_at: The created_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The updated_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ChatMessageJsonldChatMessageRead.


        :param updated_at: The updated_at of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The id of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChatMessageJsonldChatMessageRead.


        :param id: The id of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def content(self):
        """Gets the content of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The content of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ChatMessageJsonldChatMessageRead.


        :param content: The content of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def sender(self):
        """Gets the sender of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The sender of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this ChatMessageJsonldChatMessageRead.


        :param sender: The sender of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._sender = sender

    @property
    def type(self):
        """Gets the type of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The type of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChatMessageJsonldChatMessageRead.


        :param type: The type of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def chat(self):
        """Gets the chat of this ChatMessageJsonldChatMessageRead.  # noqa: E501


        :return: The chat of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :rtype: str
        """
        return self._chat

    @chat.setter
    def chat(self, chat):
        """Sets the chat of this ChatMessageJsonldChatMessageRead.


        :param chat: The chat of this ChatMessageJsonldChatMessageRead.  # noqa: E501
        :type: str
        """

        self._chat = chat

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
        if issubclass(ChatMessageJsonldChatMessageRead, dict):
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
        if not isinstance(other, ChatMessageJsonldChatMessageRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
