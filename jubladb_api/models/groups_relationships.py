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
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from jubladb_api.models.courses_relationships_contact import CoursesRelationshipsContact
from jubladb_api.models.courses_relationships_dates import CoursesRelationshipsDates
from typing import Optional, Set
from typing_extensions import Self

class GroupsRelationships(BaseModel):
    """
    GroupsRelationships
    """ # noqa: E501
    contact: Optional[CoursesRelationshipsContact] = None
    creator: Optional[CoursesRelationshipsContact] = None
    updater: Optional[CoursesRelationshipsContact] = None
    deleter: Optional[CoursesRelationshipsContact] = None
    parent: Optional[CoursesRelationshipsContact] = None
    layer_group: Optional[CoursesRelationshipsContact] = None
    phone_numbers: Optional[CoursesRelationshipsDates] = None
    social_accounts: Optional[CoursesRelationshipsDates] = None
    additional_emails: Optional[CoursesRelationshipsDates] = None
    __properties: ClassVar[List[str]] = ["contact", "creator", "updater", "deleter", "parent", "layer_group", "phone_numbers", "social_accounts", "additional_emails"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GroupsRelationships from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of contact
        if self.contact:
            _dict['contact'] = self.contact.to_dict()
        # override the default output from pydantic by calling `to_dict()` of creator
        if self.creator:
            _dict['creator'] = self.creator.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updater
        if self.updater:
            _dict['updater'] = self.updater.to_dict()
        # override the default output from pydantic by calling `to_dict()` of deleter
        if self.deleter:
            _dict['deleter'] = self.deleter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of layer_group
        if self.layer_group:
            _dict['layer_group'] = self.layer_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of phone_numbers
        if self.phone_numbers:
            _dict['phone_numbers'] = self.phone_numbers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of social_accounts
        if self.social_accounts:
            _dict['social_accounts'] = self.social_accounts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of additional_emails
        if self.additional_emails:
            _dict['additional_emails'] = self.additional_emails.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GroupsRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": CoursesRelationshipsContact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "creator": CoursesRelationshipsContact.from_dict(obj["creator"]) if obj.get("creator") is not None else None,
            "updater": CoursesRelationshipsContact.from_dict(obj["updater"]) if obj.get("updater") is not None else None,
            "deleter": CoursesRelationshipsContact.from_dict(obj["deleter"]) if obj.get("deleter") is not None else None,
            "parent": CoursesRelationshipsContact.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "layer_group": CoursesRelationshipsContact.from_dict(obj["layer_group"]) if obj.get("layer_group") is not None else None,
            "phone_numbers": CoursesRelationshipsDates.from_dict(obj["phone_numbers"]) if obj.get("phone_numbers") is not None else None,
            "social_accounts": CoursesRelationshipsDates.from_dict(obj["social_accounts"]) if obj.get("social_accounts") is not None else None,
            "additional_emails": CoursesRelationshipsDates.from_dict(obj["additional_emails"]) if obj.get("additional_emails") is not None else None
        })
        return _obj


