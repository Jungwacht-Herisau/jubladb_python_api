# coding: utf-8

# flake8: noqa

"""
    Hitobito JSON:API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: v1
    Contact: oss@basilbader.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.1.1"

# import apis into sdk package
from jubladb_api.api.event_kind_categories_api import EventKindCategoriesApi
from jubladb_api.api.event_kinds_api import EventKindsApi
from jubladb_api.api.events_api import EventsApi
from jubladb_api.api.groups_api import GroupsApi
from jubladb_api.api.invoices_api import InvoicesApi
from jubladb_api.api.people_api import PeopleApi
from jubladb_api.api.roles_api import RolesApi

# import ApiClient
from jubladb_api.api_response import ApiResponse
from jubladb_api.api_client import ApiClient
from jubladb_api.configuration import Configuration
from jubladb_api.exceptions import OpenApiException
from jubladb_api.exceptions import ApiTypeError
from jubladb_api.exceptions import ApiValueError
from jubladb_api.exceptions import ApiKeyError
from jubladb_api.exceptions import ApiAttributeError
from jubladb_api.exceptions import ApiException

# import models into sdk package
from jubladb_api.models.additional_emails import AdditionalEmails
from jubladb_api.models.additional_emails_collection import AdditionalEmailsCollection
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.additional_emails_request import AdditionalEmailsRequest
from jubladb_api.models.additional_emails_resource import AdditionalEmailsResource
from jubladb_api.models.additional_emails_single import AdditionalEmailsSingle
from jubladb_api.models.additional_emails_single_links import AdditionalEmailsSingleLinks
from jubladb_api.models.courses import Courses
from jubladb_api.models.courses_collection import CoursesCollection
from jubladb_api.models.courses_readable_attribute import CoursesReadableAttribute
from jubladb_api.models.courses_relationships import CoursesRelationships
from jubladb_api.models.courses_relationships_contact import CoursesRelationshipsContact
from jubladb_api.models.courses_relationships_dates import CoursesRelationshipsDates
from jubladb_api.models.courses_request import CoursesRequest
from jubladb_api.models.courses_resource import CoursesResource
from jubladb_api.models.courses_single import CoursesSingle
from jubladb_api.models.dates import Dates
from jubladb_api.models.dates_collection import DatesCollection
from jubladb_api.models.dates_readable_attribute import DatesReadableAttribute
from jubladb_api.models.dates_relationships import DatesRelationships
from jubladb_api.models.dates_request import DatesRequest
from jubladb_api.models.dates_resource import DatesResource
from jubladb_api.models.dates_single import DatesSingle
from jubladb_api.models.event_kind_categories import EventKindCategories
from jubladb_api.models.event_kind_categories_collection import EventKindCategoriesCollection
from jubladb_api.models.event_kind_categories_readable_attribute import EventKindCategoriesReadableAttribute
from jubladb_api.models.event_kind_categories_request import EventKindCategoriesRequest
from jubladb_api.models.event_kind_categories_resource import EventKindCategoriesResource
from jubladb_api.models.event_kind_categories_single import EventKindCategoriesSingle
from jubladb_api.models.event_kinds import EventKinds
from jubladb_api.models.event_kinds_collection import EventKindsCollection
from jubladb_api.models.event_kinds_readable_attribute import EventKindsReadableAttribute
from jubladb_api.models.event_kinds_relationships import EventKindsRelationships
from jubladb_api.models.event_kinds_request import EventKindsRequest
from jubladb_api.models.event_kinds_resource import EventKindsResource
from jubladb_api.models.event_kinds_single import EventKindsSingle
from jubladb_api.models.events import Events
from jubladb_api.models.events_collection import EventsCollection
from jubladb_api.models.events_readable_attribute import EventsReadableAttribute
from jubladb_api.models.events_relationships import EventsRelationships
from jubladb_api.models.events_request import EventsRequest
from jubladb_api.models.events_resource import EventsResource
from jubladb_api.models.events_single import EventsSingle
from jubladb_api.models.groups import Groups
from jubladb_api.models.groups_collection import GroupsCollection
from jubladb_api.models.groups_extra_attribute import GroupsExtraAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.groups_relationships import GroupsRelationships
from jubladb_api.models.groups_request import GroupsRequest
from jubladb_api.models.groups_resource import GroupsResource
from jubladb_api.models.groups_single import GroupsSingle
from jubladb_api.models.invoice_items import InvoiceItems
from jubladb_api.models.invoice_items_collection import InvoiceItemsCollection
from jubladb_api.models.invoice_items_readable_attribute import InvoiceItemsReadableAttribute
from jubladb_api.models.invoice_items_relationships import InvoiceItemsRelationships
from jubladb_api.models.invoice_items_request import InvoiceItemsRequest
from jubladb_api.models.invoice_items_resource import InvoiceItemsResource
from jubladb_api.models.invoice_items_single import InvoiceItemsSingle
from jubladb_api.models.invoices import Invoices
from jubladb_api.models.invoices_collection import InvoicesCollection
from jubladb_api.models.invoices_readable_attribute import InvoicesReadableAttribute
from jubladb_api.models.invoices_relationships import InvoicesRelationships
from jubladb_api.models.invoices_request import InvoicesRequest
from jubladb_api.models.invoices_resource import InvoicesResource
from jubladb_api.models.invoices_single import InvoicesSingle
from jubladb_api.models.jsonapi_data import JsonapiData
from jubladb_api.models.jsonapi_error import JsonapiError
from jubladb_api.models.jsonapi_error_source import JsonapiErrorSource
from jubladb_api.models.jsonapi_failure import JsonapiFailure
from jubladb_api.models.jsonapi_info import JsonapiInfo
from jubladb_api.models.jsonapi_jsonapi import JsonapiJsonapi
from jubladb_api.models.jsonapi_link import JsonapiLink
from jubladb_api.models.jsonapi_link_one_of import JsonapiLinkOneOf
from jubladb_api.models.jsonapi_linkage import JsonapiLinkage
from jubladb_api.models.jsonapi_pagination import JsonapiPagination
from jubladb_api.models.jsonapi_relationship_links import JsonapiRelationshipLinks
from jubladb_api.models.jsonapi_resource import JsonapiResource
from jubladb_api.models.jsonapi_success import JsonapiSuccess
from jubladb_api.models.people import People
from jubladb_api.models.people_collection import PeopleCollection
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.people_relationships import PeopleRelationships
from jubladb_api.models.people_request import PeopleRequest
from jubladb_api.models.people_resource import PeopleResource
from jubladb_api.models.people_single import PeopleSingle
from jubladb_api.models.person_name import PersonName
from jubladb_api.models.person_name_collection import PersonNameCollection
from jubladb_api.models.person_name_readable_attribute import PersonNameReadableAttribute
from jubladb_api.models.person_name_request import PersonNameRequest
from jubladb_api.models.person_name_resource import PersonNameResource
from jubladb_api.models.person_name_single import PersonNameSingle
from jubladb_api.models.phone_numbers import PhoneNumbers
from jubladb_api.models.phone_numbers_collection import PhoneNumbersCollection
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.phone_numbers_request import PhoneNumbersRequest
from jubladb_api.models.phone_numbers_resource import PhoneNumbersResource
from jubladb_api.models.phone_numbers_single import PhoneNumbersSingle
from jubladb_api.models.roles import Roles
from jubladb_api.models.roles_collection import RolesCollection
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
from jubladb_api.models.roles_relationships import RolesRelationships
from jubladb_api.models.roles_request import RolesRequest
from jubladb_api.models.roles_resource import RolesResource
from jubladb_api.models.roles_single import RolesSingle
from jubladb_api.models.social_accounts import SocialAccounts
from jubladb_api.models.social_accounts_collection import SocialAccountsCollection
from jubladb_api.models.social_accounts_readable_attribute import SocialAccountsReadableAttribute
from jubladb_api.models.social_accounts_request import SocialAccountsRequest
from jubladb_api.models.social_accounts_resource import SocialAccountsResource
from jubladb_api.models.social_accounts_single import SocialAccountsSingle
from jubladb_api.models.types import Types

from jubladb_api import extensions
from jubladb_api import const