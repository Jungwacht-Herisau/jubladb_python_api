# jubladb_api.PeopleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_person**](PeopleApi.md#get_person) | **GET** /api/people/{id} | Fetch Person
[**list_people**](PeopleApi.md#list_people) | **GET** /api/people | List People
[**update_person**](PeopleApi.md#update_person) | **PUT** /api/people/{id} | Update Person


# **get_person**
> PeopleSingle get_person(id, include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)

Fetch Person

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.people_single import PeopleSingle
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
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
    api_instance = jubladb_api.PeopleApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eq = ['filter_first_name_eq_example'] # List[str] | [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eq = ['filter_first_name_not_eq_example'] # List[str] | [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eql = ['filter_first_name_eql_example'] # List[str] | [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eql = ['filter_first_name_not_eql_example'] # List[str] | [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_prefix = ['filter_first_name_prefix_example'] # List[str] | [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_prefix = ['filter_first_name_not_prefix_example'] # List[str] | [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_suffix = ['filter_first_name_suffix_example'] # List[str] | [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_suffix = ['filter_first_name_not_suffix_example'] # List[str] | [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_match = ['filter_first_name_match_example'] # List[str] | [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_match = ['filter_first_name_not_match_example'] # List[str] | [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eq = ['filter_last_name_eq_example'] # List[str] | [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eq = ['filter_last_name_not_eq_example'] # List[str] | [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eql = ['filter_last_name_eql_example'] # List[str] | [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eql = ['filter_last_name_not_eql_example'] # List[str] | [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_prefix = ['filter_last_name_prefix_example'] # List[str] | [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_prefix = ['filter_last_name_not_prefix_example'] # List[str] | [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_suffix = ['filter_last_name_suffix_example'] # List[str] | [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_suffix = ['filter_last_name_not_suffix_example'] # List[str] | [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_match = ['filter_last_name_match_example'] # List[str] | [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_match = ['filter_last_name_not_match_example'] # List[str] | [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eq = ['filter_nickname_eq_example'] # List[str] | [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eq = ['filter_nickname_not_eq_example'] # List[str] | [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eql = ['filter_nickname_eql_example'] # List[str] | [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eql = ['filter_nickname_not_eql_example'] # List[str] | [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_prefix = ['filter_nickname_prefix_example'] # List[str] | [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_prefix = ['filter_nickname_not_prefix_example'] # List[str] | [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_suffix = ['filter_nickname_suffix_example'] # List[str] | [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_suffix = ['filter_nickname_not_suffix_example'] # List[str] | [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_match = ['filter_nickname_match_example'] # List[str] | [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_match = ['filter_nickname_not_match_example'] # List[str] | [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eq = ['filter_company_name_eq_example'] # List[str] | [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eq = ['filter_company_name_not_eq_example'] # List[str] | [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eql = ['filter_company_name_eql_example'] # List[str] | [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eql = ['filter_company_name_not_eql_example'] # List[str] | [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_prefix = ['filter_company_name_prefix_example'] # List[str] | [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_prefix = ['filter_company_name_not_prefix_example'] # List[str] | [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_suffix = ['filter_company_name_suffix_example'] # List[str] | [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_suffix = ['filter_company_name_not_suffix_example'] # List[str] | [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_match = ['filter_company_name_match_example'] # List[str] | [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_match = ['filter_company_name_not_match_example'] # List[str] | [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_eq = True # bool | [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eq = ['filter_email_eq_example'] # List[str] | [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eq = ['filter_email_not_eq_example'] # List[str] | [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eql = ['filter_email_eql_example'] # List[str] | [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eql = ['filter_email_not_eql_example'] # List[str] | [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_prefix = ['filter_email_prefix_example'] # List[str] | [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_prefix = ['filter_email_not_prefix_example'] # List[str] | [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_suffix = ['filter_email_suffix_example'] # List[str] | [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_suffix = ['filter_email_not_suffix_example'] # List[str] | [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_match = ['filter_email_match_example'] # List[str] | [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_match = ['filter_email_not_match_example'] # List[str] | [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eq = ['filter_address_eq_example'] # List[str] | [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eq = ['filter_address_not_eq_example'] # List[str] | [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eql = ['filter_address_eql_example'] # List[str] | [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eql = ['filter_address_not_eql_example'] # List[str] | [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_prefix = ['filter_address_prefix_example'] # List[str] | [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_prefix = ['filter_address_not_prefix_example'] # List[str] | [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_suffix = ['filter_address_suffix_example'] # List[str] | [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_suffix = ['filter_address_not_suffix_example'] # List[str] | [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_match = ['filter_address_match_example'] # List[str] | [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_match = ['filter_address_not_match_example'] # List[str] | [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eq = ['filter_zip_code_eq_example'] # List[str] | [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eq = ['filter_zip_code_not_eq_example'] # List[str] | [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eql = ['filter_zip_code_eql_example'] # List[str] | [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eql = ['filter_zip_code_not_eql_example'] # List[str] | [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_prefix = ['filter_zip_code_prefix_example'] # List[str] | [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_prefix = ['filter_zip_code_not_prefix_example'] # List[str] | [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_suffix = ['filter_zip_code_suffix_example'] # List[str] | [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_suffix = ['filter_zip_code_not_suffix_example'] # List[str] | [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_match = ['filter_zip_code_match_example'] # List[str] | [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_match = ['filter_zip_code_not_match_example'] # List[str] | [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eq = ['filter_town_eq_example'] # List[str] | [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eq = ['filter_town_not_eq_example'] # List[str] | [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eql = ['filter_town_eql_example'] # List[str] | [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eql = ['filter_town_not_eql_example'] # List[str] | [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_prefix = ['filter_town_prefix_example'] # List[str] | [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_prefix = ['filter_town_not_prefix_example'] # List[str] | [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_suffix = ['filter_town_suffix_example'] # List[str] | [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_suffix = ['filter_town_not_suffix_example'] # List[str] | [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_match = ['filter_town_match_example'] # List[str] | [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_match = ['filter_town_not_match_example'] # List[str] | [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eq = ['filter_country_eq_example'] # List[str] | [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eq = ['filter_country_not_eq_example'] # List[str] | [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eql = ['filter_country_eql_example'] # List[str] | [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eql = ['filter_country_not_eql_example'] # List[str] | [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_prefix = ['filter_country_prefix_example'] # List[str] | [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_prefix = ['filter_country_not_prefix_example'] # List[str] | [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_suffix = ['filter_country_suffix_example'] # List[str] | [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_suffix = ['filter_country_not_suffix_example'] # List[str] | [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_match = ['filter_country_match_example'] # List[str] | [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_match = ['filter_country_not_match_example'] # List[str] | [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_eq = [56] # List[int] | [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_not_eq = [56] # List[int] | [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gt = [56] # List[int] | [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gte = [56] # List[int] | [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lt = [56] # List[int] | [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lte = [56] # List[int] | [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eq = ['filter_gender_eq_example'] # List[str] | [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eq = ['filter_gender_not_eq_example'] # List[str] | [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eql = ['filter_gender_eql_example'] # List[str] | [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eql = ['filter_gender_not_eql_example'] # List[str] | [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_prefix = ['filter_gender_prefix_example'] # List[str] | [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_prefix = ['filter_gender_not_prefix_example'] # List[str] | [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_suffix = ['filter_gender_suffix_example'] # List[str] | [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_suffix = ['filter_gender_not_suffix_example'] # List[str] | [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_match = ['filter_gender_match_example'] # List[str] | [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_match = ['filter_gender_not_match_example'] # List[str] | [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_not_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gt = ['2013-10-20'] # List[date] | [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gte = ['2013-10-20'] # List[date] | [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lt = ['2013-10-20'] # List[date] | [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lte = ['2013-10-20'] # List[date] | [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eq = ['filter_language_eq_example'] # List[str] | [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eq = ['filter_language_not_eq_example'] # List[str] | [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eql = ['filter_language_eql_example'] # List[str] | [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eql = ['filter_language_not_eql_example'] # List[str] | [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_prefix = ['filter_language_prefix_example'] # List[str] | [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_prefix = ['filter_language_not_prefix_example'] # List[str] | [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_suffix = ['filter_language_suffix_example'] # List[str] | [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_suffix = ['filter_language_not_suffix_example'] # List[str] | [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_match = ['filter_language_match_example'] # List[str] | [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_match = ['filter_language_not_match_example'] # List[str] | [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_phone_numbers = [jubladb_api.PhoneNumbersReadableAttribute()] # List[PhoneNumbersReadableAttribute] | [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_social_accounts = [jubladb_api.SocialAccountsReadableAttribute()] # List[SocialAccountsReadableAttribute] | [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_additional_emails = [jubladb_api.AdditionalEmailsReadableAttribute()] # List[AdditionalEmailsReadableAttribute] | [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Person
        api_response = api_instance.get_person(id, include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)
        print("The response of PeopleApi->get_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->get_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eq** | [**List[str]**](str.md)| [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eq** | [**List[str]**](str.md)| [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eql** | [**List[str]**](str.md)| [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eql** | [**List[str]**](str.md)| [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_match** | [**List[str]**](str.md)| [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_match** | [**List[str]**](str.md)| [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eq** | [**List[str]**](str.md)| [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eq** | [**List[str]**](str.md)| [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eql** | [**List[str]**](str.md)| [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eql** | [**List[str]**](str.md)| [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_match** | [**List[str]**](str.md)| [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_match** | [**List[str]**](str.md)| [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eq** | [**List[str]**](str.md)| [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eq** | [**List[str]**](str.md)| [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eql** | [**List[str]**](str.md)| [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eql** | [**List[str]**](str.md)| [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_match** | [**List[str]**](str.md)| [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_match** | [**List[str]**](str.md)| [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eq** | [**List[str]**](str.md)| [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eq** | [**List[str]**](str.md)| [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eql** | [**List[str]**](str.md)| [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eql** | [**List[str]**](str.md)| [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_match** | [**List[str]**](str.md)| [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_match** | [**List[str]**](str.md)| [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_eq** | **bool**| [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eq** | [**List[str]**](str.md)| [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eq** | [**List[str]**](str.md)| [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eql** | [**List[str]**](str.md)| [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eql** | [**List[str]**](str.md)| [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_prefix** | [**List[str]**](str.md)| [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_prefix** | [**List[str]**](str.md)| [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_suffix** | [**List[str]**](str.md)| [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_suffix** | [**List[str]**](str.md)| [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_match** | [**List[str]**](str.md)| [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_match** | [**List[str]**](str.md)| [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eq** | [**List[str]**](str.md)| [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eq** | [**List[str]**](str.md)| [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eql** | [**List[str]**](str.md)| [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eql** | [**List[str]**](str.md)| [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_prefix** | [**List[str]**](str.md)| [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_prefix** | [**List[str]**](str.md)| [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_suffix** | [**List[str]**](str.md)| [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_suffix** | [**List[str]**](str.md)| [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_match** | [**List[str]**](str.md)| [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_match** | [**List[str]**](str.md)| [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_match** | [**List[str]**](str.md)| [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_match** | [**List[str]**](str.md)| [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eq** | [**List[str]**](str.md)| [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eq** | [**List[str]**](str.md)| [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eql** | [**List[str]**](str.md)| [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eql** | [**List[str]**](str.md)| [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_prefix** | [**List[str]**](str.md)| [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_prefix** | [**List[str]**](str.md)| [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_suffix** | [**List[str]**](str.md)| [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_suffix** | [**List[str]**](str.md)| [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_match** | [**List[str]**](str.md)| [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_match** | [**List[str]**](str.md)| [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eq** | [**List[str]**](str.md)| [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eq** | [**List[str]**](str.md)| [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eql** | [**List[str]**](str.md)| [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eql** | [**List[str]**](str.md)| [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_prefix** | [**List[str]**](str.md)| [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_prefix** | [**List[str]**](str.md)| [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_suffix** | [**List[str]**](str.md)| [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_suffix** | [**List[str]**](str.md)| [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_match** | [**List[str]**](str.md)| [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_match** | [**List[str]**](str.md)| [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_not_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eq** | [**List[str]**](str.md)| [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eq** | [**List[str]**](str.md)| [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eql** | [**List[str]**](str.md)| [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eql** | [**List[str]**](str.md)| [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_prefix** | [**List[str]**](str.md)| [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_prefix** | [**List[str]**](str.md)| [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_suffix** | [**List[str]**](str.md)| [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_suffix** | [**List[str]**](str.md)| [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_match** | [**List[str]**](str.md)| [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_match** | [**List[str]**](str.md)| [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_eq** | [**List[date]**](date.md)| [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_not_eq** | [**List[date]**](date.md)| [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gt** | [**List[date]**](date.md)| [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gte** | [**List[date]**](date.md)| [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lt** | [**List[date]**](date.md)| [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lte** | [**List[date]**](date.md)| [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eq** | [**List[str]**](str.md)| [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eq** | [**List[str]**](str.md)| [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eql** | [**List[str]**](str.md)| [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eql** | [**List[str]**](str.md)| [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_prefix** | [**List[str]**](str.md)| [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_prefix** | [**List[str]**](str.md)| [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_suffix** | [**List[str]**](str.md)| [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_suffix** | [**List[str]**](str.md)| [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_match** | [**List[str]**](str.md)| [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_match** | [**List[str]**](str.md)| [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_phone_numbers** | [**List[PhoneNumbersReadableAttribute]**](PhoneNumbersReadableAttribute.md)| [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_social_accounts** | [**List[SocialAccountsReadableAttribute]**](SocialAccountsReadableAttribute.md)| [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_additional_emails** | [**List[AdditionalEmailsReadableAttribute]**](AdditionalEmailsReadableAttribute.md)| [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**PeopleSingle**](PeopleSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Person resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_people**
> PeopleCollection list_people(include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)

List People

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_collection import PeopleCollection
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
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
    api_instance = jubladb_api.PeopleApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eq = ['filter_first_name_eq_example'] # List[str] | [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eq = ['filter_first_name_not_eq_example'] # List[str] | [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eql = ['filter_first_name_eql_example'] # List[str] | [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eql = ['filter_first_name_not_eql_example'] # List[str] | [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_prefix = ['filter_first_name_prefix_example'] # List[str] | [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_prefix = ['filter_first_name_not_prefix_example'] # List[str] | [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_suffix = ['filter_first_name_suffix_example'] # List[str] | [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_suffix = ['filter_first_name_not_suffix_example'] # List[str] | [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_match = ['filter_first_name_match_example'] # List[str] | [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_match = ['filter_first_name_not_match_example'] # List[str] | [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eq = ['filter_last_name_eq_example'] # List[str] | [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eq = ['filter_last_name_not_eq_example'] # List[str] | [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eql = ['filter_last_name_eql_example'] # List[str] | [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eql = ['filter_last_name_not_eql_example'] # List[str] | [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_prefix = ['filter_last_name_prefix_example'] # List[str] | [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_prefix = ['filter_last_name_not_prefix_example'] # List[str] | [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_suffix = ['filter_last_name_suffix_example'] # List[str] | [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_suffix = ['filter_last_name_not_suffix_example'] # List[str] | [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_match = ['filter_last_name_match_example'] # List[str] | [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_match = ['filter_last_name_not_match_example'] # List[str] | [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eq = ['filter_nickname_eq_example'] # List[str] | [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eq = ['filter_nickname_not_eq_example'] # List[str] | [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eql = ['filter_nickname_eql_example'] # List[str] | [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eql = ['filter_nickname_not_eql_example'] # List[str] | [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_prefix = ['filter_nickname_prefix_example'] # List[str] | [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_prefix = ['filter_nickname_not_prefix_example'] # List[str] | [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_suffix = ['filter_nickname_suffix_example'] # List[str] | [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_suffix = ['filter_nickname_not_suffix_example'] # List[str] | [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_match = ['filter_nickname_match_example'] # List[str] | [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_match = ['filter_nickname_not_match_example'] # List[str] | [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eq = ['filter_company_name_eq_example'] # List[str] | [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eq = ['filter_company_name_not_eq_example'] # List[str] | [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eql = ['filter_company_name_eql_example'] # List[str] | [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eql = ['filter_company_name_not_eql_example'] # List[str] | [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_prefix = ['filter_company_name_prefix_example'] # List[str] | [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_prefix = ['filter_company_name_not_prefix_example'] # List[str] | [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_suffix = ['filter_company_name_suffix_example'] # List[str] | [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_suffix = ['filter_company_name_not_suffix_example'] # List[str] | [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_match = ['filter_company_name_match_example'] # List[str] | [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_match = ['filter_company_name_not_match_example'] # List[str] | [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_eq = True # bool | [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eq = ['filter_email_eq_example'] # List[str] | [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eq = ['filter_email_not_eq_example'] # List[str] | [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eql = ['filter_email_eql_example'] # List[str] | [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eql = ['filter_email_not_eql_example'] # List[str] | [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_prefix = ['filter_email_prefix_example'] # List[str] | [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_prefix = ['filter_email_not_prefix_example'] # List[str] | [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_suffix = ['filter_email_suffix_example'] # List[str] | [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_suffix = ['filter_email_not_suffix_example'] # List[str] | [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_match = ['filter_email_match_example'] # List[str] | [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_match = ['filter_email_not_match_example'] # List[str] | [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eq = ['filter_address_eq_example'] # List[str] | [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eq = ['filter_address_not_eq_example'] # List[str] | [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eql = ['filter_address_eql_example'] # List[str] | [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eql = ['filter_address_not_eql_example'] # List[str] | [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_prefix = ['filter_address_prefix_example'] # List[str] | [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_prefix = ['filter_address_not_prefix_example'] # List[str] | [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_suffix = ['filter_address_suffix_example'] # List[str] | [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_suffix = ['filter_address_not_suffix_example'] # List[str] | [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_match = ['filter_address_match_example'] # List[str] | [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_match = ['filter_address_not_match_example'] # List[str] | [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eq = ['filter_zip_code_eq_example'] # List[str] | [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eq = ['filter_zip_code_not_eq_example'] # List[str] | [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eql = ['filter_zip_code_eql_example'] # List[str] | [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eql = ['filter_zip_code_not_eql_example'] # List[str] | [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_prefix = ['filter_zip_code_prefix_example'] # List[str] | [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_prefix = ['filter_zip_code_not_prefix_example'] # List[str] | [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_suffix = ['filter_zip_code_suffix_example'] # List[str] | [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_suffix = ['filter_zip_code_not_suffix_example'] # List[str] | [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_match = ['filter_zip_code_match_example'] # List[str] | [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_match = ['filter_zip_code_not_match_example'] # List[str] | [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eq = ['filter_town_eq_example'] # List[str] | [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eq = ['filter_town_not_eq_example'] # List[str] | [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eql = ['filter_town_eql_example'] # List[str] | [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eql = ['filter_town_not_eql_example'] # List[str] | [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_prefix = ['filter_town_prefix_example'] # List[str] | [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_prefix = ['filter_town_not_prefix_example'] # List[str] | [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_suffix = ['filter_town_suffix_example'] # List[str] | [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_suffix = ['filter_town_not_suffix_example'] # List[str] | [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_match = ['filter_town_match_example'] # List[str] | [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_match = ['filter_town_not_match_example'] # List[str] | [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eq = ['filter_country_eq_example'] # List[str] | [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eq = ['filter_country_not_eq_example'] # List[str] | [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eql = ['filter_country_eql_example'] # List[str] | [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eql = ['filter_country_not_eql_example'] # List[str] | [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_prefix = ['filter_country_prefix_example'] # List[str] | [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_prefix = ['filter_country_not_prefix_example'] # List[str] | [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_suffix = ['filter_country_suffix_example'] # List[str] | [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_suffix = ['filter_country_not_suffix_example'] # List[str] | [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_match = ['filter_country_match_example'] # List[str] | [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_match = ['filter_country_not_match_example'] # List[str] | [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_eq = [56] # List[int] | [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_not_eq = [56] # List[int] | [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gt = [56] # List[int] | [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gte = [56] # List[int] | [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lt = [56] # List[int] | [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lte = [56] # List[int] | [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eq = ['filter_gender_eq_example'] # List[str] | [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eq = ['filter_gender_not_eq_example'] # List[str] | [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eql = ['filter_gender_eql_example'] # List[str] | [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eql = ['filter_gender_not_eql_example'] # List[str] | [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_prefix = ['filter_gender_prefix_example'] # List[str] | [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_prefix = ['filter_gender_not_prefix_example'] # List[str] | [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_suffix = ['filter_gender_suffix_example'] # List[str] | [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_suffix = ['filter_gender_not_suffix_example'] # List[str] | [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_match = ['filter_gender_match_example'] # List[str] | [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_match = ['filter_gender_not_match_example'] # List[str] | [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_not_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gt = ['2013-10-20'] # List[date] | [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gte = ['2013-10-20'] # List[date] | [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lt = ['2013-10-20'] # List[date] | [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lte = ['2013-10-20'] # List[date] | [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eq = ['filter_language_eq_example'] # List[str] | [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eq = ['filter_language_not_eq_example'] # List[str] | [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eql = ['filter_language_eql_example'] # List[str] | [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eql = ['filter_language_not_eql_example'] # List[str] | [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_prefix = ['filter_language_prefix_example'] # List[str] | [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_prefix = ['filter_language_not_prefix_example'] # List[str] | [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_suffix = ['filter_language_suffix_example'] # List[str] | [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_suffix = ['filter_language_not_suffix_example'] # List[str] | [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_match = ['filter_language_match_example'] # List[str] | [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_match = ['filter_language_not_match_example'] # List[str] | [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_phone_numbers = [jubladb_api.PhoneNumbersReadableAttribute()] # List[PhoneNumbersReadableAttribute] | [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_social_accounts = [jubladb_api.SocialAccountsReadableAttribute()] # List[SocialAccountsReadableAttribute] | [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_additional_emails = [jubladb_api.AdditionalEmailsReadableAttribute()] # List[AdditionalEmailsReadableAttribute] | [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List People
        api_response = api_instance.list_people(include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)
        print("The response of PeopleApi->list_people:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->list_people: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eq** | [**List[str]**](str.md)| [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eq** | [**List[str]**](str.md)| [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eql** | [**List[str]**](str.md)| [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eql** | [**List[str]**](str.md)| [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_match** | [**List[str]**](str.md)| [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_match** | [**List[str]**](str.md)| [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eq** | [**List[str]**](str.md)| [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eq** | [**List[str]**](str.md)| [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eql** | [**List[str]**](str.md)| [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eql** | [**List[str]**](str.md)| [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_match** | [**List[str]**](str.md)| [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_match** | [**List[str]**](str.md)| [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eq** | [**List[str]**](str.md)| [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eq** | [**List[str]**](str.md)| [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eql** | [**List[str]**](str.md)| [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eql** | [**List[str]**](str.md)| [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_match** | [**List[str]**](str.md)| [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_match** | [**List[str]**](str.md)| [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eq** | [**List[str]**](str.md)| [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eq** | [**List[str]**](str.md)| [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eql** | [**List[str]**](str.md)| [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eql** | [**List[str]**](str.md)| [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_match** | [**List[str]**](str.md)| [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_match** | [**List[str]**](str.md)| [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_eq** | **bool**| [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eq** | [**List[str]**](str.md)| [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eq** | [**List[str]**](str.md)| [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eql** | [**List[str]**](str.md)| [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eql** | [**List[str]**](str.md)| [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_prefix** | [**List[str]**](str.md)| [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_prefix** | [**List[str]**](str.md)| [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_suffix** | [**List[str]**](str.md)| [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_suffix** | [**List[str]**](str.md)| [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_match** | [**List[str]**](str.md)| [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_match** | [**List[str]**](str.md)| [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eq** | [**List[str]**](str.md)| [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eq** | [**List[str]**](str.md)| [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eql** | [**List[str]**](str.md)| [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eql** | [**List[str]**](str.md)| [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_prefix** | [**List[str]**](str.md)| [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_prefix** | [**List[str]**](str.md)| [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_suffix** | [**List[str]**](str.md)| [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_suffix** | [**List[str]**](str.md)| [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_match** | [**List[str]**](str.md)| [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_match** | [**List[str]**](str.md)| [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_match** | [**List[str]**](str.md)| [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_match** | [**List[str]**](str.md)| [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eq** | [**List[str]**](str.md)| [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eq** | [**List[str]**](str.md)| [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eql** | [**List[str]**](str.md)| [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eql** | [**List[str]**](str.md)| [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_prefix** | [**List[str]**](str.md)| [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_prefix** | [**List[str]**](str.md)| [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_suffix** | [**List[str]**](str.md)| [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_suffix** | [**List[str]**](str.md)| [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_match** | [**List[str]**](str.md)| [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_match** | [**List[str]**](str.md)| [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eq** | [**List[str]**](str.md)| [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eq** | [**List[str]**](str.md)| [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eql** | [**List[str]**](str.md)| [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eql** | [**List[str]**](str.md)| [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_prefix** | [**List[str]**](str.md)| [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_prefix** | [**List[str]**](str.md)| [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_suffix** | [**List[str]**](str.md)| [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_suffix** | [**List[str]**](str.md)| [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_match** | [**List[str]**](str.md)| [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_match** | [**List[str]**](str.md)| [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_not_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eq** | [**List[str]**](str.md)| [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eq** | [**List[str]**](str.md)| [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eql** | [**List[str]**](str.md)| [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eql** | [**List[str]**](str.md)| [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_prefix** | [**List[str]**](str.md)| [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_prefix** | [**List[str]**](str.md)| [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_suffix** | [**List[str]**](str.md)| [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_suffix** | [**List[str]**](str.md)| [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_match** | [**List[str]**](str.md)| [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_match** | [**List[str]**](str.md)| [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_eq** | [**List[date]**](date.md)| [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_not_eq** | [**List[date]**](date.md)| [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gt** | [**List[date]**](date.md)| [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gte** | [**List[date]**](date.md)| [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lt** | [**List[date]**](date.md)| [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lte** | [**List[date]**](date.md)| [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eq** | [**List[str]**](str.md)| [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eq** | [**List[str]**](str.md)| [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eql** | [**List[str]**](str.md)| [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eql** | [**List[str]**](str.md)| [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_prefix** | [**List[str]**](str.md)| [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_prefix** | [**List[str]**](str.md)| [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_suffix** | [**List[str]**](str.md)| [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_suffix** | [**List[str]**](str.md)| [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_match** | [**List[str]**](str.md)| [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_match** | [**List[str]**](str.md)| [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_phone_numbers** | [**List[PhoneNumbersReadableAttribute]**](PhoneNumbersReadableAttribute.md)| [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_social_accounts** | [**List[SocialAccountsReadableAttribute]**](SocialAccountsReadableAttribute.md)| [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_additional_emails** | [**List[AdditionalEmailsReadableAttribute]**](AdditionalEmailsReadableAttribute.md)| [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**PeopleCollection**](PeopleCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: People collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_person**
> PeopleSingle update_person(id, people_request, include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)

Update Person

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.additional_emails_readable_attribute import AdditionalEmailsReadableAttribute
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.people_request import PeopleRequest
from jubladb_api.models.people_single import PeopleSingle
from jubladb_api.models.phone_numbers_readable_attribute import PhoneNumbersReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
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
    api_instance = jubladb_api.PeopleApi(api_client)
    id = 'id_example' # str | ID of the resource
    people_request = jubladb_api.PeopleRequest() # PeopleRequest | 
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eq = ['filter_first_name_eq_example'] # List[str] | [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eq = ['filter_first_name_not_eq_example'] # List[str] | [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_eql = ['filter_first_name_eql_example'] # List[str] | [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_eql = ['filter_first_name_not_eql_example'] # List[str] | [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_prefix = ['filter_first_name_prefix_example'] # List[str] | [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_prefix = ['filter_first_name_not_prefix_example'] # List[str] | [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_suffix = ['filter_first_name_suffix_example'] # List[str] | [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_suffix = ['filter_first_name_not_suffix_example'] # List[str] | [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_match = ['filter_first_name_match_example'] # List[str] | [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_first_name_not_match = ['filter_first_name_not_match_example'] # List[str] | [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eq = ['filter_last_name_eq_example'] # List[str] | [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eq = ['filter_last_name_not_eq_example'] # List[str] | [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_eql = ['filter_last_name_eql_example'] # List[str] | [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_eql = ['filter_last_name_not_eql_example'] # List[str] | [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_prefix = ['filter_last_name_prefix_example'] # List[str] | [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_prefix = ['filter_last_name_not_prefix_example'] # List[str] | [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_suffix = ['filter_last_name_suffix_example'] # List[str] | [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_suffix = ['filter_last_name_not_suffix_example'] # List[str] | [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_match = ['filter_last_name_match_example'] # List[str] | [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_last_name_not_match = ['filter_last_name_not_match_example'] # List[str] | [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eq = ['filter_nickname_eq_example'] # List[str] | [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eq = ['filter_nickname_not_eq_example'] # List[str] | [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_eql = ['filter_nickname_eql_example'] # List[str] | [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_eql = ['filter_nickname_not_eql_example'] # List[str] | [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_prefix = ['filter_nickname_prefix_example'] # List[str] | [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_prefix = ['filter_nickname_not_prefix_example'] # List[str] | [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_suffix = ['filter_nickname_suffix_example'] # List[str] | [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_suffix = ['filter_nickname_not_suffix_example'] # List[str] | [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_match = ['filter_nickname_match_example'] # List[str] | [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_nickname_not_match = ['filter_nickname_not_match_example'] # List[str] | [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eq = ['filter_company_name_eq_example'] # List[str] | [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eq = ['filter_company_name_not_eq_example'] # List[str] | [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_eql = ['filter_company_name_eql_example'] # List[str] | [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_eql = ['filter_company_name_not_eql_example'] # List[str] | [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_prefix = ['filter_company_name_prefix_example'] # List[str] | [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_prefix = ['filter_company_name_not_prefix_example'] # List[str] | [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_suffix = ['filter_company_name_suffix_example'] # List[str] | [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_suffix = ['filter_company_name_not_suffix_example'] # List[str] | [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_match = ['filter_company_name_match_example'] # List[str] | [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_name_not_match = ['filter_company_name_not_match_example'] # List[str] | [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_company_eq = True # bool | [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eq = ['filter_email_eq_example'] # List[str] | [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eq = ['filter_email_not_eq_example'] # List[str] | [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_eql = ['filter_email_eql_example'] # List[str] | [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_eql = ['filter_email_not_eql_example'] # List[str] | [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_prefix = ['filter_email_prefix_example'] # List[str] | [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_prefix = ['filter_email_not_prefix_example'] # List[str] | [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_suffix = ['filter_email_suffix_example'] # List[str] | [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_suffix = ['filter_email_not_suffix_example'] # List[str] | [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_match = ['filter_email_match_example'] # List[str] | [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_email_not_match = ['filter_email_not_match_example'] # List[str] | [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eq = ['filter_address_eq_example'] # List[str] | [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eq = ['filter_address_not_eq_example'] # List[str] | [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_eql = ['filter_address_eql_example'] # List[str] | [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_eql = ['filter_address_not_eql_example'] # List[str] | [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_prefix = ['filter_address_prefix_example'] # List[str] | [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_prefix = ['filter_address_not_prefix_example'] # List[str] | [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_suffix = ['filter_address_suffix_example'] # List[str] | [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_suffix = ['filter_address_not_suffix_example'] # List[str] | [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_match = ['filter_address_match_example'] # List[str] | [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_address_not_match = ['filter_address_not_match_example'] # List[str] | [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eq = ['filter_zip_code_eq_example'] # List[str] | [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eq = ['filter_zip_code_not_eq_example'] # List[str] | [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_eql = ['filter_zip_code_eql_example'] # List[str] | [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_eql = ['filter_zip_code_not_eql_example'] # List[str] | [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_prefix = ['filter_zip_code_prefix_example'] # List[str] | [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_prefix = ['filter_zip_code_not_prefix_example'] # List[str] | [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_suffix = ['filter_zip_code_suffix_example'] # List[str] | [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_suffix = ['filter_zip_code_not_suffix_example'] # List[str] | [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_match = ['filter_zip_code_match_example'] # List[str] | [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_zip_code_not_match = ['filter_zip_code_not_match_example'] # List[str] | [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eq = ['filter_town_eq_example'] # List[str] | [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eq = ['filter_town_not_eq_example'] # List[str] | [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_eql = ['filter_town_eql_example'] # List[str] | [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_eql = ['filter_town_not_eql_example'] # List[str] | [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_prefix = ['filter_town_prefix_example'] # List[str] | [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_prefix = ['filter_town_not_prefix_example'] # List[str] | [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_suffix = ['filter_town_suffix_example'] # List[str] | [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_suffix = ['filter_town_not_suffix_example'] # List[str] | [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_match = ['filter_town_match_example'] # List[str] | [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_town_not_match = ['filter_town_not_match_example'] # List[str] | [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eq = ['filter_country_eq_example'] # List[str] | [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eq = ['filter_country_not_eq_example'] # List[str] | [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_eql = ['filter_country_eql_example'] # List[str] | [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_eql = ['filter_country_not_eql_example'] # List[str] | [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_prefix = ['filter_country_prefix_example'] # List[str] | [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_prefix = ['filter_country_not_prefix_example'] # List[str] | [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_suffix = ['filter_country_suffix_example'] # List[str] | [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_suffix = ['filter_country_not_suffix_example'] # List[str] | [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_match = ['filter_country_match_example'] # List[str] | [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_country_not_match = ['filter_country_not_match_example'] # List[str] | [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_eq = [56] # List[int] | [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_not_eq = [56] # List[int] | [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gt = [56] # List[int] | [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_gte = [56] # List[int] | [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lt = [56] # List[int] | [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_primary_group_id_lte = [56] # List[int] | [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eq = ['filter_gender_eq_example'] # List[str] | [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eq = ['filter_gender_not_eq_example'] # List[str] | [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_eql = ['filter_gender_eql_example'] # List[str] | [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_eql = ['filter_gender_not_eql_example'] # List[str] | [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_prefix = ['filter_gender_prefix_example'] # List[str] | [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_prefix = ['filter_gender_not_prefix_example'] # List[str] | [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_suffix = ['filter_gender_suffix_example'] # List[str] | [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_suffix = ['filter_gender_not_suffix_example'] # List[str] | [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_match = ['filter_gender_match_example'] # List[str] | [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_gender_not_match = ['filter_gender_not_match_example'] # List[str] | [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_not_eq = ['2013-10-20'] # List[date] | [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gt = ['2013-10-20'] # List[date] | [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_gte = ['2013-10-20'] # List[date] | [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lt = ['2013-10-20'] # List[date] | [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_birthday_lte = ['2013-10-20'] # List[date] | [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eq = ['filter_language_eq_example'] # List[str] | [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eq = ['filter_language_not_eq_example'] # List[str] | [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_eql = ['filter_language_eql_example'] # List[str] | [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_eql = ['filter_language_not_eql_example'] # List[str] | [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_prefix = ['filter_language_prefix_example'] # List[str] | [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_prefix = ['filter_language_not_prefix_example'] # List[str] | [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_suffix = ['filter_language_suffix_example'] # List[str] | [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_suffix = ['filter_language_not_suffix_example'] # List[str] | [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_match = ['filter_language_match_example'] # List[str] | [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_language_not_match = ['filter_language_not_match_example'] # List[str] | [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_phone_numbers = [jubladb_api.PhoneNumbersReadableAttribute()] # List[PhoneNumbersReadableAttribute] | [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_social_accounts = [jubladb_api.SocialAccountsReadableAttribute()] # List[SocialAccountsReadableAttribute] | [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_additional_emails = [jubladb_api.AdditionalEmailsReadableAttribute()] # List[AdditionalEmailsReadableAttribute] | [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Update Person
        api_response = api_instance.update_person(id, people_request, include=include, sort=sort, fields_people=fields_people, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_first_name_eq=filter_first_name_eq, filter_first_name_not_eq=filter_first_name_not_eq, filter_first_name_eql=filter_first_name_eql, filter_first_name_not_eql=filter_first_name_not_eql, filter_first_name_prefix=filter_first_name_prefix, filter_first_name_not_prefix=filter_first_name_not_prefix, filter_first_name_suffix=filter_first_name_suffix, filter_first_name_not_suffix=filter_first_name_not_suffix, filter_first_name_match=filter_first_name_match, filter_first_name_not_match=filter_first_name_not_match, filter_last_name_eq=filter_last_name_eq, filter_last_name_not_eq=filter_last_name_not_eq, filter_last_name_eql=filter_last_name_eql, filter_last_name_not_eql=filter_last_name_not_eql, filter_last_name_prefix=filter_last_name_prefix, filter_last_name_not_prefix=filter_last_name_not_prefix, filter_last_name_suffix=filter_last_name_suffix, filter_last_name_not_suffix=filter_last_name_not_suffix, filter_last_name_match=filter_last_name_match, filter_last_name_not_match=filter_last_name_not_match, filter_nickname_eq=filter_nickname_eq, filter_nickname_not_eq=filter_nickname_not_eq, filter_nickname_eql=filter_nickname_eql, filter_nickname_not_eql=filter_nickname_not_eql, filter_nickname_prefix=filter_nickname_prefix, filter_nickname_not_prefix=filter_nickname_not_prefix, filter_nickname_suffix=filter_nickname_suffix, filter_nickname_not_suffix=filter_nickname_not_suffix, filter_nickname_match=filter_nickname_match, filter_nickname_not_match=filter_nickname_not_match, filter_company_name_eq=filter_company_name_eq, filter_company_name_not_eq=filter_company_name_not_eq, filter_company_name_eql=filter_company_name_eql, filter_company_name_not_eql=filter_company_name_not_eql, filter_company_name_prefix=filter_company_name_prefix, filter_company_name_not_prefix=filter_company_name_not_prefix, filter_company_name_suffix=filter_company_name_suffix, filter_company_name_not_suffix=filter_company_name_not_suffix, filter_company_name_match=filter_company_name_match, filter_company_name_not_match=filter_company_name_not_match, filter_company_eq=filter_company_eq, filter_email_eq=filter_email_eq, filter_email_not_eq=filter_email_not_eq, filter_email_eql=filter_email_eql, filter_email_not_eql=filter_email_not_eql, filter_email_prefix=filter_email_prefix, filter_email_not_prefix=filter_email_not_prefix, filter_email_suffix=filter_email_suffix, filter_email_not_suffix=filter_email_not_suffix, filter_email_match=filter_email_match, filter_email_not_match=filter_email_not_match, filter_address_eq=filter_address_eq, filter_address_not_eq=filter_address_not_eq, filter_address_eql=filter_address_eql, filter_address_not_eql=filter_address_not_eql, filter_address_prefix=filter_address_prefix, filter_address_not_prefix=filter_address_not_prefix, filter_address_suffix=filter_address_suffix, filter_address_not_suffix=filter_address_not_suffix, filter_address_match=filter_address_match, filter_address_not_match=filter_address_not_match, filter_zip_code_eq=filter_zip_code_eq, filter_zip_code_not_eq=filter_zip_code_not_eq, filter_zip_code_eql=filter_zip_code_eql, filter_zip_code_not_eql=filter_zip_code_not_eql, filter_zip_code_prefix=filter_zip_code_prefix, filter_zip_code_not_prefix=filter_zip_code_not_prefix, filter_zip_code_suffix=filter_zip_code_suffix, filter_zip_code_not_suffix=filter_zip_code_not_suffix, filter_zip_code_match=filter_zip_code_match, filter_zip_code_not_match=filter_zip_code_not_match, filter_town_eq=filter_town_eq, filter_town_not_eq=filter_town_not_eq, filter_town_eql=filter_town_eql, filter_town_not_eql=filter_town_not_eql, filter_town_prefix=filter_town_prefix, filter_town_not_prefix=filter_town_not_prefix, filter_town_suffix=filter_town_suffix, filter_town_not_suffix=filter_town_not_suffix, filter_town_match=filter_town_match, filter_town_not_match=filter_town_not_match, filter_country_eq=filter_country_eq, filter_country_not_eq=filter_country_not_eq, filter_country_eql=filter_country_eql, filter_country_not_eql=filter_country_not_eql, filter_country_prefix=filter_country_prefix, filter_country_not_prefix=filter_country_not_prefix, filter_country_suffix=filter_country_suffix, filter_country_not_suffix=filter_country_not_suffix, filter_country_match=filter_country_match, filter_country_not_match=filter_country_not_match, filter_primary_group_id_eq=filter_primary_group_id_eq, filter_primary_group_id_not_eq=filter_primary_group_id_not_eq, filter_primary_group_id_gt=filter_primary_group_id_gt, filter_primary_group_id_gte=filter_primary_group_id_gte, filter_primary_group_id_lt=filter_primary_group_id_lt, filter_primary_group_id_lte=filter_primary_group_id_lte, filter_gender_eq=filter_gender_eq, filter_gender_not_eq=filter_gender_not_eq, filter_gender_eql=filter_gender_eql, filter_gender_not_eql=filter_gender_not_eql, filter_gender_prefix=filter_gender_prefix, filter_gender_not_prefix=filter_gender_not_prefix, filter_gender_suffix=filter_gender_suffix, filter_gender_not_suffix=filter_gender_not_suffix, filter_gender_match=filter_gender_match, filter_gender_not_match=filter_gender_not_match, filter_birthday_eq=filter_birthday_eq, filter_birthday_not_eq=filter_birthday_not_eq, filter_birthday_gt=filter_birthday_gt, filter_birthday_gte=filter_birthday_gte, filter_birthday_lt=filter_birthday_lt, filter_birthday_lte=filter_birthday_lte, filter_language_eq=filter_language_eq, filter_language_not_eq=filter_language_not_eq, filter_language_eql=filter_language_eql, filter_language_not_eql=filter_language_not_eql, filter_language_prefix=filter_language_prefix, filter_language_not_prefix=filter_language_not_prefix, filter_language_suffix=filter_language_suffix, filter_language_not_suffix=filter_language_not_suffix, filter_language_match=filter_language_match, filter_language_not_match=filter_language_not_match, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, fields_groups=fields_groups, fields_roles=fields_roles, fields_phone_numbers=fields_phone_numbers, fields_social_accounts=fields_social_accounts, fields_additional_emails=fields_additional_emails)
        print("The response of PeopleApi->update_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleApi->update_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **people_request** | [**PeopleRequest**](PeopleRequest.md)|  | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort people according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Person by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Person by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Person by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Person by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Person by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Person by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eq** | [**List[str]**](str.md)| [Filter Person by first_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eq** | [**List[str]**](str.md)| [Filter Person by first_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_eql** | [**List[str]**](str.md)| [Filter Person by first_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_eql** | [**List[str]**](str.md)| [Filter Person by first_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by first_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by first_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_match** | [**List[str]**](str.md)| [Filter Person by first_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_first_name_not_match** | [**List[str]**](str.md)| [Filter Person by first_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eq** | [**List[str]**](str.md)| [Filter Person by last_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eq** | [**List[str]**](str.md)| [Filter Person by last_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_eql** | [**List[str]**](str.md)| [Filter Person by last_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_eql** | [**List[str]**](str.md)| [Filter Person by last_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by last_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by last_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_match** | [**List[str]**](str.md)| [Filter Person by last_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_last_name_not_match** | [**List[str]**](str.md)| [Filter Person by last_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eq** | [**List[str]**](str.md)| [Filter Person by nickname using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eq** | [**List[str]**](str.md)| [Filter Person by nickname using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_eql** | [**List[str]**](str.md)| [Filter Person by nickname using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_eql** | [**List[str]**](str.md)| [Filter Person by nickname using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_prefix** | [**List[str]**](str.md)| [Filter Person by nickname using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_suffix** | [**List[str]**](str.md)| [Filter Person by nickname using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_match** | [**List[str]**](str.md)| [Filter Person by nickname using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_nickname_not_match** | [**List[str]**](str.md)| [Filter Person by nickname using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eq** | [**List[str]**](str.md)| [Filter Person by company_name using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eq** | [**List[str]**](str.md)| [Filter Person by company_name using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_eql** | [**List[str]**](str.md)| [Filter Person by company_name using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_eql** | [**List[str]**](str.md)| [Filter Person by company_name using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_prefix** | [**List[str]**](str.md)| [Filter Person by company_name using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_suffix** | [**List[str]**](str.md)| [Filter Person by company_name using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_match** | [**List[str]**](str.md)| [Filter Person by company_name using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_name_not_match** | [**List[str]**](str.md)| [Filter Person by company_name using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_company_eq** | **bool**| [Filter Person by company using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eq** | [**List[str]**](str.md)| [Filter Person by email using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eq** | [**List[str]**](str.md)| [Filter Person by email using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_eql** | [**List[str]**](str.md)| [Filter Person by email using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_eql** | [**List[str]**](str.md)| [Filter Person by email using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_prefix** | [**List[str]**](str.md)| [Filter Person by email using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_prefix** | [**List[str]**](str.md)| [Filter Person by email using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_suffix** | [**List[str]**](str.md)| [Filter Person by email using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_suffix** | [**List[str]**](str.md)| [Filter Person by email using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_match** | [**List[str]**](str.md)| [Filter Person by email using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_email_not_match** | [**List[str]**](str.md)| [Filter Person by email using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eq** | [**List[str]**](str.md)| [Filter Person by address using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eq** | [**List[str]**](str.md)| [Filter Person by address using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_eql** | [**List[str]**](str.md)| [Filter Person by address using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_eql** | [**List[str]**](str.md)| [Filter Person by address using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_prefix** | [**List[str]**](str.md)| [Filter Person by address using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_prefix** | [**List[str]**](str.md)| [Filter Person by address using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_suffix** | [**List[str]**](str.md)| [Filter Person by address using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_suffix** | [**List[str]**](str.md)| [Filter Person by address using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_match** | [**List[str]**](str.md)| [Filter Person by address using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_address_not_match** | [**List[str]**](str.md)| [Filter Person by address using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eq** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_eql** | [**List[str]**](str.md)| [Filter Person by zip_code using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_prefix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_suffix** | [**List[str]**](str.md)| [Filter Person by zip_code using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_match** | [**List[str]**](str.md)| [Filter Person by zip_code using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_zip_code_not_match** | [**List[str]**](str.md)| [Filter Person by zip_code using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eq** | [**List[str]**](str.md)| [Filter Person by town using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eq** | [**List[str]**](str.md)| [Filter Person by town using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_eql** | [**List[str]**](str.md)| [Filter Person by town using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_eql** | [**List[str]**](str.md)| [Filter Person by town using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_prefix** | [**List[str]**](str.md)| [Filter Person by town using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_prefix** | [**List[str]**](str.md)| [Filter Person by town using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_suffix** | [**List[str]**](str.md)| [Filter Person by town using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_suffix** | [**List[str]**](str.md)| [Filter Person by town using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_match** | [**List[str]**](str.md)| [Filter Person by town using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_town_not_match** | [**List[str]**](str.md)| [Filter Person by town using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eq** | [**List[str]**](str.md)| [Filter Person by country using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eq** | [**List[str]**](str.md)| [Filter Person by country using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_eql** | [**List[str]**](str.md)| [Filter Person by country using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_eql** | [**List[str]**](str.md)| [Filter Person by country using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_prefix** | [**List[str]**](str.md)| [Filter Person by country using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_prefix** | [**List[str]**](str.md)| [Filter Person by country using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_suffix** | [**List[str]**](str.md)| [Filter Person by country using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_suffix** | [**List[str]**](str.md)| [Filter Person by country using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_match** | [**List[str]**](str.md)| [Filter Person by country using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_country_not_match** | [**List[str]**](str.md)| [Filter Person by country using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_not_eq** | [**List[int]**](int.md)| [Filter Person by primary_group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_gte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lt** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_primary_group_id_lte** | [**List[int]**](int.md)| [Filter Person by primary_group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eq** | [**List[str]**](str.md)| [Filter Person by gender using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eq** | [**List[str]**](str.md)| [Filter Person by gender using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_eql** | [**List[str]**](str.md)| [Filter Person by gender using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_eql** | [**List[str]**](str.md)| [Filter Person by gender using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_prefix** | [**List[str]**](str.md)| [Filter Person by gender using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_prefix** | [**List[str]**](str.md)| [Filter Person by gender using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_suffix** | [**List[str]**](str.md)| [Filter Person by gender using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_suffix** | [**List[str]**](str.md)| [Filter Person by gender using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_match** | [**List[str]**](str.md)| [Filter Person by gender using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_gender_not_match** | [**List[str]**](str.md)| [Filter Person by gender using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_eq** | [**List[date]**](date.md)| [Filter Person by birthday using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_not_eq** | [**List[date]**](date.md)| [Filter Person by birthday using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gt** | [**List[date]**](date.md)| [Filter Person by birthday using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_gte** | [**List[date]**](date.md)| [Filter Person by birthday using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lt** | [**List[date]**](date.md)| [Filter Person by birthday using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_birthday_lte** | [**List[date]**](date.md)| [Filter Person by birthday using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eq** | [**List[str]**](str.md)| [Filter Person by language using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eq** | [**List[str]**](str.md)| [Filter Person by language using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_eql** | [**List[str]**](str.md)| [Filter Person by language using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_eql** | [**List[str]**](str.md)| [Filter Person by language using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_prefix** | [**List[str]**](str.md)| [Filter Person by language using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_prefix** | [**List[str]**](str.md)| [Filter Person by language using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_suffix** | [**List[str]**](str.md)| [Filter Person by language using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_suffix** | [**List[str]**](str.md)| [Filter Person by language using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_match** | [**List[str]**](str.md)| [Filter Person by language using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_language_not_match** | [**List[str]**](str.md)| [Filter Person by language using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Person by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_phone_numbers** | [**List[PhoneNumbersReadableAttribute]**](PhoneNumbersReadableAttribute.md)| [Include only specified fields of Phone number in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_social_accounts** | [**List[SocialAccountsReadableAttribute]**](SocialAccountsReadableAttribute.md)| [Include only specified fields of Social account in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_additional_emails** | [**List[AdditionalEmailsReadableAttribute]**](AdditionalEmailsReadableAttribute.md)| [Include only specified fields of Additional email in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**PeopleSingle**](PeopleSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Person resource |  -  |
**202** | Accepted |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Conflict |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

