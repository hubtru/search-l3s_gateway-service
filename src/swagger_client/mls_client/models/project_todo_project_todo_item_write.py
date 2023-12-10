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

class ProjectTodoProjectTodoItemWrite(object):
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
        'project': 'str',
        'instructors_to_notify': 'list[str]',
        'task_todos': 'list[str]'
    }

    attribute_map = {
        'project': 'project',
        'instructors_to_notify': 'instructorsToNotify',
        'task_todos': 'taskTodos'
    }

    def __init__(self, project=None, instructors_to_notify=None, task_todos=None):  # noqa: E501
        """ProjectTodoProjectTodoItemWrite - a model defined in Swagger"""  # noqa: E501
        self._project = None
        self._instructors_to_notify = None
        self._task_todos = None
        self.discriminator = None
        self.project = project
        if instructors_to_notify is not None:
            self.instructors_to_notify = instructors_to_notify
        if task_todos is not None:
            self.task_todos = task_todos

    @property
    def project(self):
        """Gets the project of this ProjectTodoProjectTodoItemWrite.  # noqa: E501


        :return: The project of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectTodoProjectTodoItemWrite.


        :param project: The project of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :type: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def instructors_to_notify(self):
        """Gets the instructors_to_notify of this ProjectTodoProjectTodoItemWrite.  # noqa: E501


        :return: The instructors_to_notify of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._instructors_to_notify

    @instructors_to_notify.setter
    def instructors_to_notify(self, instructors_to_notify):
        """Sets the instructors_to_notify of this ProjectTodoProjectTodoItemWrite.


        :param instructors_to_notify: The instructors_to_notify of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._instructors_to_notify = instructors_to_notify

    @property
    def task_todos(self):
        """Gets the task_todos of this ProjectTodoProjectTodoItemWrite.  # noqa: E501


        :return: The task_todos of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todos

    @task_todos.setter
    def task_todos(self, task_todos):
        """Sets the task_todos of this ProjectTodoProjectTodoItemWrite.


        :param task_todos: The task_todos of this ProjectTodoProjectTodoItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_todos = task_todos

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
        if issubclass(ProjectTodoProjectTodoItemWrite, dict):
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
        if not isinstance(other, ProjectTodoProjectTodoItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
