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

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from jubladb_api.models.jsonapi_link import JsonapiLink
from jubladb_api.models.roles import Roles
from jubladb_api.models.roles_relationships import RolesRelationships
from typing import Optional, Set
from typing_extensions import Self

class RolesResource(BaseModel):
    """
    RolesResource
    """ # noqa: E501
    id: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    attributes: Optional[Roles] = None
    relationships: Optional[RolesRelationships] = None
    links: Optional[Dict[str, JsonapiLink]] = None
    __properties: ClassVar[List[str]] = ["id", "type", "attributes", "relationships", "links"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['roles']):
            raise ValueError("must be one of enum values ('roles')")
        return value

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
        """Create an instance of RolesResource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of attributes
        if self.attributes:
            _dict['attributes'] = self.attributes.to_dict()
        # override the default output from pydantic by calling `to_dict()` of relationships
        if self.relationships:
            _dict['relationships'] = self.relationships.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each value in links (dict)
        _field_dict = {}
        if self.links:
            for _key_links in self.links:
                if self.links[_key_links]:
                    _field_dict[_key_links] = self.links[_key_links].to_dict()
            _dict['links'] = _field_dict
        # set to None if links (nullable) is None
        # and model_fields_set contains the field
        if self.links is None and "links" in self.model_fields_set:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RolesResource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "attributes": Roles.from_dict(obj["attributes"]) if obj.get("attributes") is not None else None,
            "relationships": RolesRelationships.from_dict(obj["relationships"]) if obj.get("relationships") is not None else None,
            "links": dict(
                (_k, JsonapiLink.from_dict(_v))
                for _k, _v in obj["links"].items()
            )
            if obj.get("links") is not None
            else None
        })
        return _obj


