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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Courses(BaseModel):
    """
    Course attributes
    """ # noqa: E501
    group_ids: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    kind_id: Optional[StrictInt] = None
    name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    application_conditions: Optional[StrictStr] = None
    motto: Optional[StrictStr] = None
    cost: Optional[StrictStr] = None
    location: Optional[StrictStr] = None
    application_opening_at: Optional[date] = None
    application_closing_at: Optional[date] = None
    application_contact_id: Optional[StrictInt] = None
    external_application_link: Optional[StrictStr] = None
    maximum_participants: Optional[StrictInt] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    state: Optional[StrictStr] = None
    training_days: Optional[Union[StrictFloat, StrictInt]] = None
    applicant_count: Optional[StrictInt] = None
    participant_count: Optional[StrictInt] = None
    minimum_participants: Optional[StrictInt] = None
    number: Optional[StrictStr] = None
    teamer_count: Optional[StrictInt] = None
    __properties: ClassVar[List[str]] = ["group_ids", "type", "kind_id", "name", "description", "application_conditions", "motto", "cost", "location", "application_opening_at", "application_closing_at", "application_contact_id", "external_application_link", "maximum_participants", "created_at", "updated_at", "state", "training_days", "applicant_count", "participant_count", "minimum_participants", "number", "teamer_count"]

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
        """Create an instance of Courses from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "group_ids",
            "type",
            "kind_id",
            "name",
            "description",
            "application_conditions",
            "motto",
            "cost",
            "location",
            "application_opening_at",
            "application_closing_at",
            "application_contact_id",
            "external_application_link",
            "maximum_participants",
            "created_at",
            "updated_at",
            "state",
            "training_days",
            "applicant_count",
            "participant_count",
            "minimum_participants",
            "number",
            "teamer_count",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Courses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "group_ids": obj.get("group_ids"),
            "type": obj.get("type"),
            "kind_id": obj.get("kind_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "application_conditions": obj.get("application_conditions"),
            "motto": obj.get("motto"),
            "cost": obj.get("cost"),
            "location": obj.get("location"),
            "application_opening_at": obj.get("application_opening_at"),
            "application_closing_at": obj.get("application_closing_at"),
            "application_contact_id": obj.get("application_contact_id"),
            "external_application_link": obj.get("external_application_link"),
            "maximum_participants": obj.get("maximum_participants"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "state": obj.get("state"),
            "training_days": obj.get("training_days"),
            "applicant_count": obj.get("applicant_count"),
            "participant_count": obj.get("participant_count"),
            "minimum_participants": obj.get("minimum_participants"),
            "number": obj.get("number"),
            "teamer_count": obj.get("teamer_count")
        })
        return _obj


