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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from jubladb_api.models.additional_emails_single_links import AdditionalEmailsSingleLinks
from jubladb_api.models.jsonapi_jsonapi import JsonapiJsonapi
from jubladb_api.models.jsonapi_resource import JsonapiResource
from jubladb_api.models.social_accounts_resource import SocialAccountsResource
from typing import Optional, Set
from typing_extensions import Self

class SocialAccountsCollection(BaseModel):
    """
    SocialAccountsCollection
    """ # noqa: E501
    data: Optional[List[SocialAccountsResource]] = None
    included: Optional[List[JsonapiResource]] = Field(default=None, description="To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \"compound documents\".")
    meta: Optional[Dict[str, Any]] = Field(default=None, description="Non-standard meta-information that can not be represented as an attribute or relationship.")
    links: Optional[AdditionalEmailsSingleLinks] = None
    jsonapi: Optional[JsonapiJsonapi] = None
    __properties: ClassVar[List[str]] = ["data", "included", "meta", "links", "jsonapi"]

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
        """Create an instance of SocialAccountsCollection from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in data (list)
        _items = []
        if self.data:
            for _item_data in self.data:
                if _item_data:
                    _items.append(_item_data.to_dict())
            _dict['data'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in included (list)
        _items = []
        if self.included:
            for _item_included in self.included:
                if _item_included:
                    _items.append(_item_included.to_dict())
            _dict['included'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of jsonapi
        if self.jsonapi:
            _dict['jsonapi'] = self.jsonapi.to_dict()
        # set to None if meta (nullable) is None
        # and model_fields_set contains the field
        if self.meta is None and "meta" in self.model_fields_set:
            _dict['meta'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SocialAccountsCollection from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": [SocialAccountsResource.from_dict(_item) for _item in obj["data"]] if obj.get("data") is not None else None,
            "included": [JsonapiResource.from_dict(_item) for _item in obj["included"]] if obj.get("included") is not None else None,
            "meta": obj.get("meta"),
            "links": AdditionalEmailsSingleLinks.from_dict(obj["links"]) if obj.get("links") is not None else None,
            "jsonapi": JsonapiJsonapi.from_dict(obj["jsonapi"]) if obj.get("jsonapi") is not None else None
        })
        return _obj


