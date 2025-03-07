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


class DatesReadableAttribute(str, Enum):
    """
    Date readable attributes
    """

    """
    allowed enum values
    """
    ID = 'id'
    EVENT_ID = 'event_id'
    LABEL = 'label'
    LOCATION = 'location'
    START_AT = 'start_at'
    FINISH_AT = 'finish_at'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of DatesReadableAttribute from a JSON string"""
        return cls(json.loads(json_str))


