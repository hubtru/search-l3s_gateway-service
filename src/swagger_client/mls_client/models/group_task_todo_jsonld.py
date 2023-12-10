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

class GroupTaskTodoJsonld(object):
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
        'context': 'OneOfGroupTaskTodoJsonldContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'task': 'str',
        'form_solutions': 'list[str]',
        'form_answers': 'list[str]',
        'form_corrections': 'list[str]',
        'form_comments': 'list[str]',
        'assigner': 'str',
        'rater': 'str',
        'group_task_todo_links': 'list[str]',
        'status': 'str',
        'scored_points': 'float',
        'max_points': 'float',
        'last_editor': 'str',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'note': 'str',
        'instructors_to_notify': 'list[str]',
        'equipments': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'task': 'task',
        'form_solutions': 'formSolutions',
        'form_answers': 'formAnswers',
        'form_corrections': 'formCorrections',
        'form_comments': 'formComments',
        'assigner': 'assigner',
        'rater': 'rater',
        'group_task_todo_links': 'groupTaskTodoLinks',
        'status': 'status',
        'scored_points': 'scoredPoints',
        'max_points': 'maxPoints',
        'last_editor': 'lastEditor',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'note': 'note',
        'instructors_to_notify': 'instructorsToNotify',
        'equipments': 'equipments'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, task=None, form_solutions=None, form_answers=None, form_corrections=None, form_comments=None, assigner=None, rater=None, group_task_todo_links=None, status=None, scored_points=None, max_points=None, last_editor=None, start_time=None, end_time=None, note=None, instructors_to_notify=None, equipments=None):  # noqa: E501
        """GroupTaskTodoJsonld - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._task = None
        self._form_solutions = None
        self._form_answers = None
        self._form_corrections = None
        self._form_comments = None
        self._assigner = None
        self._rater = None
        self._group_task_todo_links = None
        self._status = None
        self._scored_points = None
        self._max_points = None
        self._last_editor = None
        self._start_time = None
        self._end_time = None
        self._note = None
        self._instructors_to_notify = None
        self._equipments = None
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
        self.task = task
        if form_solutions is not None:
            self.form_solutions = form_solutions
        if form_answers is not None:
            self.form_answers = form_answers
        if form_corrections is not None:
            self.form_corrections = form_corrections
        if form_comments is not None:
            self.form_comments = form_comments
        if assigner is not None:
            self.assigner = assigner
        if rater is not None:
            self.rater = rater
        if group_task_todo_links is not None:
            self.group_task_todo_links = group_task_todo_links
        if status is not None:
            self.status = status
        if scored_points is not None:
            self.scored_points = scored_points
        if max_points is not None:
            self.max_points = max_points
        if last_editor is not None:
            self.last_editor = last_editor
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if note is not None:
            self.note = note
        if instructors_to_notify is not None:
            self.instructors_to_notify = instructors_to_notify
        if equipments is not None:
            self.equipments = equipments

    @property
    def context(self):
        """Gets the context of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The context of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: OneOfGroupTaskTodoJsonldContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this GroupTaskTodoJsonld.


        :param context: The context of this GroupTaskTodoJsonld.  # noqa: E501
        :type: OneOfGroupTaskTodoJsonldContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The id of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupTaskTodoJsonld.


        :param id: The id of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The type of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GroupTaskTodoJsonld.


        :param type: The type of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The created_at of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GroupTaskTodoJsonld.


        :param created_at: The created_at of this GroupTaskTodoJsonld.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The updated_at of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this GroupTaskTodoJsonld.


        :param updated_at: The updated_at of this GroupTaskTodoJsonld.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The id of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GroupTaskTodoJsonld.


        :param id: The id of this GroupTaskTodoJsonld.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def task(self):
        """Gets the task of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The task of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this GroupTaskTodoJsonld.


        :param task: The task of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """
        if task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task

    @property
    def form_solutions(self):
        """Gets the form_solutions of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The form_solutions of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_solutions

    @form_solutions.setter
    def form_solutions(self, form_solutions):
        """Sets the form_solutions of this GroupTaskTodoJsonld.


        :param form_solutions: The form_solutions of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._form_solutions = form_solutions

    @property
    def form_answers(self):
        """Gets the form_answers of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The form_answers of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_answers

    @form_answers.setter
    def form_answers(self, form_answers):
        """Sets the form_answers of this GroupTaskTodoJsonld.


        :param form_answers: The form_answers of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._form_answers = form_answers

    @property
    def form_corrections(self):
        """Gets the form_corrections of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The form_corrections of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_corrections

    @form_corrections.setter
    def form_corrections(self, form_corrections):
        """Sets the form_corrections of this GroupTaskTodoJsonld.


        :param form_corrections: The form_corrections of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._form_corrections = form_corrections

    @property
    def form_comments(self):
        """Gets the form_comments of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The form_comments of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._form_comments

    @form_comments.setter
    def form_comments(self, form_comments):
        """Sets the form_comments of this GroupTaskTodoJsonld.


        :param form_comments: The form_comments of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._form_comments = form_comments

    @property
    def assigner(self):
        """Gets the assigner of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The assigner of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._assigner

    @assigner.setter
    def assigner(self, assigner):
        """Sets the assigner of this GroupTaskTodoJsonld.


        :param assigner: The assigner of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._assigner = assigner

    @property
    def rater(self):
        """Gets the rater of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The rater of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._rater

    @rater.setter
    def rater(self, rater):
        """Sets the rater of this GroupTaskTodoJsonld.


        :param rater: The rater of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._rater = rater

    @property
    def group_task_todo_links(self):
        """Gets the group_task_todo_links of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The group_task_todo_links of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_task_todo_links

    @group_task_todo_links.setter
    def group_task_todo_links(self, group_task_todo_links):
        """Sets the group_task_todo_links of this GroupTaskTodoJsonld.


        :param group_task_todo_links: The group_task_todo_links of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._group_task_todo_links = group_task_todo_links

    @property
    def status(self):
        """Gets the status of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The status of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GroupTaskTodoJsonld.


        :param status: The status of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def scored_points(self):
        """Gets the scored_points of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The scored_points of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: float
        """
        return self._scored_points

    @scored_points.setter
    def scored_points(self, scored_points):
        """Sets the scored_points of this GroupTaskTodoJsonld.


        :param scored_points: The scored_points of this GroupTaskTodoJsonld.  # noqa: E501
        :type: float
        """

        self._scored_points = scored_points

    @property
    def max_points(self):
        """Gets the max_points of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The max_points of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: float
        """
        return self._max_points

    @max_points.setter
    def max_points(self, max_points):
        """Sets the max_points of this GroupTaskTodoJsonld.


        :param max_points: The max_points of this GroupTaskTodoJsonld.  # noqa: E501
        :type: float
        """

        self._max_points = max_points

    @property
    def last_editor(self):
        """Gets the last_editor of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The last_editor of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this GroupTaskTodoJsonld.


        :param last_editor: The last_editor of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._last_editor = last_editor

    @property
    def start_time(self):
        """Gets the start_time of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The start_time of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this GroupTaskTodoJsonld.


        :param start_time: The start_time of this GroupTaskTodoJsonld.  # noqa: E501
        :type: datetime
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The end_time of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this GroupTaskTodoJsonld.


        :param end_time: The end_time of this GroupTaskTodoJsonld.  # noqa: E501
        :type: datetime
        """

        self._end_time = end_time

    @property
    def note(self):
        """Gets the note of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The note of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this GroupTaskTodoJsonld.


        :param note: The note of this GroupTaskTodoJsonld.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def instructors_to_notify(self):
        """Gets the instructors_to_notify of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The instructors_to_notify of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._instructors_to_notify

    @instructors_to_notify.setter
    def instructors_to_notify(self, instructors_to_notify):
        """Sets the instructors_to_notify of this GroupTaskTodoJsonld.


        :param instructors_to_notify: The instructors_to_notify of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._instructors_to_notify = instructors_to_notify

    @property
    def equipments(self):
        """Gets the equipments of this GroupTaskTodoJsonld.  # noqa: E501


        :return: The equipments of this GroupTaskTodoJsonld.  # noqa: E501
        :rtype: list[str]
        """
        return self._equipments

    @equipments.setter
    def equipments(self, equipments):
        """Sets the equipments of this GroupTaskTodoJsonld.


        :param equipments: The equipments of this GroupTaskTodoJsonld.  # noqa: E501
        :type: list[str]
        """

        self._equipments = equipments

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
        if issubclass(GroupTaskTodoJsonld, dict):
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
        if not isinstance(other, GroupTaskTodoJsonld):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
