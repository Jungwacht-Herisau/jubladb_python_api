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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Groups(BaseModel):
    """
    Group attributes
    """ # noqa: E501
    name: Optional[StrictStr] = None
    short_name: Optional[StrictStr] = None
    display_name: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    layer: Optional[StrictBool] = None
    parent_id: Optional[StrictInt] = None
    layer_group_id: Optional[StrictInt] = None
    type: Optional[StrictStr] = None
    email: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    zip_code: Optional[StrictInt] = None
    town: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    require_person_add_requests: Optional[StrictBool] = None
    self_registration_url: Optional[StrictStr] = None
    archived_at: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    logo: Optional[StrictStr] = Field(default=None, description=" This *extra field* will only be present if requested explicitely with the `extra_fields[groups]` parameter. See [Graphiti Resource Extra fields](https://www.graphiti.dev/guides/concepts/resources#extra-fields) for more information. ")
    __properties: ClassVar[List[str]] = ["name", "short_name", "display_name", "description", "layer", "parent_id", "layer_group_id", "type", "email", "address", "zip_code", "town", "country", "require_person_add_requests", "self_registration_url", "archived_at", "created_at", "updated_at", "deleted_at", "logo"]

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
        """Create an instance of Groups from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "name",
            "short_name",
            "display_name",
            "description",
            "layer",
            "parent_id",
            "layer_group_id",
            "type",
            "email",
            "address",
            "zip_code",
            "town",
            "country",
            "require_person_add_requests",
            "self_registration_url",
            "archived_at",
            "created_at",
            "updated_at",
            "deleted_at",
            "logo",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Groups from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "short_name": obj.get("short_name"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "layer": obj.get("layer"),
            "parent_id": obj.get("parent_id"),
            "layer_group_id": obj.get("layer_group_id"),
            "type": obj.get("type"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "zip_code": obj.get("zip_code"),
            "town": obj.get("town"),
            "country": obj.get("country"),
            "require_person_add_requests": obj.get("require_person_add_requests"),
            "self_registration_url": obj.get("self_registration_url"),
            "archived_at": obj.get("archived_at"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "logo": obj.get("logo")
        })
        return _obj


