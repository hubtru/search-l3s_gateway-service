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

class TaskSkill(object):
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
        'skill': 'str',
        'task': 'str',
        'level': 'str'
    }

    attribute_map = {
        'skill': 'skill',
        'task': 'task',
        'level': 'level'
    }

    def __init__(self, skill=None, task=None, level=None):  # noqa: E501
        """TaskSkill - a model defined in Swagger"""  # noqa: E501
        self._skill = None
        self._task = None
        self._level = None
        self.discriminator = None
        if skill is not None:
            self.skill = skill
        if task is not None:
            self.task = task
        if level is not None:
            self.level = level

    @property
    def skill(self):
        """Gets the skill of this TaskSkill.  # noqa: E501


        :return: The skill of this TaskSkill.  # noqa: E501
        :rtype: str
        """
        return self._skill

    @skill.setter
    def skill(self, skill):
        """Sets the skill of this TaskSkill.


        :param skill: The skill of this TaskSkill.  # noqa: E501
        :type: str
        """

        self._skill = skill

    @property
    def task(self):
        """Gets the task of this TaskSkill.  # noqa: E501


        :return: The task of this TaskSkill.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this TaskSkill.


        :param task: The task of this TaskSkill.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def level(self):
        """Gets the level of this TaskSkill.  # noqa: E501


        :return: The level of this TaskSkill.  # noqa: E501
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this TaskSkill.


        :param level: The level of this TaskSkill.  # noqa: E501
        :type: str
        """

        self._level = level

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
        if issubclass(TaskSkill, dict):
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
        if not isinstance(other, TaskSkill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
