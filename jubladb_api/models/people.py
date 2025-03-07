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

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class People(BaseModel):
    """
    Person attributes
    """ # noqa: E501
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    nickname: Optional[StrictStr] = None
    company_name: Optional[StrictStr] = None
    company: Optional[StrictBool] = None
    email: Optional[StrictStr] = None
    address: Optional[StrictStr] = None
    zip_code: Optional[StrictStr] = None
    town: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    primary_group_id: Optional[StrictInt] = None
    gender: Optional[StrictStr] = None
    birthday: Optional[date] = None
    language: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["first_name", "last_name", "nickname", "company_name", "company", "email", "address", "zip_code", "town", "country", "primary_group_id", "gender", "birthday", "language"]

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
        """Create an instance of People from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "primary_group_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of People from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "nickname": obj.get("nickname"),
            "company_name": obj.get("company_name"),
            "company": obj.get("company"),
            "email": obj.get("email"),
            "address": obj.get("address"),
            "zip_code": obj.get("zip_code"),
            "town": obj.get("town"),
            "country": obj.get("country"),
            "primary_group_id": obj.get("primary_group_id"),
            "gender": obj.get("gender"),
            "birthday": obj.get("birthday"),
            "language": obj.get("language")
        })
        return _obj


