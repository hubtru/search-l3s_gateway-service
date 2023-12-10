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

class BackgroundFile(object):
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
        'url': 'str',
        'organization': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'id': 'int',
        'custom_filename': 'str',
        'file_resource': 'str'
    }

    attribute_map = {
        'url': 'url',
        'organization': 'organization',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'custom_filename': 'customFilename',
        'file_resource': 'fileResource'
    }

    def __init__(self, url=None, organization=None, created_at=None, updated_at=None, id=None, custom_filename=None, file_resource=None):  # noqa: E501
        """BackgroundFile - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._organization = None
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._custom_filename = None
        self._file_resource = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if organization is not None:
            self.organization = organization
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        if custom_filename is not None:
            self.custom_filename = custom_filename
        if file_resource is not None:
            self.file_resource = file_resource

    @property
    def url(self):
        """Gets the url of this BackgroundFile.  # noqa: E501


        :return: The url of this BackgroundFile.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BackgroundFile.


        :param url: The url of this BackgroundFile.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def organization(self):
        """Gets the organization of this BackgroundFile.  # noqa: E501


        :return: The organization of this BackgroundFile.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this BackgroundFile.


        :param organization: The organization of this BackgroundFile.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def created_at(self):
        """Gets the created_at of this BackgroundFile.  # noqa: E501


        :return: The created_at of this BackgroundFile.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BackgroundFile.


        :param created_at: The created_at of this BackgroundFile.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this BackgroundFile.  # noqa: E501


        :return: The updated_at of this BackgroundFile.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BackgroundFile.


        :param updated_at: The updated_at of this BackgroundFile.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this BackgroundFile.  # noqa: E501


        :return: The id of this BackgroundFile.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackgroundFile.


        :param id: The id of this BackgroundFile.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def custom_filename(self):
        """Gets the custom_filename of this BackgroundFile.  # noqa: E501


        :return: The custom_filename of this BackgroundFile.  # noqa: E501
        :rtype: str
        """
        return self._custom_filename

    @custom_filename.setter
    def custom_filename(self, custom_filename):
        """Sets the custom_filename of this BackgroundFile.


        :param custom_filename: The custom_filename of this BackgroundFile.  # noqa: E501
        :type: str
        """

        self._custom_filename = custom_filename

    @property
    def file_resource(self):
        """Gets the file_resource of this BackgroundFile.  # noqa: E501


        :return: The file_resource of this BackgroundFile.  # noqa: E501
        :rtype: str
        """
        return self._file_resource

    @file_resource.setter
    def file_resource(self, file_resource):
        """Sets the file_resource of this BackgroundFile.


        :param file_resource: The file_resource of this BackgroundFile.  # noqa: E501
        :type: str
        """

        self._file_resource = file_resource

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
        if issubclass(BackgroundFile, dict):
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
        if not isinstance(other, BackgroundFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
