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

class EquipmentMaintenanceEquipmentRead(object):
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
        'status': 'str',
        'static_interval': 'datetime',
        'dynamic_interval': 'datetime'
    }

    attribute_map = {
        'status': 'status',
        'static_interval': 'staticInterval',
        'dynamic_interval': 'dynamicInterval'
    }

    def __init__(self, status=None, static_interval=None, dynamic_interval=None):  # noqa: E501
        """EquipmentMaintenanceEquipmentRead - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._static_interval = None
        self._dynamic_interval = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if static_interval is not None:
            self.static_interval = static_interval
        if dynamic_interval is not None:
            self.dynamic_interval = dynamic_interval

    @property
    def status(self):
        """Gets the status of this EquipmentMaintenanceEquipmentRead.  # noqa: E501


        :return: The status of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EquipmentMaintenanceEquipmentRead.


        :param status: The status of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def static_interval(self):
        """Gets the static_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501


        :return: The static_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :rtype: datetime
        """
        return self._static_interval

    @static_interval.setter
    def static_interval(self, static_interval):
        """Sets the static_interval of this EquipmentMaintenanceEquipmentRead.


        :param static_interval: The static_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :type: datetime
        """

        self._static_interval = static_interval

    @property
    def dynamic_interval(self):
        """Gets the dynamic_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501


        :return: The dynamic_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :rtype: datetime
        """
        return self._dynamic_interval

    @dynamic_interval.setter
    def dynamic_interval(self, dynamic_interval):
        """Sets the dynamic_interval of this EquipmentMaintenanceEquipmentRead.


        :param dynamic_interval: The dynamic_interval of this EquipmentMaintenanceEquipmentRead.  # noqa: E501
        :type: datetime
        """

        self._dynamic_interval = dynamic_interval

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
        if issubclass(EquipmentMaintenanceEquipmentRead, dict):
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
        if not isinstance(other, EquipmentMaintenanceEquipmentRead):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
