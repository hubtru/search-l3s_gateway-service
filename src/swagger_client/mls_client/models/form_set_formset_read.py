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

class FormSetFormsetRead(object):
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
        'id': 'int',
        'title': 'str',
        'forms': 'list[str]',
        'organization': 'str',
        'is_default_form_set': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'forms': 'forms',
        'organization': 'organization',
        'is_default_form_set': 'isDefaultFormSet'
    }

    def __init__(self, id=None, title=None, forms=None, organization=None, is_default_form_set=None):  # noqa: E501
        """FormSetFormsetRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._title = None
        self._forms = None
        self._organization = None
        self._is_default_form_set = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if forms is not None:
            self.forms = forms
        if organization is not None:
            self.organization = organization
        if is_default_form_set is not None:
            self.is_default_form_set = is_default_form_set

    @property
    def id(self):
        """Gets the id of this FormSetFormsetRead.  # noqa: E501


        :return: The id of this FormSetFormsetRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FormSetFormsetRead.


        :param id: The id of this FormSetFormsetRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this FormSetFormsetRead.  # noqa: E501


        :return: The title of this FormSetFormsetRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FormSetFormsetRead.


        :param title: The title of this FormSetFormsetRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def forms(self):
        """Gets the forms of this FormSetFormsetRead.  # noqa: E501


        :return: The forms of this FormSetFormsetRead.  # noqa: E501
        :rtype: list[str]
        """
        return self._forms

    @forms.setter
    def forms(self, forms):
        """Sets the forms of this FormSetFormsetRead.


        :param forms: The forms of this FormSetFormsetRead.  # noqa: E501
        :type: list[str]
        """

        self._forms = forms

    @property
    def organization(self):
        """Gets the organization of this FormSetFormsetRead.  # noqa: E501


        :return: The organization of this FormSetFormsetRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this FormSetFormsetRead.


        :param organization: The organization of this FormSetFormsetRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def is_default_form_set(self):
        """Gets the is_default_form_set of this FormSetFormsetRead.  # noqa: E501


        :return: The is_default_form_set of this FormSetFormsetRead.  # noqa: E501
        :rtype: bool
        """
        return self._is_default_form_set

    @is_default_form_set.setter
    def is_default_form_set(self, is_default_form_set):
        """Sets the is_default_form_set of this FormSetFormsetRead.


        :param is_default_form_set: The is_default_form_set of this FormSetFormsetRead.  # noqa: E501
        :type: bool
        """

        self._is_default_form_set = is_default_form_set

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
        if issubclass(FormSetFormsetRead, dict):
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
        if not isinstance(other, FormSetFormsetRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
