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

class ExternalContentJsonldExternalContentItemWrite(object):
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
        'context': 'OneOfExternalContentJsonldExternalContentItemWriteContext',
        'id': 'str',
        'type': 'str',
        'price': 'float',
        'external_content_organizations': 'list[str]',
        'projects': 'list[str]',
        'tasks': 'list[str]',
        'forms': 'list[str]',
        'directories': 'list[str]',
        'add_future_tasks_automatically': 'bool',
        'elearnings': 'list[str]',
        'no_mls_contents': 'list[str]',
        'allow_copy': 'bool',
        'links': 'list[str]'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'price': 'price',
        'external_content_organizations': 'externalContentOrganizations',
        'projects': 'projects',
        'tasks': 'tasks',
        'forms': 'forms',
        'directories': 'directories',
        'add_future_tasks_automatically': 'addFutureTasksAutomatically',
        'elearnings': 'elearnings',
        'no_mls_contents': 'noMlsContents',
        'allow_copy': 'allowCopy',
        'links': 'links'
    }

    def __init__(self, context=None, id=None, type=None, price=None, external_content_organizations=None, projects=None, tasks=None, forms=None, directories=None, add_future_tasks_automatically=None, elearnings=None, no_mls_contents=None, allow_copy=None, links=None):  # noqa: E501
        """ExternalContentJsonldExternalContentItemWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._price = None
        self._external_content_organizations = None
        self._projects = None
        self._tasks = None
        self._forms = None
        self._directories = None
        self._add_future_tasks_automatically = None
        self._elearnings = None
        self._no_mls_contents = None
        self._allow_copy = None
        self._links = None
        self.discriminator = None
        if context is not None:
            self.context = context
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if price is not None:
            self.price = price
        if external_content_organizations is not None:
            self.external_content_organizations = external_content_organizations
        if projects is not None:
            self.projects = projects
        if tasks is not None:
            self.tasks = tasks
        if forms is not None:
            self.forms = forms
        if directories is not None:
            self.directories = directories
        if add_future_tasks_automatically is not None:
            self.add_future_tasks_automatically = add_future_tasks_automatically
        if elearnings is not None:
            self.elearnings = elearnings
        if no_mls_contents is not None:
            self.no_mls_contents = no_mls_contents
        if allow_copy is not None:
            self.allow_copy = allow_copy
        if links is not None:
            self.links = links

    @property
    def context(self):
        """Gets the context of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The context of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: OneOfExternalContentJsonldExternalContentItemWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ExternalContentJsonldExternalContentItemWrite.


        :param context: The context of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: OneOfExternalContentJsonldExternalContentItemWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The id of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalContentJsonldExternalContentItemWrite.


        :param id: The id of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The type of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalContentJsonldExternalContentItemWrite.


        :param type: The type of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def price(self):
        """Gets the price of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The price of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: float
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this ExternalContentJsonldExternalContentItemWrite.


        :param price: The price of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: float
        """

        self._price = price

    @property
    def external_content_organizations(self):
        """Gets the external_content_organizations of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The external_content_organizations of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._external_content_organizations

    @external_content_organizations.setter
    def external_content_organizations(self, external_content_organizations):
        """Sets the external_content_organizations of this ExternalContentJsonldExternalContentItemWrite.


        :param external_content_organizations: The external_content_organizations of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._external_content_organizations = external_content_organizations

    @property
    def projects(self):
        """Gets the projects of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The projects of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ExternalContentJsonldExternalContentItemWrite.


        :param projects: The projects of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._projects = projects

    @property
    def tasks(self):
        """Gets the tasks of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The tasks of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._tasks

    @tasks.setter
    def tasks(self, tasks):
        """Sets the tasks of this ExternalContentJsonldExternalContentItemWrite.


        :param tasks: The tasks of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._tasks = tasks

    @property
    def forms(self):
        """Gets the forms of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The forms of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._forms

    @forms.setter
    def forms(self, forms):
        """Sets the forms of this ExternalContentJsonldExternalContentItemWrite.


        :param forms: The forms of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._forms = forms

    @property
    def directories(self):
        """Gets the directories of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The directories of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._directories

    @directories.setter
    def directories(self, directories):
        """Sets the directories of this ExternalContentJsonldExternalContentItemWrite.


        :param directories: The directories of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._directories = directories

    @property
    def add_future_tasks_automatically(self):
        """Gets the add_future_tasks_automatically of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The add_future_tasks_automatically of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._add_future_tasks_automatically

    @add_future_tasks_automatically.setter
    def add_future_tasks_automatically(self, add_future_tasks_automatically):
        """Sets the add_future_tasks_automatically of this ExternalContentJsonldExternalContentItemWrite.


        :param add_future_tasks_automatically: The add_future_tasks_automatically of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: bool
        """

        self._add_future_tasks_automatically = add_future_tasks_automatically

    @property
    def elearnings(self):
        """Gets the elearnings of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The elearnings of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._elearnings

    @elearnings.setter
    def elearnings(self, elearnings):
        """Sets the elearnings of this ExternalContentJsonldExternalContentItemWrite.


        :param elearnings: The elearnings of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._elearnings = elearnings

    @property
    def no_mls_contents(self):
        """Gets the no_mls_contents of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The no_mls_contents of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._no_mls_contents

    @no_mls_contents.setter
    def no_mls_contents(self, no_mls_contents):
        """Sets the no_mls_contents of this ExternalContentJsonldExternalContentItemWrite.


        :param no_mls_contents: The no_mls_contents of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._no_mls_contents = no_mls_contents

    @property
    def allow_copy(self):
        """Gets the allow_copy of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The allow_copy of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: bool
        """
        return self._allow_copy

    @allow_copy.setter
    def allow_copy(self, allow_copy):
        """Sets the allow_copy of this ExternalContentJsonldExternalContentItemWrite.


        :param allow_copy: The allow_copy of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: bool
        """

        self._allow_copy = allow_copy

    @property
    def links(self):
        """Gets the links of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501


        :return: The links of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this ExternalContentJsonldExternalContentItemWrite.


        :param links: The links of this ExternalContentJsonldExternalContentItemWrite.  # noqa: E501
        :type: list[str]
        """

        self._links = links

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
        if issubclass(ExternalContentJsonldExternalContentItemWrite, dict):
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
        if not isinstance(other, ExternalContentJsonldExternalContentItemWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
