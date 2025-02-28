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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from jubladb_api.models.additional_emails_resource import AdditionalEmailsResource
from jubladb_api.models.courses_resource import CoursesResource
from jubladb_api.models.dates_resource import DatesResource
from jubladb_api.models.event_kind_categories_resource import EventKindCategoriesResource
from jubladb_api.models.event_kinds_resource import EventKindsResource
from jubladb_api.models.events_resource import EventsResource
from jubladb_api.models.groups_resource import GroupsResource
from jubladb_api.models.invoice_items_resource import InvoiceItemsResource
from jubladb_api.models.invoices_resource import InvoicesResource
from jubladb_api.models.people_resource import PeopleResource
from jubladb_api.models.person_name_resource import PersonNameResource
from jubladb_api.models.phone_numbers_resource import PhoneNumbersResource
from jubladb_api.models.roles_resource import RolesResource
from jubladb_api.models.social_accounts_resource import SocialAccountsResource
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

JSONAPIRESOURCE_ONE_OF_SCHEMAS = ["AdditionalEmailsResource", "CoursesResource", "DatesResource", "EventKindCategoriesResource", "EventKindsResource", "EventsResource", "GroupsResource", "InvoiceItemsResource", "InvoicesResource", "PeopleResource", "PersonNameResource", "PhoneNumbersResource", "RolesResource", "SocialAccountsResource"]

class JsonapiResource(BaseModel):
    """
    JsonapiResource
    """
    # data type: AdditionalEmailsResource
    oneof_schema_1_validator: Optional[AdditionalEmailsResource] = None
    # data type: CoursesResource
    oneof_schema_2_validator: Optional[CoursesResource] = None
    # data type: DatesResource
    oneof_schema_3_validator: Optional[DatesResource] = None
    # data type: EventKindCategoriesResource
    oneof_schema_4_validator: Optional[EventKindCategoriesResource] = None
    # data type: EventKindsResource
    oneof_schema_5_validator: Optional[EventKindsResource] = None
    # data type: EventsResource
    oneof_schema_6_validator: Optional[EventsResource] = None
    # data type: GroupsResource
    oneof_schema_7_validator: Optional[GroupsResource] = None
    # data type: InvoiceItemsResource
    oneof_schema_8_validator: Optional[InvoiceItemsResource] = None
    # data type: InvoicesResource
    oneof_schema_9_validator: Optional[InvoicesResource] = None
    # data type: PersonNameResource
    oneof_schema_10_validator: Optional[PersonNameResource] = None
    # data type: PeopleResource
    oneof_schema_11_validator: Optional[PeopleResource] = None
    # data type: PhoneNumbersResource
    oneof_schema_12_validator: Optional[PhoneNumbersResource] = None
    # data type: RolesResource
    oneof_schema_13_validator: Optional[RolesResource] = None
    # data type: SocialAccountsResource
    oneof_schema_14_validator: Optional[SocialAccountsResource] = None
    actual_instance: Optional[Union[AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource]] = None
    one_of_schemas: Set[str] = { "AdditionalEmailsResource", "CoursesResource", "DatesResource", "EventKindCategoriesResource", "EventKindsResource", "EventsResource", "GroupsResource", "InvoiceItemsResource", "InvoicesResource", "PeopleResource", "PersonNameResource", "PhoneNumbersResource", "RolesResource", "SocialAccountsResource" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = JsonapiResource.model_construct()
        error_messages = []
        match = 0
        # validate data type: AdditionalEmailsResource
        if not isinstance(v, AdditionalEmailsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AdditionalEmailsResource`")
        else:
            match += 1
        # validate data type: CoursesResource
        if not isinstance(v, CoursesResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CoursesResource`")
        else:
            match += 1
        # validate data type: DatesResource
        if not isinstance(v, DatesResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `DatesResource`")
        else:
            match += 1
        # validate data type: EventKindCategoriesResource
        if not isinstance(v, EventKindCategoriesResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EventKindCategoriesResource`")
        else:
            match += 1
        # validate data type: EventKindsResource
        if not isinstance(v, EventKindsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EventKindsResource`")
        else:
            match += 1
        # validate data type: EventsResource
        if not isinstance(v, EventsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EventsResource`")
        else:
            match += 1
        # validate data type: GroupsResource
        if not isinstance(v, GroupsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GroupsResource`")
        else:
            match += 1
        # validate data type: InvoiceItemsResource
        if not isinstance(v, InvoiceItemsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvoiceItemsResource`")
        else:
            match += 1
        # validate data type: InvoicesResource
        if not isinstance(v, InvoicesResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `InvoicesResource`")
        else:
            match += 1
        # validate data type: PersonNameResource
        if not isinstance(v, PersonNameResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PersonNameResource`")
        else:
            match += 1
        # validate data type: PeopleResource
        if not isinstance(v, PeopleResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PeopleResource`")
        else:
            match += 1
        # validate data type: PhoneNumbersResource
        if not isinstance(v, PhoneNumbersResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PhoneNumbersResource`")
        else:
            match += 1
        # validate data type: RolesResource
        if not isinstance(v, RolesResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `RolesResource`")
        else:
            match += 1
        # validate data type: SocialAccountsResource
        if not isinstance(v, SocialAccountsResource):
            error_messages.append(f"Error! Input type `{type(v)}` is not `SocialAccountsResource`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in JsonapiResource with oneOf schemas: AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in JsonapiResource with oneOf schemas: AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into AdditionalEmailsResource
        try:
            instance.actual_instance = AdditionalEmailsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CoursesResource
        try:
            instance.actual_instance = CoursesResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into DatesResource
        try:
            instance.actual_instance = DatesResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EventKindCategoriesResource
        try:
            instance.actual_instance = EventKindCategoriesResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EventKindsResource
        try:
            instance.actual_instance = EventKindsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EventsResource
        try:
            instance.actual_instance = EventsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GroupsResource
        try:
            instance.actual_instance = GroupsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InvoiceItemsResource
        try:
            instance.actual_instance = InvoiceItemsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into InvoicesResource
        try:
            instance.actual_instance = InvoicesResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PersonNameResource
        try:
            instance.actual_instance = PersonNameResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PeopleResource
        try:
            instance.actual_instance = PeopleResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PhoneNumbersResource
        try:
            instance.actual_instance = PhoneNumbersResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into RolesResource
        try:
            instance.actual_instance = RolesResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into SocialAccountsResource
        try:
            instance.actual_instance = SocialAccountsResource.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into JsonapiResource with oneOf schemas: AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into JsonapiResource with oneOf schemas: AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], AdditionalEmailsResource, CoursesResource, DatesResource, EventKindCategoriesResource, EventKindsResource, EventsResource, GroupsResource, InvoiceItemsResource, InvoicesResource, PeopleResource, PersonNameResource, PhoneNumbersResource, RolesResource, SocialAccountsResource]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


