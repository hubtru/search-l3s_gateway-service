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

class Supplier(object):
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
        'id': 'int',
        'name': 'str',
        'address': 'str',
        'phone': 'str',
        'description': 'str',
        'contact_person_supplier': 'str',
        'contact_person_mls': 'str',
        'website': 'str',
        'organization': 'str',
        'logo': 'str',
        'header': 'str',
        'books': 'list[str]'
    }

    attribute_map = {
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'id': 'id',
        'name': 'name',
        'address': 'address',
        'phone': 'phone',
        'description': 'description',
        'contact_person_supplier': 'contactPersonSupplier',
        'contact_person_mls': 'contactPersonMLS',
        'website': 'website',
        'organization': 'organization',
        'logo': 'logo',
        'header': 'header',
        'books': 'books'
    }

    def __init__(self, created_at=None, updated_at=None, id=None, name=None, address=None, phone=None, description=None, contact_person_supplier=None, contact_person_mls=None, website=None, organization=None, logo=None, header=None, books=None):  # noqa: E501
        """Supplier - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._updated_at = None
        self._id = None
        self._name = None
        self._address = None
        self._phone = None
        self._description = None
        self._contact_person_supplier = None
        self._contact_person_mls = None
        self._website = None
        self._organization = None
        self._logo = None
        self._header = None
        self._books = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if id is not None:
            self.id = id
        self.name = name
        self.address = address
        self.phone = phone
        if description is not None:
            self.description = description
        if contact_person_supplier is not None:
            self.contact_person_supplier = contact_person_supplier
        if contact_person_mls is not None:
            self.contact_person_mls = contact_person_mls
        if website is not None:
            self.website = website
        if organization is not None:
            self.organization = organization
        if logo is not None:
            self.logo = logo
        if header is not None:
            self.header = header
        if books is not None:
            self.books = books

    @property
    def created_at(self):
        """Gets the created_at of this Supplier.  # noqa: E501


        :return: The created_at of this Supplier.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Supplier.


        :param created_at: The created_at of this Supplier.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Supplier.  # noqa: E501


        :return: The updated_at of this Supplier.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Supplier.


        :param updated_at: The updated_at of this Supplier.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Supplier.  # noqa: E501


        :return: The id of this Supplier.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Supplier.


        :param id: The id of this Supplier.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Supplier.  # noqa: E501


        :return: The name of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Supplier.


        :param name: The name of this Supplier.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def address(self):
        """Gets the address of this Supplier.  # noqa: E501


        :return: The address of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Supplier.


        :param address: The address of this Supplier.  # noqa: E501
        :type: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def phone(self):
        """Gets the phone of this Supplier.  # noqa: E501


        :return: The phone of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Supplier.


        :param phone: The phone of this Supplier.  # noqa: E501
        :type: str
        """
        if phone is None:
            raise ValueError("Invalid value for `phone`, must not be `None`")  # noqa: E501

        self._phone = phone

    @property
    def description(self):
        """Gets the description of this Supplier.  # noqa: E501


        :return: The description of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Supplier.


        :param description: The description of this Supplier.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def contact_person_supplier(self):
        """Gets the contact_person_supplier of this Supplier.  # noqa: E501


        :return: The contact_person_supplier of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._contact_person_supplier

    @contact_person_supplier.setter
    def contact_person_supplier(self, contact_person_supplier):
        """Sets the contact_person_supplier of this Supplier.


        :param contact_person_supplier: The contact_person_supplier of this Supplier.  # noqa: E501
        :type: str
        """

        self._contact_person_supplier = contact_person_supplier

    @property
    def contact_person_mls(self):
        """Gets the contact_person_mls of this Supplier.  # noqa: E501


        :return: The contact_person_mls of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._contact_person_mls

    @contact_person_mls.setter
    def contact_person_mls(self, contact_person_mls):
        """Sets the contact_person_mls of this Supplier.


        :param contact_person_mls: The contact_person_mls of this Supplier.  # noqa: E501
        :type: str
        """

        self._contact_person_mls = contact_person_mls

    @property
    def website(self):
        """Gets the website of this Supplier.  # noqa: E501


        :return: The website of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Supplier.


        :param website: The website of this Supplier.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def organization(self):
        """Gets the organization of this Supplier.  # noqa: E501


        :return: The organization of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Supplier.


        :param organization: The organization of this Supplier.  # noqa: E501
        :type: str
        """

        self._organization = organization

    @property
    def logo(self):
        """Gets the logo of this Supplier.  # noqa: E501


        :return: The logo of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._logo

    @logo.setter
    def logo(self, logo):
        """Sets the logo of this Supplier.


        :param logo: The logo of this Supplier.  # noqa: E501
        :type: str
        """

        self._logo = logo

    @property
    def header(self):
        """Gets the header of this Supplier.  # noqa: E501


        :return: The header of this Supplier.  # noqa: E501
        :rtype: str
        """
        return self._header

    @header.setter
    def header(self, header):
        """Sets the header of this Supplier.


        :param header: The header of this Supplier.  # noqa: E501
        :type: str
        """

        self._header = header

    @property
    def books(self):
        """Gets the books of this Supplier.  # noqa: E501


        :return: The books of this Supplier.  # noqa: E501
        :rtype: list[str]
        """
        return self._books

    @books.setter
    def books(self, books):
        """Sets the books of this Supplier.


        :param books: The books of this Supplier.  # noqa: E501
        :type: list[str]
        """

        self._books = books

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
        if issubclass(Supplier, dict):
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
        if not isinstance(other, Supplier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
