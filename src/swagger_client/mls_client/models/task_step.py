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

class TaskStep(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'title': 'str',
        'content': 'list[str]',
        'helping_topics': 'list[str]',
        'task_step_category': 'str',
        'parent': 'str',
        'task_steps': 'list[str]',
        'position': 'int',
        'task': 'str',
        'stop': 'bool',
        'connected_forms': 'list[str]',
        'files': 'list[str]',
        'trainee_notices': 'list[str]',
        'mls1_id': 'int',
        'root_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'title': 'title',
        'content': 'content',
        'helping_topics': 'helpingTopics',
        'task_step_category': 'taskStepCategory',
        'parent': 'parent',
        'task_steps': 'taskSteps',
        'position': 'position',
        'task': 'task',
        'stop': 'stop',
        'connected_forms': 'connectedForms',
        'files': 'files',
        'trainee_notices': 'traineeNotices',
        'mls1_id': 'mls1Id',
        'root_id': 'rootId'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, title=None, content=None, helping_topics=None, task_step_category=None, parent=None, task_steps=None, position=None, task=None, stop=None, connected_forms=None, files=None, trainee_notices=None, mls1_id=None, root_id=None):  # noqa: E501
        """TaskStep - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._title = None
        self._content = None
        self._helping_topics = None
        self._task_step_category = None
        self._parent = None
        self._task_steps = None
        self._position = None
        self._task = None
        self._stop = None
        self._connected_forms = None
        self._files = None
        self._trainee_notices = None
        self._mls1_id = None
        self._root_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        self.title = title
        if content is not None:
            self.content = content
        if helping_topics is not None:
            self.helping_topics = helping_topics
        if task_step_category is not None:
            self.task_step_category = task_step_category
        if parent is not None:
            self.parent = parent
        if task_steps is not None:
            self.task_steps = task_steps
        if position is not None:
            self.position = position
        if task is not None:
            self.task = task
        if stop is not None:
            self.stop = stop
        if connected_forms is not None:
            self.connected_forms = connected_forms
        if files is not None:
            self.files = files
        if trainee_notices is not None:
            self.trainee_notices = trainee_notices
        if mls1_id is not None:
            self.mls1_id = mls1_id
        if root_id is not None:
            self.root_id = root_id

    @property
    def created_at(self):
        """Gets the created_at of this TaskStep.  # noqa: E501


        :return: The created_at of this TaskStep.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskStep.


        :param created_at: The created_at of this TaskStep.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskStep.  # noqa: E501


        :return: The updated_at of this TaskStep.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskStep.


        :param updated_at: The updated_at of this TaskStep.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TaskStep.  # noqa: E501


        :return: The id of this TaskStep.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskStep.


        :param id: The id of this TaskStep.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TaskStep.  # noqa: E501


        :return: The title of this TaskStep.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskStep.


        :param title: The title of this TaskStep.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this TaskStep.  # noqa: E501


        :return: The content of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this TaskStep.


        :param content: The content of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._content = content

    @property
    def helping_topics(self):
        """Gets the helping_topics of this TaskStep.  # noqa: E501


        :return: The helping_topics of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._helping_topics

    @helping_topics.setter
    def helping_topics(self, helping_topics):
        """Sets the helping_topics of this TaskStep.


        :param helping_topics: The helping_topics of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._helping_topics = helping_topics

    @property
    def task_step_category(self):
        """Gets the task_step_category of this TaskStep.  # noqa: E501


        :return: The task_step_category of this TaskStep.  # noqa: E501
        :rtype: str
        """
        return self._task_step_category

    @task_step_category.setter
    def task_step_category(self, task_step_category):
        """Sets the task_step_category of this TaskStep.


        :param task_step_category: The task_step_category of this TaskStep.  # noqa: E501
        :type: str
        """

        self._task_step_category = task_step_category

    @property
    def parent(self):
        """Gets the parent of this TaskStep.  # noqa: E501


        :return: The parent of this TaskStep.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this TaskStep.


        :param parent: The parent of this TaskStep.  # noqa: E501
        :type: str
        """

        self._parent = parent

    @property
    def task_steps(self):
        """Gets the task_steps of this TaskStep.  # noqa: E501


        :return: The task_steps of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_steps

    @task_steps.setter
    def task_steps(self, task_steps):
        """Sets the task_steps of this TaskStep.


        :param task_steps: The task_steps of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._task_steps = task_steps

    @property
    def position(self):
        """Gets the position of this TaskStep.  # noqa: E501


        :return: The position of this TaskStep.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this TaskStep.


        :param position: The position of this TaskStep.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def task(self):
        """Gets the task of this TaskStep.  # noqa: E501


        :return: The task of this TaskStep.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this TaskStep.


        :param task: The task of this TaskStep.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def stop(self):
        """Gets the stop of this TaskStep.  # noqa: E501


        :return: The stop of this TaskStep.  # noqa: E501
        :rtype: bool
        """
        return self._stop

    @stop.setter
    def stop(self, stop):
        """Sets the stop of this TaskStep.


        :param stop: The stop of this TaskStep.  # noqa: E501
        :type: bool
        """

        self._stop = stop

    @property
    def connected_forms(self):
        """Gets the connected_forms of this TaskStep.  # noqa: E501


        :return: The connected_forms of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._connected_forms

    @connected_forms.setter
    def connected_forms(self, connected_forms):
        """Sets the connected_forms of this TaskStep.


        :param connected_forms: The connected_forms of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._connected_forms = connected_forms

    @property
    def files(self):
        """Gets the files of this TaskStep.  # noqa: E501


        :return: The files of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this TaskStep.


        :param files: The files of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._files = files

    @property
    def trainee_notices(self):
        """Gets the trainee_notices of this TaskStep.  # noqa: E501


        :return: The trainee_notices of this TaskStep.  # noqa: E501
        :rtype: list[str]
        """
        return self._trainee_notices

    @trainee_notices.setter
    def trainee_notices(self, trainee_notices):
        """Sets the trainee_notices of this TaskStep.


        :param trainee_notices: The trainee_notices of this TaskStep.  # noqa: E501
        :type: list[str]
        """

        self._trainee_notices = trainee_notices

    @property
    def mls1_id(self):
        """Gets the mls1_id of this TaskStep.  # noqa: E501


        :return: The mls1_id of this TaskStep.  # noqa: E501
        :rtype: int
        """
        return self._mls1_id

    @mls1_id.setter
    def mls1_id(self, mls1_id):
        """Sets the mls1_id of this TaskStep.


        :param mls1_id: The mls1_id of this TaskStep.  # noqa: E501
        :type: int
        """

        self._mls1_id = mls1_id

    @property
    def root_id(self):
        """Gets the root_id of this TaskStep.  # noqa: E501


        :return: The root_id of this TaskStep.  # noqa: E501
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this TaskStep.


        :param root_id: The root_id of this TaskStep.  # noqa: E501
        :type: str
        """

        self._root_id = root_id

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
        if issubclass(TaskStep, dict):
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
        if not isinstance(other, TaskStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
