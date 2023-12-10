# coding: utf-8

"""
    Skill Repository

    The API description of the Skill Repository.  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class LearningPathDto(object):
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
        'id': 'str',
        'title': 'str',
        'owner': 'str',
        'description': 'str',
        'lifecycle': 'object',
        'path_goals': 'list[str]',
        'requirements': 'list[str]',
        'recommended_unit_sequence': 'list[str]',
        'target_audience': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'owner': 'owner',
        'description': 'description',
        'lifecycle': 'lifecycle',
        'path_goals': 'pathGoals',
        'requirements': 'requirements',
        'recommended_unit_sequence': 'recommendedUnitSequence',
        'target_audience': 'targetAudience',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, id=None, title=None, owner=None, description=None, lifecycle=None, path_goals=None, requirements=None, recommended_unit_sequence=None, target_audience=None, created_at=None, updated_at=None):  # noqa: E501
        """LearningPathDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._owner = None
        self._description = None
        self._lifecycle = None
        self._path_goals = None
        self._requirements = None
        self._recommended_unit_sequence = None
        self._target_audience = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.id = id
        self.title = title
        self.owner = owner
        if description is not None:
            self.description = description
        self.lifecycle = lifecycle
        self.path_goals = path_goals
        self.requirements = requirements
        self.recommended_unit_sequence = recommended_unit_sequence
        if target_audience is not None:
            self.target_audience = target_audience
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this LearningPathDto.  # noqa: E501


        :return: The id of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LearningPathDto.


        :param id: The id of this LearningPathDto.  # noqa: E501
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def title(self):
        """Gets the title of this LearningPathDto.  # noqa: E501


        :return: The title of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LearningPathDto.


        :param title: The title of this LearningPathDto.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def owner(self):
        """Gets the owner of this LearningPathDto.  # noqa: E501


        :return: The owner of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this LearningPathDto.


        :param owner: The owner of this LearningPathDto.  # noqa: E501
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def description(self):
        """Gets the description of this LearningPathDto.  # noqa: E501


        :return: The description of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LearningPathDto.


        :param description: The description of this LearningPathDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def lifecycle(self):
        """Gets the lifecycle of this LearningPathDto.  # noqa: E501


        :return: The lifecycle of this LearningPathDto.  # noqa: E501
        :rtype: object
        """
        return self._lifecycle

    @lifecycle.setter
    def lifecycle(self, lifecycle):
        """Sets the lifecycle of this LearningPathDto.


        :param lifecycle: The lifecycle of this LearningPathDto.  # noqa: E501
        :type: object
        """
        if lifecycle is None:
            raise ValueError("Invalid value for `lifecycle`, must not be `None`")  # noqa: E501

        self._lifecycle = lifecycle

    @property
    def path_goals(self):
        """Gets the path_goals of this LearningPathDto.  # noqa: E501


        :return: The path_goals of this LearningPathDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._path_goals

    @path_goals.setter
    def path_goals(self, path_goals):
        """Sets the path_goals of this LearningPathDto.


        :param path_goals: The path_goals of this LearningPathDto.  # noqa: E501
        :type: list[str]
        """
        if path_goals is None:
            raise ValueError("Invalid value for `path_goals`, must not be `None`")  # noqa: E501

        self._path_goals = path_goals

    @property
    def requirements(self):
        """Gets the requirements of this LearningPathDto.  # noqa: E501


        :return: The requirements of this LearningPathDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._requirements

    @requirements.setter
    def requirements(self, requirements):
        """Sets the requirements of this LearningPathDto.


        :param requirements: The requirements of this LearningPathDto.  # noqa: E501
        :type: list[str]
        """
        if requirements is None:
            raise ValueError("Invalid value for `requirements`, must not be `None`")  # noqa: E501

        self._requirements = requirements

    @property
    def recommended_unit_sequence(self):
        """Gets the recommended_unit_sequence of this LearningPathDto.  # noqa: E501


        :return: The recommended_unit_sequence of this LearningPathDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._recommended_unit_sequence

    @recommended_unit_sequence.setter
    def recommended_unit_sequence(self, recommended_unit_sequence):
        """Sets the recommended_unit_sequence of this LearningPathDto.


        :param recommended_unit_sequence: The recommended_unit_sequence of this LearningPathDto.  # noqa: E501
        :type: list[str]
        """
        if recommended_unit_sequence is None:
            raise ValueError("Invalid value for `recommended_unit_sequence`, must not be `None`")  # noqa: E501

        self._recommended_unit_sequence = recommended_unit_sequence

    @property
    def target_audience(self):
        """Gets the target_audience of this LearningPathDto.  # noqa: E501


        :return: The target_audience of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._target_audience

    @target_audience.setter
    def target_audience(self, target_audience):
        """Sets the target_audience of this LearningPathDto.


        :param target_audience: The target_audience of this LearningPathDto.  # noqa: E501
        :type: str
        """

        self._target_audience = target_audience

    @property
    def created_at(self):
        """Gets the created_at of this LearningPathDto.  # noqa: E501


        :return: The created_at of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this LearningPathDto.


        :param created_at: The created_at of this LearningPathDto.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this LearningPathDto.  # noqa: E501


        :return: The updated_at of this LearningPathDto.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this LearningPathDto.


        :param updated_at: The updated_at of this LearningPathDto.  # noqa: E501
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(LearningPathDto, dict):
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
        if not isinstance(other, LearningPathDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
