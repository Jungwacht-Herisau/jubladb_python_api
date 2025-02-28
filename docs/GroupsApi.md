# jubladb_api.GroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_group**](GroupsApi.md#get_group) | **GET** /api/groups/{id} | Fetch Group
[**list_groups**](GroupsApi.md#list_groups) | **GET** /api/groups | List Groups


# **get_group**
> GroupsSingle get_group(id, include=include, sort=sort, fields_groups=fields_groups, extra_fields_groups=extra_fields_groups, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_name_eq=filter_name_eq, filter_name_not_eq=filter_name_not_eq, filter_name_eql=filter_name_eql, filter_name_not_eql=filter_name_not_eql, filter_name_prefix=filter_name_prefix, filter_name_not_prefix=filter_name_not_prefix, filter_name_suffix=filter_name_suffix, filter_name_not_suffix=filter_name_not_suffix, filter_name_match=filter_name_match, filter_name_not_match=filter_name_not_match, filter_short_name_eq=filter_short_name_eq, filter_short_name_not_eq=filter_short_name_not_eq, filter_short_name_eql=filter_short_name_eql, filter_short_name_not_eql=filter_short_name_not_eql, filter_short_name_prefix=filter_short_name_prefix, filter_short_name_not_prefix=filter_short_name_not_prefix, filter_short_name_suffix=filter_short_name_suffix, filter_short_name_not_suffix=filter_short_name_not_suffix, filter_short_name_match=filter_short_name_match, filter_short_name_not_match=filter_short_name_not_match, filter_display_name_eq=filter_display_name_eq, filter_display_name_not_eq=filter_display_name_not_eq, filter_display_name_eql=filter_display_name_eql, filter_display_name_not_eql=filter_display_name_not_eql, filter_display_name_prefix=filter_display_name_prefix, filter_display_name_not_prefix=filter_display_name_not_prefix, filter_display_name_suffix=filter_display_name_suffix, filter_display_name_not_suffix=filter_display_name_not_suffix, filter_display_name_match=filter_display_name_match, filter_display_name_not_match=filter_display_name_not_match, filter_description_eq=filter_description_eq, filter_description_not_eq=filter_description_not_eq, filter_description_eql=filter_description_eql, filter_description_not_eql=filter_description_not_eql, filter_description_prefix=filter_description_prefix, filter_description_not_prefix=filter_description_not_prefix, filter_description_suffix=filter_description_suffix, filter_description_not_suffix=filter_description_not_suffix, filter_description_match=filter_description_match, filter_description_not_match=filter_description_not_match, filter_layer_eq=filter_layer_eq, filter_parent_id_eq=filter_parent_id_eq, filter_parent_id_not_eq=filter_parent_id_not_eq, filter_parent_id_gt=filter_parent_id_gt, filter_parent_id_gte=filter_parent_id_gte, filter_parent_id_lt=filter_parent_id_lt, filter_parent_id_lte=filter_parent_id_lte, filter_layer_group_id_eq=filter_layer_group_id_eq, filter_layer_group_id_not_eq=filter_layer_group_id_not_eq, filter_layer_group_id_gt=filter_layer_group_id_gt, filter_layer_group_id_gte=filter_layer_group_id_gte, filter_layer_group_id_lt=filter_layer_group_id_lt, filter_layer_group_id_lte=filter_layer_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_gt=filter_zip_code_gt, filter_zip_code_gte=filter_zip_code_gte, filter_zip_code_lt=filter_zip_code_lt, filter_zip_code_lte=filter_zip_code_lte, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_require_person_add_requests_eq=filter_require_person_add_requests_eq, filter_self_registration_url_eq=filter_self_registration_url_eq, filter_self_registration_url_not_eq=filter_self_registration_url_not_eq, filter_self_registration_url_eql=filter_self_registration_url_eql, filter_self_registration_url_not_eql=filter_self_registration_url_not_eql, filter_self_registration_url_prefix=filter_self_registration_url_prefix, filter_self_registration_url_not_prefix=filter_self_registration_url_not_prefix, filter_self_registration_url_suffix=filter_self_registration_url_suffix, filter_self_registration_url_not_suffix=filter_self_registration_url_not_suffix, filter_self_registration_url_match=filter_self_registration_url_match, filter_self_registration_url_not_match=filter_self_registration_url_not_match, filter_archived_at_eq=filter_archived_at_eq, filter_archived_at_not_eq=filter_archived_at_not_eq, filter_archived_at_gt=filter_archived_at_gt, filter_archived_at_gte=filter_archived_at_gte, filter_archived_at_lt=filter_archived_at_lt, filter_archived_at_lte=filter_archived_at_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_deleted_at_eq=filter_deleted_at_eq, filter_deleted_at_not_eq=filter_deleted_at_not_eq, filter_deleted_at_gt=filter_deleted_at_gt, filter_deleted_at_gte=filter_deleted_at_gte, filter_deleted_at_lt=filter_deleted_at_lt, filter_deleted_at_lte=filter_deleted_at_lte, filter_with_deleted_eq=filter_with_deleted_eq, filter_with_archived_eq=filter_with_archived_eq, fields_people=fields_people, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)

Fetch Group

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.groups_extra_attribute import GroupsExtraAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.groups_single import GroupsSingle
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.social_accounts_readable_attribute import SocialAccountsReadableAttribute
from jubladb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jubladb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ServiceTokenAuthHeader
configuration.api_key['ServiceTokenAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ServiceTokenAuthHeader'] = 'Bearer'

# Configure API key authorization: ServiceTokenAuthParam
configuration.api_key['ServiceTokenAuthParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ServiceTokenAuthParam'] = 'Bearer'

# Enter a context with an instance of the API client
with jubladb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jubladb_api.GroupsApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort groups according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    extra_fields_groups = [jubladb_api.GroupsExtraAttribute()] # List[GroupsExtraAttribute] | [Include specified extra fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Group by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Group by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Group by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Group by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Group by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Group by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_eq = ['filter_name_eq_example'] # List[str] | [Filter Group by name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_eq = ['filter_name_not_eq_example'] # List[str] | [Filter Group by name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_eql = ['filter_name_eql_example'] # List[str] | [Filter Group by name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_eql = ['filter_name_not_eql_example'] # List[str] | [Filter Group by name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_prefix = ['filter_name_prefix_example'] # List[str] | [Filter Group by name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_prefix = ['filter_name_not_prefix_example'] # List[str] | [Filter Group by name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_suffix = ['filter_name_suffix_example'] # List[str] | [Filter Group by name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_suffix = ['filter_name_not_suffix_example'] # List[str] | [Filter Group by name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_match = ['filter_name_match_example'] # List[str] | [Filter Group by name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_match = ['filter_name_not_match_example'] # List[str] | [Filter Group by name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_eq = ['filter_short_name_eq_example'] # List[str] | [Filter Group by short_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_eq = ['filter_short_name_not_eq_example'] # List[str] | [Filter Group by short_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_eql = ['filter_short_name_eql_example'] # List[str] | [Filter Group by short_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_eql = ['filter_short_name_not_eql_example'] # List[str] | [Filter Group by short_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_prefix = ['filter_short_name_prefix_example'] # List[str] | [Filter Group by short_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_prefix = ['filter_short_name_not_prefix_example'] # List[str] | [Filter Group by short_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_suffix = ['filter_short_name_suffix_example'] # List[str] | [Filter Group by short_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_suffix = ['filter_short_name_not_suffix_example'] # List[str] | [Filter Group by short_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_match = ['filter_short_name_match_example'] # List[str] | [Filter Group by short_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_match = ['filter_short_name_not_match_example'] # List[str] | [Filter Group by short_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_eq = ['filter_display_name_eq_example'] # List[str] | [Filter Group by display_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_eq = ['filter_display_name_not_eq_example'] # List[str] | [Filter Group by display_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_eql = ['filter_display_name_eql_example'] # List[str] | [Filter Group by display_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_eql = ['filter_display_name_not_eql_example'] # List[str] | [Filter Group by display_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_prefix = ['filter_display_name_prefix_example'] # List[str] | [Filter Group by display_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_prefix = ['filter_display_name_not_prefix_example'] # List[str] | [Filter Group by display_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_suffix = ['filter_display_name_suffix_example'] # List[str] | [Filter Group by display_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_suffix = ['filter_display_name_not_suffix_example'] # List[str] | [Filter Group by display_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_match = ['filter_display_name_match_example'] # List[str] | [Filter Group by display_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_match = ['filter_display_name_not_match_example'] # List[str] | [Filter Group by display_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_eq = ['filter_description_eq_example'] # List[str] | [Filter Group by description using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_eq = ['filter_description_not_eq_example'] # List[str] | [Filter Group by description using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_eql = ['filter_description_eql_example'] # List[str] | [Filter Group by description using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_eql = ['filter_description_not_eql_example'] # List[str] | [Filter Group by description using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_prefix = ['filter_description_prefix_example'] # List[str] | [Filter Group by description using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_prefix = ['filter_description_not_prefix_example'] # List[str] | [Filter Group by description using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_suffix = ['filter_description_suffix_example'] # List[str] | [Filter Group by description using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_suffix = ['filter_description_not_suffix_example'] # List[str] | [Filter Group by description using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_match = ['filter_description_match_example'] # List[str] | [Filter Group by description using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_match = ['filter_description_not_match_example'] # List[str] | [Filter Group by description using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_eq = True # bool | [Filter Group by layer using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_eq = [56] # List[int] | [Filter Group by parent_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_not_eq = [56] # List[int] | [Filter Group by parent_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_gt = [56] # List[int] | [Filter Group by parent_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_gte = [56] # List[int] | [Filter Group by parent_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_lt = [56] # List[int] | [Filter Group by parent_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_lte = [56] # List[int] | [Filter Group by parent_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_eq = [56] # List[int] | [Filter Group by layer_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_not_eq = [56] # List[int] | [Filter Group by layer_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_gt = [56] # List[int] | [Filter Group by layer_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_gte = [56] # List[int] | [Filter Group by layer_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_lt = [56] # List[int] | [Filter Group by layer_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_lte = [56] # List[int] | [Filter Group by layer_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Group by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Group by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Group by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Group by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Group by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Group by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Group by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Group by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Group by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Group by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eq = ['filter_email_eq_example'] # List[str] | [Filter Group by email using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eq = ['filter_email_not_eq_example'] # List[str] | [Filter Group by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eql = ['filter_email_eql_example'] # List[str] | [Filter Group by email using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eql = ['filter_email_not_eql_example'] # List[str] | [Filter Group by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_prefix = ['filter_email_prefix_example'] # List[str] | [Filter Group by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_prefix = ['filter_email_not_prefix_example'] # List[str] | [Filter Group by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_suffix = ['filter_email_suffix_example'] # List[str] | [Filter Group by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_suffix = ['filter_email_not_suffix_example'] # List[str] | [Filter Group by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_match = ['filter_email_match_example'] # List[str] | [Filter Group by email using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_match = ['filter_email_not_match_example'] # List[str] | [Filter Group by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eq = ['filter_address_eq_example'] # List[str] | [Filter Group by address using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eq = ['filter_address_not_eq_example'] # List[str] | [Filter Group by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eql = ['filter_address_eql_example'] # List[str] | [Filter Group by address using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eql = ['filter_address_not_eql_example'] # List[str] | [Filter Group by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_prefix = ['filter_address_prefix_example'] # List[str] | [Filter Group by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_prefix = ['filter_address_not_prefix_example'] # List[str] | [Filter Group by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_suffix = ['filter_address_suffix_example'] # List[str] | [Filter Group by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_suffix = ['filter_address_not_suffix_example'] # List[str] | [Filter Group by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_match = ['filter_address_match_example'] # List[str] | [Filter Group by address using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_match = ['filter_address_not_match_example'] # List[str] | [Filter Group by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eq = [56] # List[int] | [Filter Group by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eq = [56] # List[int] | [Filter Group by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_gt = [56] # List[int] | [Filter Group by zip_code using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_gte = [56] # List[int] | [Filter Group by zip_code using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_lt = [56] # List[int] | [Filter Group by zip_code using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_lte = [56] # List[int] | [Filter Group by zip_code using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eq = ['filter_town_eq_example'] # List[str] | [Filter Group by town using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eq = ['filter_town_not_eq_example'] # List[str] | [Filter Group by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eql = ['filter_town_eql_example'] # List[str] | [Filter Group by town using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eql = ['filter_town_not_eql_example'] # List[str] | [Filter Group by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_prefix = ['filter_town_prefix_example'] # List[str] | [Filter Group by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_prefix = ['filter_town_not_prefix_example'] # List[str] | [Filter Group by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_suffix = ['filter_town_suffix_example'] # List[str] | [Filter Group by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_suffix = ['filter_town_not_suffix_example'] # List[str] | [Filter Group by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_match = ['filter_town_match_example'] # List[str] | [Filter Group by town using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_match = ['filter_town_not_match_example'] # List[str] | [Filter Group by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eq = ['filter_country_eq_example'] # List[str] | [Filter Group by country using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eq = ['filter_country_not_eq_example'] # List[str] | [Filter Group by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eql = ['filter_country_eql_example'] # List[str] | [Filter Group by country using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eql = ['filter_country_not_eql_example'] # List[str] | [Filter Group by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_prefix = ['filter_country_prefix_example'] # List[str] | [Filter Group by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_prefix = ['filter_country_not_prefix_example'] # List[str] | [Filter Group by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_suffix = ['filter_country_suffix_example'] # List[str] | [Filter Group by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_suffix = ['filter_country_not_suffix_example'] # List[str] | [Filter Group by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_match = ['filter_country_match_example'] # List[str] | [Filter Group by country using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_match = ['filter_country_not_match_example'] # List[str] | [Filter Group by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_require_person_add_requests_eq = True # bool | [Filter Group by require_person_add_requests using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_eq = ['filter_self_registration_url_eq_example'] # List[str] | [Filter Group by self_registration_url using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_eq = ['filter_self_registration_url_not_eq_example'] # List[str] | [Filter Group by self_registration_url using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_eql = ['filter_self_registration_url_eql_example'] # List[str] | [Filter Group by self_registration_url using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_eql = ['filter_self_registration_url_not_eql_example'] # List[str] | [Filter Group by self_registration_url using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_prefix = ['filter_self_registration_url_prefix_example'] # List[str] | [Filter Group by self_registration_url using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_prefix = ['filter_self_registration_url_not_prefix_example'] # List[str] | [Filter Group by self_registration_url using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_suffix = ['filter_self_registration_url_suffix_example'] # List[str] | [Filter Group by self_registration_url using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_suffix = ['filter_self_registration_url_not_suffix_example'] # List[str] | [Filter Group by self_registration_url using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_match = ['filter_self_registration_url_match_example'] # List[str] | [Filter Group by self_registration_url using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_match = ['filter_self_registration_url_not_match_example'] # List[str] | [Filter Group by self_registration_url using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_with_deleted_eq = True # bool | [Filter Group by with_deleted using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_with_archived_eq = True # bool | [Filter Group by with_archived using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_phone_numbers = [jubladb_api.PhoneNumbersReadableAttribute()] # List[PhoneNumbersReadableAttribute] | [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_social_accounts = [jubladb_api.SocialAccountsReadableAttribute()] # List[SocialAccountsReadableAttribute] | [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_additional_emails = [jubladb_api.AdditionalEmailsReadableAttribute()] # List[AdditionalEmailsReadableAttribute] | [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Group
        api_response = api_instance.get_group(id, include=include, sort=sort, fields_groups=fields_groups, extra_fields_groups=extra_fields_groups, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_name_eq=filter_name_eq, filter_name_not_eq=filter_name_not_eq, filter_name_eql=filter_name_eql, filter_name_not_eql=filter_name_not_eql, filter_name_prefix=filter_name_prefix, filter_name_not_prefix=filter_name_not_prefix, filter_name_suffix=filter_name_suffix, filter_name_not_suffix=filter_name_not_suffix, filter_name_match=filter_name_match, filter_name_not_match=filter_name_not_match, filter_short_name_eq=filter_short_name_eq, filter_short_name_not_eq=filter_short_name_not_eq, filter_short_name_eql=filter_short_name_eql, filter_short_name_not_eql=filter_short_name_not_eql, filter_short_name_prefix=filter_short_name_prefix, filter_short_name_not_prefix=filter_short_name_not_prefix, filter_short_name_suffix=filter_short_name_suffix, filter_short_name_not_suffix=filter_short_name_not_suffix, filter_short_name_match=filter_short_name_match, filter_short_name_not_match=filter_short_name_not_match, filter_display_name_eq=filter_display_name_eq, filter_display_name_not_eq=filter_display_name_not_eq, filter_display_name_eql=filter_display_name_eql, filter_display_name_not_eql=filter_display_name_not_eql, filter_display_name_prefix=filter_display_name_prefix, filter_display_name_not_prefix=filter_display_name_not_prefix, filter_display_name_suffix=filter_display_name_suffix, filter_display_name_not_suffix=filter_display_name_not_suffix, filter_display_name_match=filter_display_name_match, filter_display_name_not_match=filter_display_name_not_match, filter_description_eq=filter_description_eq, filter_description_not_eq=filter_description_not_eq, filter_description_eql=filter_description_eql, filter_description_not_eql=filter_description_not_eql, filter_description_prefix=filter_description_prefix, filter_description_not_prefix=filter_description_not_prefix, filter_description_suffix=filter_description_suffix, filter_description_not_suffix=filter_description_not_suffix, filter_description_match=filter_description_match, filter_description_not_match=filter_description_not_match, filter_layer_eq=filter_layer_eq, filter_parent_id_eq=filter_parent_id_eq, filter_parent_id_not_eq=filter_parent_id_not_eq, filter_parent_id_gt=filter_parent_id_gt, filter_parent_id_gte=filter_parent_id_gte, filter_parent_id_lt=filter_parent_id_lt, filter_parent_id_lte=filter_parent_id_lte, filter_layer_group_id_eq=filter_layer_group_id_eq, filter_layer_group_id_not_eq=filter_layer_group_id_not_eq, filter_layer_group_id_gt=filter_layer_group_id_gt, filter_layer_group_id_gte=filter_layer_group_id_gte, filter_layer_group_id_lt=filter_layer_group_id_lt, filter_layer_group_id_lte=filter_layer_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_gt=filter_zip_code_gt, filter_zip_code_gte=filter_zip_code_gte, filter_zip_code_lt=filter_zip_code_lt, filter_zip_code_lte=filter_zip_code_lte, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_require_person_add_requests_eq=filter_require_person_add_requests_eq, filter_self_registration_url_eq=filter_self_registration_url_eq, filter_self_registration_url_not_eq=filter_self_registration_url_not_eq, filter_self_registration_url_eql=filter_self_registration_url_eql, filter_self_registration_url_not_eql=filter_self_registration_url_not_eql, filter_self_registration_url_prefix=filter_self_registration_url_prefix, filter_self_registration_url_not_prefix=filter_self_registration_url_not_prefix, filter_self_registration_url_suffix=filter_self_registration_url_suffix, filter_self_registration_url_not_suffix=filter_self_registration_url_not_suffix, filter_self_registration_url_match=filter_self_registration_url_match, filter_self_registration_url_not_match=filter_self_registration_url_not_match, filter_archived_at_eq=filter_archived_at_eq, filter_archived_at_not_eq=filter_archived_at_not_eq, filter_archived_at_gt=filter_archived_at_gt, filter_archived_at_gte=filter_archived_at_gte, filter_archived_at_lt=filter_archived_at_lt, filter_archived_at_lte=filter_archived_at_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_deleted_at_eq=filter_deleted_at_eq, filter_deleted_at_not_eq=filter_deleted_at_not_eq, filter_deleted_at_gt=filter_deleted_at_gt, filter_deleted_at_gte=filter_deleted_at_gte, filter_deleted_at_lt=filter_deleted_at_lt, filter_deleted_at_lte=filter_deleted_at_lte, filter_with_deleted_eq=filter_with_deleted_eq, filter_with_archived_eq=filter_with_archived_eq, fields_people=fields_people, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)
        print("The response of GroupsApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->get_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort groups according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **extra_fields_groups** | [**List[GroupsExtraAttribute]**](GroupsExtraAttribute.md)| [Include specified extra fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Group by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Group by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Group by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Group by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Group by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Group by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_eq** | [**List[str]**](str.md)| [Filter Group by name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_eq** | [**List[str]**](str.md)| [Filter Group by name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_eql** | [**List[str]**](str.md)| [Filter Group by name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_eql** | [**List[str]**](str.md)| [Filter Group by name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_prefix** | [**List[str]**](str.md)| [Filter Group by name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_suffix** | [**List[str]**](str.md)| [Filter Group by name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_match** | [**List[str]**](str.md)| [Filter Group by name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_match** | [**List[str]**](str.md)| [Filter Group by name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_eq** | [**List[str]**](str.md)| [Filter Group by short_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_eq** | [**List[str]**](str.md)| [Filter Group by short_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_eql** | [**List[str]**](str.md)| [Filter Group by short_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_eql** | [**List[str]**](str.md)| [Filter Group by short_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_prefix** | [**List[str]**](str.md)| [Filter Group by short_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by short_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_suffix** | [**List[str]**](str.md)| [Filter Group by short_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by short_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_match** | [**List[str]**](str.md)| [Filter Group by short_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_match** | [**List[str]**](str.md)| [Filter Group by short_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_eq** | [**List[str]**](str.md)| [Filter Group by display_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_eq** | [**List[str]**](str.md)| [Filter Group by display_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_eql** | [**List[str]**](str.md)| [Filter Group by display_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_eql** | [**List[str]**](str.md)| [Filter Group by display_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_prefix** | [**List[str]**](str.md)| [Filter Group by display_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by display_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_suffix** | [**List[str]**](str.md)| [Filter Group by display_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by display_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_match** | [**List[str]**](str.md)| [Filter Group by display_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_match** | [**List[str]**](str.md)| [Filter Group by display_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_eq** | [**List[str]**](str.md)| [Filter Group by description using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_eq** | [**List[str]**](str.md)| [Filter Group by description using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_eql** | [**List[str]**](str.md)| [Filter Group by description using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_eql** | [**List[str]**](str.md)| [Filter Group by description using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_prefix** | [**List[str]**](str.md)| [Filter Group by description using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_prefix** | [**List[str]**](str.md)| [Filter Group by description using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_suffix** | [**List[str]**](str.md)| [Filter Group by description using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_suffix** | [**List[str]**](str.md)| [Filter Group by description using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_match** | [**List[str]**](str.md)| [Filter Group by description using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_match** | [**List[str]**](str.md)| [Filter Group by description using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_eq** | **bool**| [Filter Group by layer using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_eq** | [**List[int]**](int.md)| [Filter Group by parent_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_not_eq** | [**List[int]**](int.md)| [Filter Group by parent_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_gt** | [**List[int]**](int.md)| [Filter Group by parent_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_gte** | [**List[int]**](int.md)| [Filter Group by parent_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_lt** | [**List[int]**](int.md)| [Filter Group by parent_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_lte** | [**List[int]**](int.md)| [Filter Group by parent_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_eq** | [**List[int]**](int.md)| [Filter Group by layer_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_not_eq** | [**List[int]**](int.md)| [Filter Group by layer_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_gt** | [**List[int]**](int.md)| [Filter Group by layer_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_gte** | [**List[int]**](int.md)| [Filter Group by layer_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_lt** | [**List[int]**](int.md)| [Filter Group by layer_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_lte** | [**List[int]**](int.md)| [Filter Group by layer_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Group by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Group by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Group by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Group by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Group by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Group by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Group by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Group by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Group by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Group by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eq** | [**List[str]**](str.md)| [Filter Group by email using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eq** | [**List[str]**](str.md)| [Filter Group by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eql** | [**List[str]**](str.md)| [Filter Group by email using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eql** | [**List[str]**](str.md)| [Filter Group by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_prefix** | [**List[str]**](str.md)| [Filter Group by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_prefix** | [**List[str]**](str.md)| [Filter Group by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_suffix** | [**List[str]**](str.md)| [Filter Group by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_suffix** | [**List[str]**](str.md)| [Filter Group by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_match** | [**List[str]**](str.md)| [Filter Group by email using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_match** | [**List[str]**](str.md)| [Filter Group by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eq** | [**List[str]**](str.md)| [Filter Group by address using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eq** | [**List[str]**](str.md)| [Filter Group by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eql** | [**List[str]**](str.md)| [Filter Group by address using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eql** | [**List[str]**](str.md)| [Filter Group by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_prefix** | [**List[str]**](str.md)| [Filter Group by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_prefix** | [**List[str]**](str.md)| [Filter Group by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_suffix** | [**List[str]**](str.md)| [Filter Group by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_suffix** | [**List[str]**](str.md)| [Filter Group by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_match** | [**List[str]**](str.md)| [Filter Group by address using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_match** | [**List[str]**](str.md)| [Filter Group by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eq** | [**List[int]**](int.md)| [Filter Group by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eq** | [**List[int]**](int.md)| [Filter Group by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_gt** | [**List[int]**](int.md)| [Filter Group by zip_code using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_gte** | [**List[int]**](int.md)| [Filter Group by zip_code using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_lt** | [**List[int]**](int.md)| [Filter Group by zip_code using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_lte** | [**List[int]**](int.md)| [Filter Group by zip_code using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eq** | [**List[str]**](str.md)| [Filter Group by town using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eq** | [**List[str]**](str.md)| [Filter Group by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eql** | [**List[str]**](str.md)| [Filter Group by town using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eql** | [**List[str]**](str.md)| [Filter Group by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_prefix** | [**List[str]**](str.md)| [Filter Group by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_prefix** | [**List[str]**](str.md)| [Filter Group by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_suffix** | [**List[str]**](str.md)| [Filter Group by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_suffix** | [**List[str]**](str.md)| [Filter Group by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_match** | [**List[str]**](str.md)| [Filter Group by town using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_match** | [**List[str]**](str.md)| [Filter Group by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eq** | [**List[str]**](str.md)| [Filter Group by country using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eq** | [**List[str]**](str.md)| [Filter Group by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eql** | [**List[str]**](str.md)| [Filter Group by country using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eql** | [**List[str]**](str.md)| [Filter Group by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_prefix** | [**List[str]**](str.md)| [Filter Group by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_prefix** | [**List[str]**](str.md)| [Filter Group by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_suffix** | [**List[str]**](str.md)| [Filter Group by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_suffix** | [**List[str]**](str.md)| [Filter Group by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_match** | [**List[str]**](str.md)| [Filter Group by country using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_match** | [**List[str]**](str.md)| [Filter Group by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_require_person_add_requests_eq** | **bool**| [Filter Group by require_person_add_requests using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_eq** | [**List[str]**](str.md)| [Filter Group by self_registration_url using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_eq** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_eql** | [**List[str]**](str.md)| [Filter Group by self_registration_url using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_eql** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_prefix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_prefix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_suffix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_suffix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_match** | [**List[str]**](str.md)| [Filter Group by self_registration_url using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_match** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_with_deleted_eq** | **bool**| [Filter Group by with_deleted using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_with_archived_eq** | **bool**| [Filter Group by with_archived using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_phone_numbers** | [**List[PhoneNumbersReadableAttribute]**](PhoneNumbersReadableAttribute.md)| [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_social_accounts** | [**List[SocialAccountsReadableAttribute]**](SocialAccountsReadableAttribute.md)| [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_additional_emails** | [**List[AdditionalEmailsReadableAttribute]**](AdditionalEmailsReadableAttribute.md)| [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**GroupsSingle**](GroupsSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Group resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> GroupsCollection list_groups(include=include, sort=sort, fields_groups=fields_groups, extra_fields_groups=extra_fields_groups, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_name_eq=filter_name_eq, filter_name_not_eq=filter_name_not_eq, filter_name_eql=filter_name_eql, filter_name_not_eql=filter_name_not_eql, filter_name_prefix=filter_name_prefix, filter_name_not_prefix=filter_name_not_prefix, filter_name_suffix=filter_name_suffix, filter_name_not_suffix=filter_name_not_suffix, filter_name_match=filter_name_match, filter_name_not_match=filter_name_not_match, filter_short_name_eq=filter_short_name_eq, filter_short_name_not_eq=filter_short_name_not_eq, filter_short_name_eql=filter_short_name_eql, filter_short_name_not_eql=filter_short_name_not_eql, filter_short_name_prefix=filter_short_name_prefix, filter_short_name_not_prefix=filter_short_name_not_prefix, filter_short_name_suffix=filter_short_name_suffix, filter_short_name_not_suffix=filter_short_name_not_suffix, filter_short_name_match=filter_short_name_match, filter_short_name_not_match=filter_short_name_not_match, filter_display_name_eq=filter_display_name_eq, filter_display_name_not_eq=filter_display_name_not_eq, filter_display_name_eql=filter_display_name_eql, filter_display_name_not_eql=filter_display_name_not_eql, filter_display_name_prefix=filter_display_name_prefix, filter_display_name_not_prefix=filter_display_name_not_prefix, filter_display_name_suffix=filter_display_name_suffix, filter_display_name_not_suffix=filter_display_name_not_suffix, filter_display_name_match=filter_display_name_match, filter_display_name_not_match=filter_display_name_not_match, filter_description_eq=filter_description_eq, filter_description_not_eq=filter_description_not_eq, filter_description_eql=filter_description_eql, filter_description_not_eql=filter_description_not_eql, filter_description_prefix=filter_description_prefix, filter_description_not_prefix=filter_description_not_prefix, filter_description_suffix=filter_description_suffix, filter_description_not_suffix=filter_description_not_suffix, filter_description_match=filter_description_match, filter_description_not_match=filter_description_not_match, filter_layer_eq=filter_layer_eq, filter_parent_id_eq=filter_parent_id_eq, filter_parent_id_not_eq=filter_parent_id_not_eq, filter_parent_id_gt=filter_parent_id_gt, filter_parent_id_gte=filter_parent_id_gte, filter_parent_id_lt=filter_parent_id_lt, filter_parent_id_lte=filter_parent_id_lte, filter_layer_group_id_eq=filter_layer_group_id_eq, filter_layer_group_id_not_eq=filter_layer_group_id_not_eq, filter_layer_group_id_gt=filter_layer_group_id_gt, filter_layer_group_id_gte=filter_layer_group_id_gte, filter_layer_group_id_lt=filter_layer_group_id_lt, filter_layer_group_id_lte=filter_layer_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_gt=filter_zip_code_gt, filter_zip_code_gte=filter_zip_code_gte, filter_zip_code_lt=filter_zip_code_lt, filter_zip_code_lte=filter_zip_code_lte, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_require_person_add_requests_eq=filter_require_person_add_requests_eq, filter_self_registration_url_eq=filter_self_registration_url_eq, filter_self_registration_url_not_eq=filter_self_registration_url_not_eq, filter_self_registration_url_eql=filter_self_registration_url_eql, filter_self_registration_url_not_eql=filter_self_registration_url_not_eql, filter_self_registration_url_prefix=filter_self_registration_url_prefix, filter_self_registration_url_not_prefix=filter_self_registration_url_not_prefix, filter_self_registration_url_suffix=filter_self_registration_url_suffix, filter_self_registration_url_not_suffix=filter_self_registration_url_not_suffix, filter_self_registration_url_match=filter_self_registration_url_match, filter_self_registration_url_not_match=filter_self_registration_url_not_match, filter_archived_at_eq=filter_archived_at_eq, filter_archived_at_not_eq=filter_archived_at_not_eq, filter_archived_at_gt=filter_archived_at_gt, filter_archived_at_gte=filter_archived_at_gte, filter_archived_at_lt=filter_archived_at_lt, filter_archived_at_lte=filter_archived_at_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_deleted_at_eq=filter_deleted_at_eq, filter_deleted_at_not_eq=filter_deleted_at_not_eq, filter_deleted_at_gt=filter_deleted_at_gt, filter_deleted_at_gte=filter_deleted_at_gte, filter_deleted_at_lt=filter_deleted_at_lt, filter_deleted_at_lte=filter_deleted_at_lte, filter_with_deleted_eq=filter_with_deleted_eq, filter_with_archived_eq=filter_with_archived_eq, fields_people=fields_people, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)

List Groups

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.groups_collection import GroupsCollection
from jubladb_api.models.groups_extra_attribute import GroupsExtraAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.social_accounts_readable_attribute import SocialAccountsReadableAttribute
from jubladb_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = jubladb_api.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ServiceTokenAuthHeader
configuration.api_key['ServiceTokenAuthHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ServiceTokenAuthHeader'] = 'Bearer'

# Configure API key authorization: ServiceTokenAuthParam
configuration.api_key['ServiceTokenAuthParam'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ServiceTokenAuthParam'] = 'Bearer'

# Enter a context with an instance of the API client
with jubladb_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = jubladb_api.GroupsApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort groups according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    extra_fields_groups = [jubladb_api.GroupsExtraAttribute()] # List[GroupsExtraAttribute] | [Include specified extra fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Group by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Group by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Group by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Group by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Group by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Group by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_eq = ['filter_name_eq_example'] # List[str] | [Filter Group by name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_eq = ['filter_name_not_eq_example'] # List[str] | [Filter Group by name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_eql = ['filter_name_eql_example'] # List[str] | [Filter Group by name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_eql = ['filter_name_not_eql_example'] # List[str] | [Filter Group by name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_prefix = ['filter_name_prefix_example'] # List[str] | [Filter Group by name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_prefix = ['filter_name_not_prefix_example'] # List[str] | [Filter Group by name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_suffix = ['filter_name_suffix_example'] # List[str] | [Filter Group by name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_suffix = ['filter_name_not_suffix_example'] # List[str] | [Filter Group by name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_match = ['filter_name_match_example'] # List[str] | [Filter Group by name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_name_not_match = ['filter_name_not_match_example'] # List[str] | [Filter Group by name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_eq = ['filter_short_name_eq_example'] # List[str] | [Filter Group by short_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_eq = ['filter_short_name_not_eq_example'] # List[str] | [Filter Group by short_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_eql = ['filter_short_name_eql_example'] # List[str] | [Filter Group by short_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_eql = ['filter_short_name_not_eql_example'] # List[str] | [Filter Group by short_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_prefix = ['filter_short_name_prefix_example'] # List[str] | [Filter Group by short_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_prefix = ['filter_short_name_not_prefix_example'] # List[str] | [Filter Group by short_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_suffix = ['filter_short_name_suffix_example'] # List[str] | [Filter Group by short_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_suffix = ['filter_short_name_not_suffix_example'] # List[str] | [Filter Group by short_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_match = ['filter_short_name_match_example'] # List[str] | [Filter Group by short_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_short_name_not_match = ['filter_short_name_not_match_example'] # List[str] | [Filter Group by short_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_eq = ['filter_display_name_eq_example'] # List[str] | [Filter Group by display_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_eq = ['filter_display_name_not_eq_example'] # List[str] | [Filter Group by display_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_eql = ['filter_display_name_eql_example'] # List[str] | [Filter Group by display_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_eql = ['filter_display_name_not_eql_example'] # List[str] | [Filter Group by display_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_prefix = ['filter_display_name_prefix_example'] # List[str] | [Filter Group by display_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_prefix = ['filter_display_name_not_prefix_example'] # List[str] | [Filter Group by display_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_suffix = ['filter_display_name_suffix_example'] # List[str] | [Filter Group by display_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_suffix = ['filter_display_name_not_suffix_example'] # List[str] | [Filter Group by display_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_match = ['filter_display_name_match_example'] # List[str] | [Filter Group by display_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_display_name_not_match = ['filter_display_name_not_match_example'] # List[str] | [Filter Group by display_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_eq = ['filter_description_eq_example'] # List[str] | [Filter Group by description using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_eq = ['filter_description_not_eq_example'] # List[str] | [Filter Group by description using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_eql = ['filter_description_eql_example'] # List[str] | [Filter Group by description using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_eql = ['filter_description_not_eql_example'] # List[str] | [Filter Group by description using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_prefix = ['filter_description_prefix_example'] # List[str] | [Filter Group by description using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_prefix = ['filter_description_not_prefix_example'] # List[str] | [Filter Group by description using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_suffix = ['filter_description_suffix_example'] # List[str] | [Filter Group by description using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_suffix = ['filter_description_not_suffix_example'] # List[str] | [Filter Group by description using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_match = ['filter_description_match_example'] # List[str] | [Filter Group by description using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_description_not_match = ['filter_description_not_match_example'] # List[str] | [Filter Group by description using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_eq = True # bool | [Filter Group by layer using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_eq = [56] # List[int] | [Filter Group by parent_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_not_eq = [56] # List[int] | [Filter Group by parent_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_gt = [56] # List[int] | [Filter Group by parent_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_gte = [56] # List[int] | [Filter Group by parent_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_lt = [56] # List[int] | [Filter Group by parent_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_parent_id_lte = [56] # List[int] | [Filter Group by parent_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_eq = [56] # List[int] | [Filter Group by layer_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_not_eq = [56] # List[int] | [Filter Group by layer_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_gt = [56] # List[int] | [Filter Group by layer_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_gte = [56] # List[int] | [Filter Group by layer_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_lt = [56] # List[int] | [Filter Group by layer_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_layer_group_id_lte = [56] # List[int] | [Filter Group by layer_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Group by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Group by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Group by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Group by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Group by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Group by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Group by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Group by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Group by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Group by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eq = ['filter_email_eq_example'] # List[str] | [Filter Group by email using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eq = ['filter_email_not_eq_example'] # List[str] | [Filter Group by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eql = ['filter_email_eql_example'] # List[str] | [Filter Group by email using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eql = ['filter_email_not_eql_example'] # List[str] | [Filter Group by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_prefix = ['filter_email_prefix_example'] # List[str] | [Filter Group by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_prefix = ['filter_email_not_prefix_example'] # List[str] | [Filter Group by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_suffix = ['filter_email_suffix_example'] # List[str] | [Filter Group by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_suffix = ['filter_email_not_suffix_example'] # List[str] | [Filter Group by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_match = ['filter_email_match_example'] # List[str] | [Filter Group by email using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_match = ['filter_email_not_match_example'] # List[str] | [Filter Group by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eq = ['filter_address_eq_example'] # List[str] | [Filter Group by address using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eq = ['filter_address_not_eq_example'] # List[str] | [Filter Group by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eql = ['filter_address_eql_example'] # List[str] | [Filter Group by address using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eql = ['filter_address_not_eql_example'] # List[str] | [Filter Group by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_prefix = ['filter_address_prefix_example'] # List[str] | [Filter Group by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_prefix = ['filter_address_not_prefix_example'] # List[str] | [Filter Group by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_suffix = ['filter_address_suffix_example'] # List[str] | [Filter Group by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_suffix = ['filter_address_not_suffix_example'] # List[str] | [Filter Group by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_match = ['filter_address_match_example'] # List[str] | [Filter Group by address using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_match = ['filter_address_not_match_example'] # List[str] | [Filter Group by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eq = [56] # List[int] | [Filter Group by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eq = [56] # List[int] | [Filter Group by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_gt = [56] # List[int] | [Filter Group by zip_code using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_gte = [56] # List[int] | [Filter Group by zip_code using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_lt = [56] # List[int] | [Filter Group by zip_code using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_lte = [56] # List[int] | [Filter Group by zip_code using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eq = ['filter_town_eq_example'] # List[str] | [Filter Group by town using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eq = ['filter_town_not_eq_example'] # List[str] | [Filter Group by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eql = ['filter_town_eql_example'] # List[str] | [Filter Group by town using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eql = ['filter_town_not_eql_example'] # List[str] | [Filter Group by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_prefix = ['filter_town_prefix_example'] # List[str] | [Filter Group by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_prefix = ['filter_town_not_prefix_example'] # List[str] | [Filter Group by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_suffix = ['filter_town_suffix_example'] # List[str] | [Filter Group by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_suffix = ['filter_town_not_suffix_example'] # List[str] | [Filter Group by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_match = ['filter_town_match_example'] # List[str] | [Filter Group by town using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_match = ['filter_town_not_match_example'] # List[str] | [Filter Group by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eq = ['filter_country_eq_example'] # List[str] | [Filter Group by country using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eq = ['filter_country_not_eq_example'] # List[str] | [Filter Group by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eql = ['filter_country_eql_example'] # List[str] | [Filter Group by country using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eql = ['filter_country_not_eql_example'] # List[str] | [Filter Group by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_prefix = ['filter_country_prefix_example'] # List[str] | [Filter Group by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_prefix = ['filter_country_not_prefix_example'] # List[str] | [Filter Group by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_suffix = ['filter_country_suffix_example'] # List[str] | [Filter Group by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_suffix = ['filter_country_not_suffix_example'] # List[str] | [Filter Group by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_match = ['filter_country_match_example'] # List[str] | [Filter Group by country using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_match = ['filter_country_not_match_example'] # List[str] | [Filter Group by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_require_person_add_requests_eq = True # bool | [Filter Group by require_person_add_requests using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_eq = ['filter_self_registration_url_eq_example'] # List[str] | [Filter Group by self_registration_url using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_eq = ['filter_self_registration_url_not_eq_example'] # List[str] | [Filter Group by self_registration_url using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_eql = ['filter_self_registration_url_eql_example'] # List[str] | [Filter Group by self_registration_url using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_eql = ['filter_self_registration_url_not_eql_example'] # List[str] | [Filter Group by self_registration_url using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_prefix = ['filter_self_registration_url_prefix_example'] # List[str] | [Filter Group by self_registration_url using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_prefix = ['filter_self_registration_url_not_prefix_example'] # List[str] | [Filter Group by self_registration_url using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_suffix = ['filter_self_registration_url_suffix_example'] # List[str] | [Filter Group by self_registration_url using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_suffix = ['filter_self_registration_url_not_suffix_example'] # List[str] | [Filter Group by self_registration_url using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_match = ['filter_self_registration_url_match_example'] # List[str] | [Filter Group by self_registration_url using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_self_registration_url_not_match = ['filter_self_registration_url_not_match_example'] # List[str] | [Filter Group by self_registration_url using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_archived_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by archived_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_deleted_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Group by deleted_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_with_deleted_eq = True # bool | [Filter Group by with_deleted using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_with_archived_eq = True # bool | [Filter Group by with_archived using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_phone_numbers = [jubladb_api.PhoneNumbersReadableAttribute()] # List[PhoneNumbersReadableAttribute] | [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_social_accounts = [jubladb_api.SocialAccountsReadableAttribute()] # List[SocialAccountsReadableAttribute] | [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_additional_emails = [jubladb_api.AdditionalEmailsReadableAttribute()] # List[AdditionalEmailsReadableAttribute] | [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List Groups
        api_response = api_instance.list_groups(include=include, sort=sort, fields_groups=fields_groups, extra_fields_groups=extra_fields_groups, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_name_eq=filter_name_eq, filter_name_not_eq=filter_name_not_eq, filter_name_eql=filter_name_eql, filter_name_not_eql=filter_name_not_eql, filter_name_prefix=filter_name_prefix, filter_name_not_prefix=filter_name_not_prefix, filter_name_suffix=filter_name_suffix, filter_name_not_suffix=filter_name_not_suffix, filter_name_match=filter_name_match, filter_name_not_match=filter_name_not_match, filter_short_name_eq=filter_short_name_eq, filter_short_name_not_eq=filter_short_name_not_eq, filter_short_name_eql=filter_short_name_eql, filter_short_name_not_eql=filter_short_name_not_eql, filter_short_name_prefix=filter_short_name_prefix, filter_short_name_not_prefix=filter_short_name_not_prefix, filter_short_name_suffix=filter_short_name_suffix, filter_short_name_not_suffix=filter_short_name_not_suffix, filter_short_name_match=filter_short_name_match, filter_short_name_not_match=filter_short_name_not_match, filter_display_name_eq=filter_display_name_eq, filter_display_name_not_eq=filter_display_name_not_eq, filter_display_name_eql=filter_display_name_eql, filter_display_name_not_eql=filter_display_name_not_eql, filter_display_name_prefix=filter_display_name_prefix, filter_display_name_not_prefix=filter_display_name_not_prefix, filter_display_name_suffix=filter_display_name_suffix, filter_display_name_not_suffix=filter_display_name_not_suffix, filter_display_name_match=filter_display_name_match, filter_display_name_not_match=filter_display_name_not_match, filter_description_eq=filter_description_eq, filter_description_not_eq=filter_description_not_eq, filter_description_eql=filter_description_eql, filter_description_not_eql=filter_description_not_eql, filter_description_prefix=filter_description_prefix, filter_description_not_prefix=filter_description_not_prefix, filter_description_suffix=filter_description_suffix, filter_description_not_suffix=filter_description_not_suffix, filter_description_match=filter_description_match, filter_description_not_match=filter_description_not_match, filter_layer_eq=filter_layer_eq, filter_parent_id_eq=filter_parent_id_eq, filter_parent_id_not_eq=filter_parent_id_not_eq, filter_parent_id_gt=filter_parent_id_gt, filter_parent_id_gte=filter_parent_id_gte, filter_parent_id_lt=filter_parent_id_lt, filter_parent_id_lte=filter_parent_id_lte, filter_layer_group_id_eq=filter_layer_group_id_eq, filter_layer_group_id_not_eq=filter_layer_group_id_not_eq, filter_layer_group_id_gt=filter_layer_group_id_gt, filter_layer_group_id_gte=filter_layer_group_id_gte, filter_layer_group_id_lt=filter_layer_group_id_lt, filter_layer_group_id_lte=filter_layer_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_gt=filter_zip_code_gt, filter_zip_code_gte=filter_zip_code_gte, filter_zip_code_lt=filter_zip_code_lt, filter_zip_code_lte=filter_zip_code_lte, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_require_person_add_requests_eq=filter_require_person_add_requests_eq, filter_self_registration_url_eq=filter_self_registration_url_eq, filter_self_registration_url_not_eq=filter_self_registration_url_not_eq, filter_self_registration_url_eql=filter_self_registration_url_eql, filter_self_registration_url_not_eql=filter_self_registration_url_not_eql, filter_self_registration_url_prefix=filter_self_registration_url_prefix, filter_self_registration_url_not_prefix=filter_self_registration_url_not_prefix, filter_self_registration_url_suffix=filter_self_registration_url_suffix, filter_self_registration_url_not_suffix=filter_self_registration_url_not_suffix, filter_self_registration_url_match=filter_self_registration_url_match, filter_self_registration_url_not_match=filter_self_registration_url_not_match, filter_archived_at_eq=filter_archived_at_eq, filter_archived_at_not_eq=filter_archived_at_not_eq, filter_archived_at_gt=filter_archived_at_gt, filter_archived_at_gte=filter_archived_at_gte, filter_archived_at_lt=filter_archived_at_lt, filter_archived_at_lte=filter_archived_at_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_deleted_at_eq=filter_deleted_at_eq, filter_deleted_at_not_eq=filter_deleted_at_not_eq, filter_deleted_at_gt=filter_deleted_at_gt, filter_deleted_at_gte=filter_deleted_at_gte, filter_deleted_at_lt=filter_deleted_at_lt, filter_deleted_at_lte=filter_deleted_at_lte, filter_with_deleted_eq=filter_with_deleted_eq, filter_with_archived_eq=filter_with_archived_eq, fields_people=fields_people, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)
        print("The response of GroupsApi->list_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort groups according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **extra_fields_groups** | [**List[GroupsExtraAttribute]**](GroupsExtraAttribute.md)| [Include specified extra fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Group by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Group by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Group by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Group by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Group by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Group by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_eq** | [**List[str]**](str.md)| [Filter Group by name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_eq** | [**List[str]**](str.md)| [Filter Group by name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_eql** | [**List[str]**](str.md)| [Filter Group by name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_eql** | [**List[str]**](str.md)| [Filter Group by name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_prefix** | [**List[str]**](str.md)| [Filter Group by name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_suffix** | [**List[str]**](str.md)| [Filter Group by name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_match** | [**List[str]**](str.md)| [Filter Group by name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_name_not_match** | [**List[str]**](str.md)| [Filter Group by name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_eq** | [**List[str]**](str.md)| [Filter Group by short_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_eq** | [**List[str]**](str.md)| [Filter Group by short_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_eql** | [**List[str]**](str.md)| [Filter Group by short_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_eql** | [**List[str]**](str.md)| [Filter Group by short_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_prefix** | [**List[str]**](str.md)| [Filter Group by short_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by short_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_suffix** | [**List[str]**](str.md)| [Filter Group by short_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by short_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_match** | [**List[str]**](str.md)| [Filter Group by short_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_short_name_not_match** | [**List[str]**](str.md)| [Filter Group by short_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_eq** | [**List[str]**](str.md)| [Filter Group by display_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_eq** | [**List[str]**](str.md)| [Filter Group by display_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_eql** | [**List[str]**](str.md)| [Filter Group by display_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_eql** | [**List[str]**](str.md)| [Filter Group by display_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_prefix** | [**List[str]**](str.md)| [Filter Group by display_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_prefix** | [**List[str]**](str.md)| [Filter Group by display_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_suffix** | [**List[str]**](str.md)| [Filter Group by display_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_suffix** | [**List[str]**](str.md)| [Filter Group by display_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_match** | [**List[str]**](str.md)| [Filter Group by display_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_display_name_not_match** | [**List[str]**](str.md)| [Filter Group by display_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_eq** | [**List[str]**](str.md)| [Filter Group by description using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_eq** | [**List[str]**](str.md)| [Filter Group by description using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_eql** | [**List[str]**](str.md)| [Filter Group by description using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_eql** | [**List[str]**](str.md)| [Filter Group by description using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_prefix** | [**List[str]**](str.md)| [Filter Group by description using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_prefix** | [**List[str]**](str.md)| [Filter Group by description using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_suffix** | [**List[str]**](str.md)| [Filter Group by description using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_suffix** | [**List[str]**](str.md)| [Filter Group by description using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_match** | [**List[str]**](str.md)| [Filter Group by description using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_description_not_match** | [**List[str]**](str.md)| [Filter Group by description using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_eq** | **bool**| [Filter Group by layer using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_eq** | [**List[int]**](int.md)| [Filter Group by parent_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_not_eq** | [**List[int]**](int.md)| [Filter Group by parent_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_gt** | [**List[int]**](int.md)| [Filter Group by parent_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_gte** | [**List[int]**](int.md)| [Filter Group by parent_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_lt** | [**List[int]**](int.md)| [Filter Group by parent_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_parent_id_lte** | [**List[int]**](int.md)| [Filter Group by parent_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_eq** | [**List[int]**](int.md)| [Filter Group by layer_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_not_eq** | [**List[int]**](int.md)| [Filter Group by layer_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_gt** | [**List[int]**](int.md)| [Filter Group by layer_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_gte** | [**List[int]**](int.md)| [Filter Group by layer_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_lt** | [**List[int]**](int.md)| [Filter Group by layer_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_layer_group_id_lte** | [**List[int]**](int.md)| [Filter Group by layer_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Group by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Group by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Group by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Group by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Group by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Group by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Group by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Group by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Group by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Group by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eq** | [**List[str]**](str.md)| [Filter Group by email using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eq** | [**List[str]**](str.md)| [Filter Group by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eql** | [**List[str]**](str.md)| [Filter Group by email using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eql** | [**List[str]**](str.md)| [Filter Group by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_prefix** | [**List[str]**](str.md)| [Filter Group by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_prefix** | [**List[str]**](str.md)| [Filter Group by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_suffix** | [**List[str]**](str.md)| [Filter Group by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_suffix** | [**List[str]**](str.md)| [Filter Group by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_match** | [**List[str]**](str.md)| [Filter Group by email using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_match** | [**List[str]**](str.md)| [Filter Group by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eq** | [**List[str]**](str.md)| [Filter Group by address using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eq** | [**List[str]**](str.md)| [Filter Group by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eql** | [**List[str]**](str.md)| [Filter Group by address using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eql** | [**List[str]**](str.md)| [Filter Group by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_prefix** | [**List[str]**](str.md)| [Filter Group by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_prefix** | [**List[str]**](str.md)| [Filter Group by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_suffix** | [**List[str]**](str.md)| [Filter Group by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_suffix** | [**List[str]**](str.md)| [Filter Group by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_match** | [**List[str]**](str.md)| [Filter Group by address using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_match** | [**List[str]**](str.md)| [Filter Group by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eq** | [**List[int]**](int.md)| [Filter Group by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eq** | [**List[int]**](int.md)| [Filter Group by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_gt** | [**List[int]**](int.md)| [Filter Group by zip_code using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_gte** | [**List[int]**](int.md)| [Filter Group by zip_code using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_lt** | [**List[int]**](int.md)| [Filter Group by zip_code using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_lte** | [**List[int]**](int.md)| [Filter Group by zip_code using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eq** | [**List[str]**](str.md)| [Filter Group by town using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eq** | [**List[str]**](str.md)| [Filter Group by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eql** | [**List[str]**](str.md)| [Filter Group by town using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eql** | [**List[str]**](str.md)| [Filter Group by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_prefix** | [**List[str]**](str.md)| [Filter Group by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_prefix** | [**List[str]**](str.md)| [Filter Group by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_suffix** | [**List[str]**](str.md)| [Filter Group by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_suffix** | [**List[str]**](str.md)| [Filter Group by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_match** | [**List[str]**](str.md)| [Filter Group by town using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_match** | [**List[str]**](str.md)| [Filter Group by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eq** | [**List[str]**](str.md)| [Filter Group by country using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eq** | [**List[str]**](str.md)| [Filter Group by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eql** | [**List[str]**](str.md)| [Filter Group by country using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eql** | [**List[str]**](str.md)| [Filter Group by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_prefix** | [**List[str]**](str.md)| [Filter Group by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_prefix** | [**List[str]**](str.md)| [Filter Group by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_suffix** | [**List[str]**](str.md)| [Filter Group by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_suffix** | [**List[str]**](str.md)| [Filter Group by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_match** | [**List[str]**](str.md)| [Filter Group by country using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_match** | [**List[str]**](str.md)| [Filter Group by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_require_person_add_requests_eq** | **bool**| [Filter Group by require_person_add_requests using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_eq** | [**List[str]**](str.md)| [Filter Group by self_registration_url using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_eq** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_eql** | [**List[str]**](str.md)| [Filter Group by self_registration_url using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_eql** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_prefix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_prefix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_suffix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_suffix** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_match** | [**List[str]**](str.md)| [Filter Group by self_registration_url using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_self_registration_url_not_match** | [**List[str]**](str.md)| [Filter Group by self_registration_url using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_archived_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by archived_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_eq** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_gt** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_gte** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_lt** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_deleted_at_lte** | [**List[datetime]**](datetime.md)| [Filter Group by deleted_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_with_deleted_eq** | **bool**| [Filter Group by with_deleted using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_with_archived_eq** | **bool**| [Filter Group by with_archived using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_phone_numbers** | [**List[PhoneNumbersReadableAttribute]**](PhoneNumbersReadableAttribute.md)| [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_social_accounts** | [**List[SocialAccountsReadableAttribute]**](SocialAccountsReadableAttribute.md)| [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_additional_emails** | [**List[AdditionalEmailsReadableAttribute]**](AdditionalEmailsReadableAttribute.md)| [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**GroupsCollection**](GroupsCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Groups collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

