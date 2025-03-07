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


class GroupsExtraAttribute(str, Enum):
    """
    Group extra attributes
    """

    """
    allowed enum values
    """
    LOGO = 'logo'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of GroupsExtraAttribute from a JSON string"""
        return cls(json.loads(json_str))


