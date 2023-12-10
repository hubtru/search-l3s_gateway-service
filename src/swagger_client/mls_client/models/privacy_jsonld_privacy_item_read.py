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

class PrivacyJsonldPrivacyItemRead(object):
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
        'context': 'OneOfPrivacyJsonldPrivacyItemReadContext',
        'id': 'str',
        'type': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'excerpt': 'str',
        'text': 'str',
        'active': 'bool',
        'version': 'str',
        'organization': 'str',
        'privacy_pdf': 'AnyOfPrivacyJsonldPrivacyItemReadPrivacyPdf'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'excerpt': 'excerpt',
        'text': 'text',
        'active': 'active',
        'version': 'version',
        'organization': 'organization',
        'privacy_pdf': 'privacyPDF'
    }

    def __init__(self, context=None, id=None, type=None, created_at=None, updated_at=None, id=None, excerpt=None, text=None, active=None, version=None, organization=None, privacy_pdf=None):  # noqa: E501
        """PrivacyJsonldPrivacyItemRead - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._excerpt = None
        self._text = None
        self._active = None
        self._version = None
        self._organization = None
        self._privacy_pdf = None
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
        if excerpt is not None:
            self.excerpt = excerpt
        if text is not None:
            self.text = text
        if active is not None:
            self.active = active
        if version is not None:
            self.version = version
        if organization is not None:
            self.organization = organization
        if privacy_pdf is not None:
            self.privacy_pdf = privacy_pdf

    @property
    def context(self):
        """Gets the context of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The context of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: OneOfPrivacyJsonldPrivacyItemReadContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this PrivacyJsonldPrivacyItemRead.


        :param context: The context of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: OneOfPrivacyJsonldPrivacyItemReadContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivacyJsonldPrivacyItemRead.


        :param id: The id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The type of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PrivacyJsonldPrivacyItemRead.


        :param type: The type of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def created_at(self):
        """Gets the created_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The created_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this PrivacyJsonldPrivacyItemRead.


        :param created_at: The created_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The updated_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this PrivacyJsonldPrivacyItemRead.


        :param updated_at: The updated_at of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivacyJsonldPrivacyItemRead.


        :param id: The id of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def excerpt(self):
        """Gets the excerpt of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The excerpt of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._excerpt

    @excerpt.setter
    def excerpt(self, excerpt):
        """Sets the excerpt of this PrivacyJsonldPrivacyItemRead.


        :param excerpt: The excerpt of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._excerpt = excerpt

    @property
    def text(self):
        """Gets the text of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The text of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this PrivacyJsonldPrivacyItemRead.


        :param text: The text of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def active(self):
        """Gets the active of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The active of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this PrivacyJsonldPrivacyItemRead.


        :param active: The active of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def version(self):
        """Gets the version of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The version of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PrivacyJsonldPrivacyItemRead.


        :param version: The version of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def organization(self):
        """Gets the organization of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The organization of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this PrivacyJsonldPrivacyItemRead.


        :param organization: The organization of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def privacy_pdf(self):
        """Gets the privacy_pdf of this PrivacyJsonldPrivacyItemRead.  # noqa: E501


        :return: The privacy_pdf of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :rtype: AnyOfPrivacyJsonldPrivacyItemReadPrivacyPdf
        """
        return self._privacy_pdf

    @privacy_pdf.setter
    def privacy_pdf(self, privacy_pdf):
        """Sets the privacy_pdf of this PrivacyJsonldPrivacyItemRead.


        :param privacy_pdf: The privacy_pdf of this PrivacyJsonldPrivacyItemRead.  # noqa: E501
        :type: AnyOfPrivacyJsonldPrivacyItemReadPrivacyPdf
        """

        self._privacy_pdf = privacy_pdf

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
        if issubclass(PrivacyJsonldPrivacyItemRead, dict):
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
        if not isinstance(other, PrivacyJsonldPrivacyItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
