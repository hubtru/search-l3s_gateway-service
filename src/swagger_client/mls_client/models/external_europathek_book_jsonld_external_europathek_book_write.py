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

class ExternalEuropathekBookJsonldExternalEuropathekBookWrite(object):
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
        'context': 'OneOfExternalEuropathekBookJsonldExternalEuropathekBookWriteContext',
        'id': 'str',
        'type': 'str',
        'id': 'int',
        'title': 'str',
        'product': 'str',
        'edition': 'str',
        'licenses': 'str',
        'code': 'str',
        'internal': 'str',
        'duration': 'str',
        'europa': 'str',
        'organization_settings': 'list[str]',
        'supplier': 'str',
        'type': 'str'
    }

    attribute_map = {
        'context': '@context',
        'id': '@id',
        'type': '@type',
        'id': 'id',
        'title': 'title',
        'product': 'product',
        'edition': 'edition',
        'licenses': 'licenses',
        'code': 'code',
        'internal': 'internal',
        'duration': 'duration',
        'europa': 'europa',
        'organization_settings': 'organizationSettings',
        'supplier': 'supplier',
        'type': 'type'
    }

    def __init__(self, context=None, id=None, type=None, id=None, title=None, product=None, edition=None, licenses=None, code=None, internal=None, duration=None, europa=None, organization_settings=None, supplier=None, type='EUROPATHEK'):  # noqa: E501
        """ExternalEuropathekBookJsonldExternalEuropathekBookWrite - a model defined in Swagger"""  # noqa: E501
        self._context = None
        self._id = None
        self._type = None
        self._id = None
        self._title = None
        self._product = None
        self._edition = None
        self._licenses = None
        self._code = None
        self._internal = None
        self._duration = None
        self._europa = None
        self._organization_settings = None
        self._supplier = None
        self._type = None
        self.discriminator = None
        if context is not None:
            self.context = context
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
        if licenses is not None:
            self.licenses = licenses
        if code is not None:
            self.code = code
        if internal is not None:
            self.internal = internal
        if duration is not None:
            self.duration = duration
        if europa is not None:
            self.europa = europa
        if organization_settings is not None:
            self.organization_settings = organization_settings
        if supplier is not None:
            self.supplier = supplier
        if type is not None:
            self.type = type

    @property
    def context(self):
        """Gets the context of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The context of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: OneOfExternalEuropathekBookJsonldExternalEuropathekBookWriteContext
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param context: The context of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: OneOfExternalEuropathekBookJsonldExternalEuropathekBookWriteContext
        """

        self._context = context

    @property
    def id(self):
        """Gets the id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param id: The id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param type: The type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param id: The id of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The title of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param title: The title of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def product(self):
        """Gets the product of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The product of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param product: The product of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._product = product

    @property
    def edition(self):
        """Gets the edition of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The edition of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._edition

    @edition.setter
    def edition(self, edition):
        """Sets the edition of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param edition: The edition of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._edition = edition

    @property
    def licenses(self):
        """Gets the licenses of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The licenses of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._licenses

    @licenses.setter
    def licenses(self, licenses):
        """Sets the licenses of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param licenses: The licenses of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._licenses = licenses

    @property
    def code(self):
        """Gets the code of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The code of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param code: The code of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def internal(self):
        """Gets the internal of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The internal of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._internal

    @internal.setter
    def internal(self, internal):
        """Sets the internal of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param internal: The internal of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._internal = internal

    @property
    def duration(self):
        """Gets the duration of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The duration of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param duration: The duration of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def europa(self):
        """Gets the europa of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The europa of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._europa

    @europa.setter
    def europa(self, europa):
        """Sets the europa of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param europa: The europa of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._europa = europa

    @property
    def organization_settings(self):
        """Gets the organization_settings of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The organization_settings of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: list[str]
        """
        return self._organization_settings

    @organization_settings.setter
    def organization_settings(self, organization_settings):
        """Sets the organization_settings of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param organization_settings: The organization_settings of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: list[str]
        """

        self._organization_settings = organization_settings

    @property
    def supplier(self):
        """Gets the supplier of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The supplier of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param supplier: The supplier of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._supplier = supplier

    @property
    def type(self):
        """Gets the type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501


        :return: The type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.


        :param type: The type of this ExternalEuropathekBookJsonldExternalEuropathekBookWrite.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ExternalEuropathekBookJsonldExternalEuropathekBookWrite, dict):
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
        if not isinstance(other, ExternalEuropathekBookJsonldExternalEuropathekBookWrite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
