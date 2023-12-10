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

class TaskSet(object):
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
        'locale': 'str',
        'id': 'int',
        'title': 'str',
        'tasks': 'list[str]',
        'organization': 'str',
        'translations': 'list[str]',
        'is_default_task_set': 'bool',
        'shared_organizations': 'list[str]',
        'root_id': 'str'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'locale': 'locale',
        'id': 'id',
        'title': 'title',
        'tasks': 'tasks',
        'organization': 'organization',
        'translations': 'translations',
        'is_default_task_set': 'isDefaultTaskSet',
        'shared_organizations': 'sharedOrganizations',
        'root_id': 'rootId'
    }

    def __init__(self, created_at=None, updated_at=None, locale=None, id=None, title=None, tasks=None, organization=None, translations=None, is_default_task_set=None, shared_organizations=None, root_id=None):  # noqa: E501
        """TaskSet - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._locale = None
        self._id = None
        self._title = None
        self._tasks = None
        self._organization = None
        self._translations = None
        self._is_default_task_set = None
        self._shared_organizations = None
        self._root_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if locale is not None:
            self.locale = locale
        if id is not None:
            self.id = id
        self.title = title
        if tasks is not None:
            self.tasks = tasks
        if organization is not None:
            self.organization = organization
        if translations is not None:
            self.translations = translations
        if is_default_task_set is not None:
            self.is_default_task_set = is_default_task_set
        if shared_organizations is not None:
            self.shared_organizations = shared_organizations
        if root_id is not None:
            self.root_id = root_id

    @property
    def created_at(self):
        """Gets the created_at of this TaskSet.  # noqa: E501


        :return: The created_at of this TaskSet.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TaskSet.


        :param created_at: The created_at of this TaskSet.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TaskSet.  # noqa: E501


        :return: The updated_at of this TaskSet.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TaskSet.


        :param updated_at: The updated_at of this TaskSet.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def locale(self):
        """Gets the locale of this TaskSet.  # noqa: E501


        :return: The locale of this TaskSet.  # noqa: E501
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this TaskSet.


        :param locale: The locale of this TaskSet.  # noqa: E501
        :type: str
        """

        self._locale = locale

    @property
    def id(self):
        """Gets the id of this TaskSet.  # noqa: E501


        :return: The id of this TaskSet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaskSet.


        :param id: The id of this TaskSet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this TaskSet.  # noqa: E501


        :return: The title of this TaskSet.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TaskSet.


        :param title: The title of this TaskSet.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def tasks(self):
        """Gets the tasks of this TaskSet.  # noqa: E501


        :return: The tasks of this TaskSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this TaskSet.


        :param tasks: The tasks of this TaskSet.  # noqa: E501
        :type: list[str]
        """

        self._tasks = tasks

    @property
    def organization(self):
        """Gets the organization of this TaskSet.  # noqa: E501


        :return: The organization of this TaskSet.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this TaskSet.


        :param organization: The organization of this TaskSet.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def translations(self):
        """Gets the translations of this TaskSet.  # noqa: E501


        :return: The translations of this TaskSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._translations

    @translations.setter
    def translations(self, translations):
        """Sets the translations of this TaskSet.


        :param translations: The translations of this TaskSet.  # noqa: E501
        :type: list[str]
        """

        self._translations = translations

    @property
    def is_default_task_set(self):
        """Gets the is_default_task_set of this TaskSet.  # noqa: E501


        :return: The is_default_task_set of this TaskSet.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_task_set

    @is_default_task_set.setter
    def is_default_task_set(self, is_default_task_set):
        """Sets the is_default_task_set of this TaskSet.


        :param is_default_task_set: The is_default_task_set of this TaskSet.  # noqa: E501
        :type: bool
        """

        self._is_default_task_set = is_default_task_set

    @property
    def shared_organizations(self):
        """Gets the shared_organizations of this TaskSet.  # noqa: E501


        :return: The shared_organizations of this TaskSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._shared_organizations

    @shared_organizations.setter
    def shared_organizations(self, shared_organizations):
        """Sets the shared_organizations of this TaskSet.


        :param shared_organizations: The shared_organizations of this TaskSet.  # noqa: E501
        :type: list[str]
        """

        self._shared_organizations = shared_organizations

    @property
    def root_id(self):
        """Gets the root_id of this TaskSet.  # noqa: E501


        :return: The root_id of this TaskSet.  # noqa: E501
        :rtype: str
        """
        return self._root_id

    @root_id.setter
    def root_id(self, root_id):
        """Sets the root_id of this TaskSet.


        :param root_id: The root_id of this TaskSet.  # noqa: E501
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
        if issubclass(TaskSet, dict):
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
        if not isinstance(other, TaskSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
