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

class FeedbackFeedbackItemWrite(object):
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
        'text': 'str',
        'area': 'str',
        'screenshots': 'list[str]',
        'is_problem': 'bool',
        'comment': 'str'
    }

    attribute_map = {
        'text': 'text',
        'area': 'area',
        'screenshots': 'screenshots',
        'is_problem': 'isProblem',
        'comment': 'comment'
    }

    def __init__(self, text=None, area='feedback', screenshots=None, is_problem=True, comment=None):  # noqa: E501
        """FeedbackFeedbackItemWrite - a model defined in Swagger"""  # noqa: E501
        self._text = None
        self._area = None
        self._screenshots = None
        self._is_problem = None
        self._comment = None
        self.discriminator = None
        if text is not None:
            self.text = text
        if area is not None:
            self.area = area
        if screenshots is not None:
            self.screenshots = screenshots
        if is_problem is not None:
            self.is_problem = is_problem
        if comment is not None:
            self.comment = comment

    @property
    def text(self):
        """Gets the text of this FeedbackFeedbackItemWrite.  # noqa: E501


        :return: The text of this FeedbackFeedbackItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this FeedbackFeedbackItemWrite.


        :param text: The text of this FeedbackFeedbackItemWrite.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def area(self):
        """Gets the area of this FeedbackFeedbackItemWrite.  # noqa: E501


        :return: The area of this FeedbackFeedbackItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._area

    @area.setter
    def area(self, area):
        """Sets the area of this FeedbackFeedbackItemWrite.


        :param area: The area of this FeedbackFeedbackItemWrite.  # noqa: E501
        :type: str
        """

        self._area = area

    @property
    def screenshots(self):
        """Gets the screenshots of this FeedbackFeedbackItemWrite.  # noqa: E501


        :return: The screenshots of this FeedbackFeedbackItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._screenshots

    @screenshots.setter
    def screenshots(self, screenshots):
        """Sets the screenshots of this FeedbackFeedbackItemWrite.


        :param screenshots: The screenshots of this FeedbackFeedbackItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._screenshots = screenshots

    @property
    def is_problem(self):
        """Gets the is_problem of this FeedbackFeedbackItemWrite.  # noqa: E501


        :return: The is_problem of this FeedbackFeedbackItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_problem

    @is_problem.setter
    def is_problem(self, is_problem):
        """Sets the is_problem of this FeedbackFeedbackItemWrite.


        :param is_problem: The is_problem of this FeedbackFeedbackItemWrite.  # noqa: E501
        :type: bool
        """

        self._is_problem = is_problem

    @property
    def comment(self):
        """Gets the comment of this FeedbackFeedbackItemWrite.  # noqa: E501


        :return: The comment of this FeedbackFeedbackItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this FeedbackFeedbackItemWrite.


        :param comment: The comment of this FeedbackFeedbackItemWrite.  # noqa: E501
        :type: str
        """

        self._comment = comment

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
        if issubclass(FeedbackFeedbackItemWrite, dict):
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
        if not isinstance(other, FeedbackFeedbackItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
