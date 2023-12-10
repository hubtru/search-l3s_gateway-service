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

class TaskTodoInfoJsonld(object):
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
        'context': 'OneOfTaskTodoInfoJsonldContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'status': 'str',
        'steps_processed': 'int',
        'locking_steps_processed': 'int',
        'task_todo': 'str',
        'max_steps_processed': 'int',
        'lock_after_step': 'list[str]',
        'working_time_intervals': 'list[str]',
        'due_time': 'int'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'status': 'status',
        'steps_processed': 'stepsProcessed',
        'locking_steps_processed': 'lockingStepsProcessed',
        'task_todo': 'taskTodo',
        'max_steps_processed': 'maxStepsProcessed',
        'lock_after_step': 'lockAfterStep',
        'working_time_intervals': 'workingTimeIntervals',
        'due_time': 'dueTime'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, status=None, steps_processed=None, locking_steps_processed=None, task_todo=None, max_steps_processed=None, lock_after_step=None, working_time_intervals=None, due_time=None):  # noqa: E501
        """TaskTodoInfoJsonld - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._status = None
        self._steps_processed = None
        self._locking_steps_processed = None
        self._task_todo = None
        self._max_steps_processed = None
        self._lock_after_step = None
        self._working_time_intervals = None
        self._due_time = None
        self.discriminator = None
        if context is not None:
            self.context = context
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
        self.status = status
        if steps_processed is not None:
            self.steps_processed = steps_processed
        if locking_steps_processed is not None:
            self.locking_steps_processed = locking_steps_processed
        if task_todo is not None:
            self.task_todo = task_todo
        if max_steps_processed is not None:
            self.max_steps_processed = max_steps_processed
        if lock_after_step is not None:
            self.lock_after_step = lock_after_step
        if working_time_intervals is not None:
            self.working_time_intervals = working_time_intervals
        if due_time is not None:
            self.due_time = due_time

    @property
    def context(self):
        """Gets the context of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The context of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: OneOfTaskTodoInfoJsonldContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this TaskTodoInfoJsonld.


        :param context: The context of this TaskTodoInfoJsonld.  # noqa: E501
        :type: OneOfTaskTodoInfoJsonldContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The id of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskTodoInfoJsonld.


        :param id: The id of this TaskTodoInfoJsonld.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The type of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaskTodoInfoJsonld.


        :param type: The type of this TaskTodoInfoJsonld.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The created_at of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskTodoInfoJsonld.


        :param created_at: The created_at of this TaskTodoInfoJsonld.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The updated_at of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskTodoInfoJsonld.


        :param updated_at: The updated_at of this TaskTodoInfoJsonld.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The id of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskTodoInfoJsonld.


        :param id: The id of this TaskTodoInfoJsonld.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def status(self):
        """Gets the status of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The status of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskTodoInfoJsonld.


        :param status: The status of this TaskTodoInfoJsonld.  # noqa: E501
        :type: str
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def steps_processed(self):
        """Gets the steps_processed of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._steps_processed

    @steps_processed.setter
    def steps_processed(self, steps_processed):
        """Sets the steps_processed of this TaskTodoInfoJsonld.


        :param steps_processed: The steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :type: int
        """

        self._steps_processed = steps_processed

    @property
    def locking_steps_processed(self):
        """Gets the locking_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The locking_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._locking_steps_processed

    @locking_steps_processed.setter
    def locking_steps_processed(self, locking_steps_processed):
        """Sets the locking_steps_processed of this TaskTodoInfoJsonld.


        :param locking_steps_processed: The locking_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :type: int
        """

        self._locking_steps_processed = locking_steps_processed

    @property
    def task_todo(self):
        """Gets the task_todo of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The task_todo of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._task_todo

    @task_todo.setter
    def task_todo(self, task_todo):
        """Sets the task_todo of this TaskTodoInfoJsonld.


        :param task_todo: The task_todo of this TaskTodoInfoJsonld.  # noqa: E501
        :type: str
        """

        self._task_todo = task_todo

    @property
    def max_steps_processed(self):
        """Gets the max_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The max_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._max_steps_processed

    @max_steps_processed.setter
    def max_steps_processed(self, max_steps_processed):
        """Sets the max_steps_processed of this TaskTodoInfoJsonld.


        :param max_steps_processed: The max_steps_processed of this TaskTodoInfoJsonld.  # noqa: E501
        :type: int
        """

        self._max_steps_processed = max_steps_processed

    @property
    def lock_after_step(self):
        """Gets the lock_after_step of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The lock_after_step of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._lock_after_step

    @lock_after_step.setter
    def lock_after_step(self, lock_after_step):
        """Sets the lock_after_step of this TaskTodoInfoJsonld.


        :param lock_after_step: The lock_after_step of this TaskTodoInfoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._lock_after_step = lock_after_step

    @property
    def working_time_intervals(self):
        """Gets the working_time_intervals of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The working_time_intervals of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._working_time_intervals

    @working_time_intervals.setter
    def working_time_intervals(self, working_time_intervals):
        """Sets the working_time_intervals of this TaskTodoInfoJsonld.


        :param working_time_intervals: The working_time_intervals of this TaskTodoInfoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._working_time_intervals = working_time_intervals

    @property
    def due_time(self):
        """Gets the due_time of this TaskTodoInfoJsonld.  # noqa: E501


        :return: The due_time of this TaskTodoInfoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._due_time

    @due_time.setter
    def due_time(self, due_time):
        """Sets the due_time of this TaskTodoInfoJsonld.


        :param due_time: The due_time of this TaskTodoInfoJsonld.  # noqa: E501
        :type: int
        """

        self._due_time = due_time

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
        if issubclass(TaskTodoInfoJsonld, dict):
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
        if not isinstance(other, TaskTodoInfoJsonld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
