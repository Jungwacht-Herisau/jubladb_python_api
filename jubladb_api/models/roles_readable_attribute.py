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


class RolesReadableAttribute(str, Enum):
    """
    Role readable attributes
    """

    """
    allowed enum values
    """
    ID = 'id'
    CREATED_AT = 'created_at'
    UPDATED_AT = 'updated_at'
    START_ON = 'start_on'
    END_ON = 'end_on'
    PERSON_ID = 'person_id'
    GROUP_ID = 'group_id'
    TYPE = 'type'
    LABEL = 'label'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RolesReadableAttribute from a JSON string"""
        return cls(json.loads(json_str))


