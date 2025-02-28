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


class Types(str, Enum):
    """
    Types
    """

    """
    allowed enum values
    """
    ADDITIONAL_EMAILS = 'additional_emails'
    COURSES = 'courses'
    DATES = 'dates'
    EVENT_KIND_CATEGORIES = 'event_kind_categories'
    EVENT_KINDS = 'event_kinds'
    EVENTS = 'events'
    GROUPS = 'groups'
    INVOICE_ITEMS = 'invoice_items'
    INVOICES = 'invoices'
    PERSON_MINUS_NAME = 'person-name'
    PEOPLE = 'people'
    PHONE_NUMBERS = 'phone_numbers'
    ROLES = 'roles'
    SOCIAL_ACCOUNTS = 'social_accounts'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Types from a JSON string"""
        return cls(json.loads(json_str))


