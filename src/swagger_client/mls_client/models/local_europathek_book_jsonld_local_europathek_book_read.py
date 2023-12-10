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

class LocalEuropathekBookJsonldLocalEuropathekBookRead(object):
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
        'type': 'str',
        'id': 'int',
        'title': 'str',
        'product': 'str',
        'edition': 'str',
        'year_of_publication': 'int',
        'page_offset': 'int'
    }

    attribute_map = {
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'title': 'title',
        'product': 'product',
        'edition': 'edition',
        'year_of_publication': 'yearOfPublication',
        'page_offset': 'pageOffset'
    }

    def __init__(self, id=None, type=None, id=None, title=None, product=None, edition=None, year_of_publication=None, page_offset=None):  # noqa: E501
        """LocalEuropathekBookJsonldLocalEuropathekBookRead - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._type = None
        self._id = None
        self._title = None
        self._product = None
        self._edition = None
        self._year_of_publication = None
        self._page_offset = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if product is not None:
            self.product = product
        if edition is not None:
            self.edition = edition
        if year_of_publication is not None:
            self.year_of_publication = year_of_publication
        if page_offset is not None:
            self.page_offset = page_offset

    @property
    def id(self):
        """Gets the id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param id: The id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The type of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param type: The type of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param id: The id of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The title of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param title: The title of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def product(self):
        """Gets the product of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The product of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param product: The product of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def edition(self):
        """Gets the edition of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The edition of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param edition: The edition of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def year_of_publication(self):
        """Gets the year_of_publication of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The year_of_publication of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: int
        """
        return self._year_of_publication

    @year_of_publication.setter
    def year_of_publication(self, year_of_publication):
        """Sets the year_of_publication of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param year_of_publication: The year_of_publication of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: int
        """

        self._year_of_publication = year_of_publication

    @property
    def page_offset(self):
        """Gets the page_offset of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501


        :return: The page_offset of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :rtype: int
        """
        return self._page_offset

    @page_offset.setter
    def page_offset(self, page_offset):
        """Sets the page_offset of this LocalEuropathekBookJsonldLocalEuropathekBookRead.


        :param page_offset: The page_offset of this LocalEuropathekBookJsonldLocalEuropathekBookRead.  # noqa: E501
        :type: int
        """

        self._page_offset = page_offset

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
        if issubclass(LocalEuropathekBookJsonldLocalEuropathekBookRead, dict):
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
        if not isinstance(other, LocalEuropathekBookJsonldLocalEuropathekBookRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
