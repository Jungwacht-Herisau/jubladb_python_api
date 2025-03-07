# coding: utf-8

"""
    Hitobito JSON:API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: oss@basilbader.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class PersonNameReadableAttribute(str, Enum):
    """
    Name readable attributes
    """

    """
    allowed enum values
    """
    ID = 'id'
    FIRST_NAME = 'first_name'
    LAST_NAME = 'last_name'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of PersonNameReadableAttribute from a JSON string"""
        return cls(json.loads(json_str))


