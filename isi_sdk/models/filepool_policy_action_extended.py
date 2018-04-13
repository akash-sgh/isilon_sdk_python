# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems
import re


class FilepoolPolicyActionExtended(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        FilepoolPolicyActionExtended - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'action_param': 'str',
            'action_type': 'str'
        }

        self.attribute_map = {
            'action_param': 'action_param',
            'action_type': 'action_type'
        }

        self._action_param = None
        self._action_type = None

    @property
    def action_param(self):
        """
        Gets the action_param of this FilepoolPolicyActionExtended.
        Varies according to action_type

        :return: The action_param of this FilepoolPolicyActionExtended.
        :rtype: str
        """
        return self._action_param

    @action_param.setter
    def action_param(self, action_param):
        """
        Sets the action_param of this FilepoolPolicyActionExtended.
        Varies according to action_type

        :param action_param: The action_param of this FilepoolPolicyActionExtended.
        :type: str
        """
        
        self._action_param = action_param

    @property
    def action_type(self):
        """
        Gets the action_type of this FilepoolPolicyActionExtended.


        :return: The action_type of this FilepoolPolicyActionExtended.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """
        Sets the action_type of this FilepoolPolicyActionExtended.


        :param action_type: The action_type of this FilepoolPolicyActionExtended.
        :type: str
        """
        allowed_values = ["set_requested_protection", "set_data_access_pattern", "enable_coalescer", "apply_data_storage_policy", "apply_snapshot_storage_policy", "set_cloudpool_policy"]
        if action_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_type`, must be one of {0}"
                .format(allowed_values)
            )

        self._action_type = action_type

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
