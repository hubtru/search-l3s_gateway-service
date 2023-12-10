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

class EquipmentFilesEquipmentFilesItemRead(object):
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
        'equipment': 'str',
        'id': 'int',
        'custom_filename': 'str',
        'file_resource': 'FileResourceEquipmentFilesItemRead'
    }

    attribute_map = {
        'equipment': 'equipment',
        'id': 'id',
        'custom_filename': 'customFilename',
        'file_resource': 'fileResource'
    }

    def __init__(self, equipment=None, id=None, custom_filename=None, file_resource=None):  # noqa: E501
        """EquipmentFilesEquipmentFilesItemRead - a model defined in Swagger"""  # noqa: E501
        self._equipment = None
        self._id = None
        self._custom_filename = None
        self._file_resource = None
        self.discriminator = None
        if equipment is not None:
            self.equipment = equipment
        if id is not None:
            self.id = id
        if custom_filename is not None:
            self.custom_filename = custom_filename
        if file_resource is not None:
            self.file_resource = file_resource

    @property
    def equipment(self):
        """Gets the equipment of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501


        :return: The equipment of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :rtype: str
        """
        return self._equipment

    @equipment.setter
    def equipment(self, equipment):
        """Sets the equipment of this EquipmentFilesEquipmentFilesItemRead.


        :param equipment: The equipment of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :type: str
        """

        self._equipment = equipment

    @property
    def id(self):
        """Gets the id of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501


        :return: The id of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EquipmentFilesEquipmentFilesItemRead.


        :param id: The id of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def custom_filename(self):
        """Gets the custom_filename of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501


        :return: The custom_filename of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :rtype: str
        """
        return self._custom_filename

    @custom_filename.setter
    def custom_filename(self, custom_filename):
        """Sets the custom_filename of this EquipmentFilesEquipmentFilesItemRead.


        :param custom_filename: The custom_filename of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :type: str
        """

        self._custom_filename = custom_filename

    @property
    def file_resource(self):
        """Gets the file_resource of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501


        :return: The file_resource of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :rtype: FileResourceEquipmentFilesItemRead
        """
        return self._file_resource

    @file_resource.setter
    def file_resource(self, file_resource):
        """Sets the file_resource of this EquipmentFilesEquipmentFilesItemRead.


        :param file_resource: The file_resource of this EquipmentFilesEquipmentFilesItemRead.  # noqa: E501
        :type: FileResourceEquipmentFilesItemRead
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
        if issubclass(EquipmentFilesEquipmentFilesItemRead, dict):
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
        if not isinstance(other, EquipmentFilesEquipmentFilesItemRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
