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

class CoursesRelationships(BaseModel):
    """
    CoursesRelationships
    """ # noqa: E501
    contact: Optional[CoursesRelationshipsContact] = None
    kind: Optional[CoursesRelationshipsContact] = None
    dates: Optional[CoursesRelationshipsDates] = None
    leaders: Optional[CoursesRelationshipsDates] = None
    __properties: ClassVar[List[str]] = ["contact", "kind", "dates", "leaders"]

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
        """Create an instance of CoursesRelationships from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of kind
        if self.kind:
            _dict['kind'] = self.kind.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dates
        if self.dates:
            _dict['dates'] = self.dates.to_dict()
        # override the default output from pydantic by calling `to_dict()` of leaders
        if self.leaders:
            _dict['leaders'] = self.leaders.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CoursesRelationships from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contact": CoursesRelationshipsContact.from_dict(obj["contact"]) if obj.get("contact") is not None else None,
            "kind": CoursesRelationshipsContact.from_dict(obj["kind"]) if obj.get("kind") is not None else None,
            "dates": CoursesRelationshipsDates.from_dict(obj["dates"]) if obj.get("dates") is not None else None,
            "leaders": CoursesRelationshipsDates.from_dict(obj["leaders"]) if obj.get("leaders") is not None else None
        })
        return _obj


