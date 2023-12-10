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

class FilemanagerCreateFileBody(object):
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
        'parent': 'int',
        'files': 'str',
        'feedback': 'int'
    }

    attribute_map = {
        'parent': 'parent',
        'files': 'files',
        'feedback': 'feedback'
    }

    def __init__(self, parent=None, files=None, feedback=None):  # noqa: E501
        """FilemanagerCreateFileBody - a model defined in Swagger"""  # noqa: E501
        self._parent = None
        self._files = None
        self._feedback = None
        self.discriminator = None
        if parent is not None:
            self.parent = parent
        if files is not None:
            self.files = files
        if feedback is not None:
            self.feedback = feedback

    @property
    def parent(self):
        """Gets the parent of this FilemanagerCreateFileBody.  # noqa: E501


        :return: The parent of this FilemanagerCreateFileBody.  # noqa: E501
        :rtype: int
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this FilemanagerCreateFileBody.


        :param parent: The parent of this FilemanagerCreateFileBody.  # noqa: E501
        :type: int
        """

        self._parent = parent

    @property
    def files(self):
        """Gets the files of this FilemanagerCreateFileBody.  # noqa: E501


        :return: The files of this FilemanagerCreateFileBody.  # noqa: E501
        :rtype: str
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this FilemanagerCreateFileBody.


        :param files: The files of this FilemanagerCreateFileBody.  # noqa: E501
        :type: str
        """

        self._files = files

    @property
    def feedback(self):
        """Gets the feedback of this FilemanagerCreateFileBody.  # noqa: E501


        :return: The feedback of this FilemanagerCreateFileBody.  # noqa: E501
        :rtype: int
        """
        return self._feedback

    @feedback.setter
    def feedback(self, feedback):
        """Sets the feedback of this FilemanagerCreateFileBody.


        :param feedback: The feedback of this FilemanagerCreateFileBody.  # noqa: E501
        :type: int
        """

        self._feedback = feedback

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
        if issubclass(FilemanagerCreateFileBody, dict):
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
        if not isinstance(other, FilemanagerCreateFileBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
