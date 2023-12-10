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

class EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite(object):
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
        'context': 'OneOfEquipmentMaintenanceJsonldEquipmentMaintenanceItemWriteContext',
        'id': 'str',
        'type': 'str',
        'status': 'str',
        'static_interval': 'datetime',
        'dynamic_interval': 'datetime',
        'last_run': 'datetime',
        'equipment': 'str',
        'task': 'str',
        'interval_length': 'int',
        'task_todo': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'status': 'status',
        'static_interval': 'staticInterval',
        'dynamic_interval': 'dynamicInterval',
        'last_run': 'lastRun',
        'equipment': 'equipment',
        'task': 'task',
        'interval_length': 'intervalLength',
        'task_todo': 'taskTodo'
    }

    def __init__(self, context=None, id=None, type=None, status=None, static_interval=None, dynamic_interval=None, last_run=None, equipment=None, task=None, interval_length=None, task_todo=None):  # noqa: E501
        """EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._status = None
        self._static_interval = None
        self._dynamic_interval = None
        self._last_run = None
        self._equipment = None
        self._task = None
        self._interval_length = None
        self._task_todo = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if static_interval is not None:
            self.static_interval = static_interval
        if dynamic_interval is not None:
            self.dynamic_interval = dynamic_interval
        if last_run is not None:
            self.last_run = last_run
        if equipment is not None:
            self.equipment = equipment
        if task is not None:
            self.task = task
        if interval_length is not None:
            self.interval_length = interval_length
        if task_todo is not None:
            self.task_todo = task_todo

    @property
    def context(self):
        """Gets the context of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The context of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: OneOfEquipmentMaintenanceJsonldEquipmentMaintenanceItemWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param context: The context of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: OneOfEquipmentMaintenanceJsonldEquipmentMaintenanceItemWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The id of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param id: The id of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The type of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param type: The type of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def status(self):
        """Gets the status of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The status of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param status: The status of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def static_interval(self):
        """Gets the static_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The static_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: datetime
        """
        return self._static_interval

    @static_interval.setter
    def static_interval(self, static_interval):
        """Sets the static_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param static_interval: The static_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: datetime
        """

        self._static_interval = static_interval

    @property
    def dynamic_interval(self):
        """Gets the dynamic_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The dynamic_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: datetime
        """
        return self._dynamic_interval

    @dynamic_interval.setter
    def dynamic_interval(self, dynamic_interval):
        """Sets the dynamic_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param dynamic_interval: The dynamic_interval of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: datetime
        """

        self._dynamic_interval = dynamic_interval

    @property
    def last_run(self):
        """Gets the last_run of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The last_run of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run

    @last_run.setter
    def last_run(self, last_run):
        """Sets the last_run of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param last_run: The last_run of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: datetime
        """

        self._last_run = last_run

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The equipment of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param equipment: The equipment of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: str
        """

        self._equipment = equipment

    @property
    def task(self):
        """Gets the task of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The task of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param task: The task of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: str
        """

        self._task = task

    @property
    def interval_length(self):
        """Gets the interval_length of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The interval_length of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: int
        """
        return self._interval_length

    @interval_length.setter
    def interval_length(self, interval_length):
        """Sets the interval_length of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param interval_length: The interval_length of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: int
        """

        self._interval_length = interval_length

    @property
    def task_todo(self):
        """Gets the task_todo of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501


        :return: The task_todo of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._task_todo

    @task_todo.setter
    def task_todo(self, task_todo):
        """Sets the task_todo of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.


        :param task_todo: The task_todo of this EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._task_todo = task_todo

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
        if issubclass(EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite, dict):
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
        if not isinstance(other, EquipmentMaintenanceJsonldEquipmentMaintenanceItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
