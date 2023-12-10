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

class TaskTaskItemWrite(object):
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
        'title': 'str',
        'task_set': 'str',
        'description': 'str',
        'preparation': 'str',
        'instructor_information': 'str',
        'due': 'float',
        'is_work_in_groups': 'bool',
        'lifecycle': 'str',
        'app_tags': 'list[str]',
        'task_todos': 'list[str]',
        'group_task_todos': 'list[str]',
        'skills': 'list[str]',
        'task_files': 'list[str]',
        'sample_solution': 'str',
        'preview_image': 'str',
        'linked_tasks': 'list[str]'
    }

    attribute_map = {
        'title': 'title',
        'task_set': 'taskSet',
        'description': 'description',
        'preparation': 'preparation',
        'instructor_information': 'instructorInformation',
        'due': 'due',
        'is_work_in_groups': 'isWorkInGroups',
        'lifecycle': 'lifecycle',
        'app_tags': 'appTags',
        'task_todos': 'taskTodos',
        'group_task_todos': 'groupTaskTodos',
        'skills': 'skills',
        'task_files': 'taskFiles',
        'sample_solution': 'sampleSolution',
        'preview_image': 'previewImage',
        'linked_tasks': 'linkedTasks'
    }

    def __init__(self, title=None, task_set=None, description=None, preparation=None, instructor_information=None, due=None, is_work_in_groups=None, lifecycle='DRAFT', app_tags=None, task_todos=None, group_task_todos=None, skills=None, task_files=None, sample_solution=None, preview_image=None, linked_tasks=None):  # noqa: E501
        """TaskTaskItemWrite - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._task_set = None
        self._description = None
        self._preparation = None
        self._instructor_information = None
        self._due = None
        self._is_work_in_groups = None
        self._lifecycle = None
        self._app_tags = None
        self._task_todos = None
        self._group_task_todos = None
        self._skills = None
        self._task_files = None
        self._sample_solution = None
        self._preview_image = None
        self._linked_tasks = None
        self.discriminator = None
        if title is not None:
            self.title = title
        self.task_set = task_set
        if description is not None:
            self.description = description
        if preparation is not None:
            self.preparation = preparation
        if instructor_information is not None:
            self.instructor_information = instructor_information
        if due is not None:
            self.due = due
        if is_work_in_groups is not None:
            self.is_work_in_groups = is_work_in_groups
        if lifecycle is not None:
            self.lifecycle = lifecycle
        if app_tags is not None:
            self.app_tags = app_tags
        if task_todos is not None:
            self.task_todos = task_todos
        if group_task_todos is not None:
            self.group_task_todos = group_task_todos
        if skills is not None:
            self.skills = skills
        if task_files is not None:
            self.task_files = task_files
        if sample_solution is not None:
            self.sample_solution = sample_solution
        if preview_image is not None:
            self.preview_image = preview_image
        if linked_tasks is not None:
            self.linked_tasks = linked_tasks

    @property
    def title(self):
        """Gets the title of this TaskTaskItemWrite.  # noqa: E501


        :return: The title of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskTaskItemWrite.


        :param title: The title of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def task_set(self):
        """Gets the task_set of this TaskTaskItemWrite.  # noqa: E501


        :return: The task_set of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._task_set

    @task_set.setter
    def task_set(self, task_set):
        """Sets the task_set of this TaskTaskItemWrite.


        :param task_set: The task_set of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """
        if task_set is None:
            raise ValueError("Invalid value for `task_set`, must not be `None`")  # noqa: E501

        self._task_set = task_set

    @property
    def description(self):
        """Gets the description of this TaskTaskItemWrite.  # noqa: E501


        :return: The description of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaskTaskItemWrite.


        :param description: The description of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def preparation(self):
        """Gets the preparation of this TaskTaskItemWrite.  # noqa: E501


        :return: The preparation of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._preparation

    @preparation.setter
    def preparation(self, preparation):
        """Sets the preparation of this TaskTaskItemWrite.


        :param preparation: The preparation of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._preparation = preparation

    @property
    def instructor_information(self):
        """Gets the instructor_information of this TaskTaskItemWrite.  # noqa: E501


        :return: The instructor_information of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._instructor_information

    @instructor_information.setter
    def instructor_information(self, instructor_information):
        """Sets the instructor_information of this TaskTaskItemWrite.


        :param instructor_information: The instructor_information of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._instructor_information = instructor_information

    @property
    def due(self):
        """Gets the due of this TaskTaskItemWrite.  # noqa: E501


        :return: The due of this TaskTaskItemWrite.  # noqa: E501
        :rtype: float
        """
        return self._due

    @due.setter
    def due(self, due):
        """Sets the due of this TaskTaskItemWrite.


        :param due: The due of this TaskTaskItemWrite.  # noqa: E501
        :type: float
        """

        self._due = due

    @property
    def is_work_in_groups(self):
        """Gets the is_work_in_groups of this TaskTaskItemWrite.  # noqa: E501


        :return: The is_work_in_groups of this TaskTaskItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._is_work_in_groups

    @is_work_in_groups.setter
    def is_work_in_groups(self, is_work_in_groups):
        """Sets the is_work_in_groups of this TaskTaskItemWrite.


        :param is_work_in_groups: The is_work_in_groups of this TaskTaskItemWrite.  # noqa: E501
        :type: bool
        """

        self._is_work_in_groups = is_work_in_groups

    @property
    def lifecycle(self):
        """Gets the lifecycle of this TaskTaskItemWrite.  # noqa: E501


        :return: The lifecycle of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this TaskTaskItemWrite.


        :param lifecycle: The lifecycle of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._lifecycle = lifecycle

    @property
    def app_tags(self):
        """Gets the app_tags of this TaskTaskItemWrite.  # noqa: E501


        :return: The app_tags of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_tags

    @app_tags.setter
    def app_tags(self, app_tags):
        """Sets the app_tags of this TaskTaskItemWrite.


        :param app_tags: The app_tags of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._app_tags = app_tags

    @property
    def task_todos(self):
        """Gets the task_todos of this TaskTaskItemWrite.  # noqa: E501


        :return: The task_todos of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todos

    @task_todos.setter
    def task_todos(self, task_todos):
        """Sets the task_todos of this TaskTaskItemWrite.


        :param task_todos: The task_todos of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_todos = task_todos

    @property
    def group_task_todos(self):
        """Gets the group_task_todos of this TaskTaskItemWrite.  # noqa: E501


        :return: The group_task_todos of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_task_todos

    @group_task_todos.setter
    def group_task_todos(self, group_task_todos):
        """Sets the group_task_todos of this TaskTaskItemWrite.


        :param group_task_todos: The group_task_todos of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._group_task_todos = group_task_todos

    @property
    def skills(self):
        """Gets the skills of this TaskTaskItemWrite.  # noqa: E501


        :return: The skills of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._skills

    @skills.setter
    def skills(self, skills):
        """Sets the skills of this TaskTaskItemWrite.


        :param skills: The skills of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._skills = skills

    @property
    def task_files(self):
        """Gets the task_files of this TaskTaskItemWrite.  # noqa: E501


        :return: The task_files of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_files

    @task_files.setter
    def task_files(self, task_files):
        """Sets the task_files of this TaskTaskItemWrite.


        :param task_files: The task_files of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_files = task_files

    @property
    def sample_solution(self):
        """Gets the sample_solution of this TaskTaskItemWrite.  # noqa: E501


        :return: The sample_solution of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._sample_solution

    @sample_solution.setter
    def sample_solution(self, sample_solution):
        """Sets the sample_solution of this TaskTaskItemWrite.


        :param sample_solution: The sample_solution of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._sample_solution = sample_solution

    @property
    def preview_image(self):
        """Gets the preview_image of this TaskTaskItemWrite.  # noqa: E501


        :return: The preview_image of this TaskTaskItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._preview_image

    @preview_image.setter
    def preview_image(self, preview_image):
        """Sets the preview_image of this TaskTaskItemWrite.


        :param preview_image: The preview_image of this TaskTaskItemWrite.  # noqa: E501
        :type: str
        """

        self._preview_image = preview_image

    @property
    def linked_tasks(self):
        """Gets the linked_tasks of this TaskTaskItemWrite.  # noqa: E501


        :return: The linked_tasks of this TaskTaskItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._linked_tasks

    @linked_tasks.setter
    def linked_tasks(self, linked_tasks):
        """Sets the linked_tasks of this TaskTaskItemWrite.


        :param linked_tasks: The linked_tasks of this TaskTaskItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._linked_tasks = linked_tasks

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
        if issubclass(TaskTaskItemWrite, dict):
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
        if not isinstance(other, TaskTaskItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
