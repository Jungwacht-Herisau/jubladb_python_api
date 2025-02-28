# jubladb_api.RolesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RolesApi.md#create_role) | **POST** /api/roles | Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/roles/{id} | Destroy Role
[**get_role**](RolesApi.md#get_role) | **GET** /api/roles/{id} | Fetch Role
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/roles | List Roles
[**update_role**](RolesApi.md#update_role) | **PUT** /api/roles/{id} | Update Role


# **create_role**
> RolesSingle create_role(roles_request, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)

Create Role

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
from jubladb_api.models.roles_request import RolesRequest
from jubladb_api.models.roles_single import RolesSingle
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
    api_instance = jubladb_api.RolesApi(api_client)
    roles_request = jubladb_api.RolesRequest() # RolesRequest | 
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gt = ['2013-10-20'] # List[date] | [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gte = ['2013-10-20'] # List[date] | [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lt = ['2013-10-20'] # List[date] | [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lte = ['2013-10-20'] # List[date] | [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gt = ['2013-10-20'] # List[date] | [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gte = ['2013-10-20'] # List[date] | [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lt = ['2013-10-20'] # List[date] | [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lte = ['2013-10-20'] # List[date] | [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_eq = [56] # List[int] | [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_not_eq = [56] # List[int] | [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gt = [56] # List[int] | [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gte = [56] # List[int] | [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lt = [56] # List[int] | [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lte = [56] # List[int] | [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eq = ['filter_label_eq_example'] # List[str] | [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eq = ['filter_label_not_eq_example'] # List[str] | [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eql = ['filter_label_eql_example'] # List[str] | [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eql = ['filter_label_not_eql_example'] # List[str] | [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_prefix = ['filter_label_prefix_example'] # List[str] | [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_prefix = ['filter_label_not_prefix_example'] # List[str] | [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_suffix = ['filter_label_suffix_example'] # List[str] | [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_suffix = ['filter_label_not_suffix_example'] # List[str] | [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_match = ['filter_label_match_example'] # List[str] | [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_match = ['filter_label_not_match_example'] # List[str] | [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Create Role
        api_response = api_instance.create_role(roles_request, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **roles_request** | [**RolesRequest**](RolesRequest.md)|  | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_eq** | [**List[date]**](date.md)| [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_not_eq** | [**List[date]**](date.md)| [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gt** | [**List[date]**](date.md)| [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gte** | [**List[date]**](date.md)| [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lt** | [**List[date]**](date.md)| [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lte** | [**List[date]**](date.md)| [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_eq** | [**List[date]**](date.md)| [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_not_eq** | [**List[date]**](date.md)| [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gt** | [**List[date]**](date.md)| [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gte** | [**List[date]**](date.md)| [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lt** | [**List[date]**](date.md)| [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lte** | [**List[date]**](date.md)| [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_eq** | [**List[int]**](int.md)| [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_not_eq** | [**List[int]**](int.md)| [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gt** | [**List[int]**](int.md)| [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gte** | [**List[int]**](int.md)| [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lt** | [**List[int]**](int.md)| [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lte** | [**List[int]**](int.md)| [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eq** | [**List[str]**](str.md)| [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eq** | [**List[str]**](str.md)| [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eql** | [**List[str]**](str.md)| [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eql** | [**List[str]**](str.md)| [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_prefix** | [**List[str]**](str.md)| [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_prefix** | [**List[str]**](str.md)| [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_suffix** | [**List[str]**](str.md)| [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_suffix** | [**List[str]**](str.md)| [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_match** | [**List[str]**](str.md)| [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_match** | [**List[str]**](str.md)| [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**RolesSingle**](RolesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**202** | Accepted |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Conflict |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> JsonapiInfo delete_role(id, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)

Destroy Role

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.jsonapi_info import JsonapiInfo
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
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
    api_instance = jubladb_api.RolesApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gt = ['2013-10-20'] # List[date] | [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gte = ['2013-10-20'] # List[date] | [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lt = ['2013-10-20'] # List[date] | [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lte = ['2013-10-20'] # List[date] | [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gt = ['2013-10-20'] # List[date] | [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gte = ['2013-10-20'] # List[date] | [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lt = ['2013-10-20'] # List[date] | [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lte = ['2013-10-20'] # List[date] | [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_eq = [56] # List[int] | [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_not_eq = [56] # List[int] | [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gt = [56] # List[int] | [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gte = [56] # List[int] | [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lt = [56] # List[int] | [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lte = [56] # List[int] | [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eq = ['filter_label_eq_example'] # List[str] | [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eq = ['filter_label_not_eq_example'] # List[str] | [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eql = ['filter_label_eql_example'] # List[str] | [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eql = ['filter_label_not_eql_example'] # List[str] | [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_prefix = ['filter_label_prefix_example'] # List[str] | [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_prefix = ['filter_label_not_prefix_example'] # List[str] | [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_suffix = ['filter_label_suffix_example'] # List[str] | [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_suffix = ['filter_label_not_suffix_example'] # List[str] | [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_match = ['filter_label_match_example'] # List[str] | [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_match = ['filter_label_not_match_example'] # List[str] | [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Destroy Role
        api_response = api_instance.delete_role(id, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)
        print("The response of RolesApi->delete_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_eq** | [**List[date]**](date.md)| [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_not_eq** | [**List[date]**](date.md)| [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gt** | [**List[date]**](date.md)| [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gte** | [**List[date]**](date.md)| [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lt** | [**List[date]**](date.md)| [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lte** | [**List[date]**](date.md)| [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_eq** | [**List[date]**](date.md)| [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_not_eq** | [**List[date]**](date.md)| [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gt** | [**List[date]**](date.md)| [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gte** | [**List[date]**](date.md)| [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lt** | [**List[date]**](date.md)| [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lte** | [**List[date]**](date.md)| [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_eq** | [**List[int]**](int.md)| [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_not_eq** | [**List[int]**](int.md)| [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gt** | [**List[int]**](int.md)| [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gte** | [**List[int]**](int.md)| [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lt** | [**List[int]**](int.md)| [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lte** | [**List[int]**](int.md)| [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eq** | [**List[str]**](str.md)| [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eq** | [**List[str]**](str.md)| [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eql** | [**List[str]**](str.md)| [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eql** | [**List[str]**](str.md)| [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_prefix** | [**List[str]**](str.md)| [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_prefix** | [**List[str]**](str.md)| [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_suffix** | [**List[str]**](str.md)| [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_suffix** | [**List[str]**](str.md)| [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_match** | [**List[str]**](str.md)| [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_match** | [**List[str]**](str.md)| [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**JsonapiInfo**](JsonapiInfo.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RolesSingle get_role(id, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)

Fetch Role

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
from jubladb_api.models.roles_single import RolesSingle
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
    api_instance = jubladb_api.RolesApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gt = ['2013-10-20'] # List[date] | [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gte = ['2013-10-20'] # List[date] | [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lt = ['2013-10-20'] # List[date] | [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lte = ['2013-10-20'] # List[date] | [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gt = ['2013-10-20'] # List[date] | [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gte = ['2013-10-20'] # List[date] | [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lt = ['2013-10-20'] # List[date] | [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lte = ['2013-10-20'] # List[date] | [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_eq = [56] # List[int] | [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_not_eq = [56] # List[int] | [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gt = [56] # List[int] | [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gte = [56] # List[int] | [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lt = [56] # List[int] | [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lte = [56] # List[int] | [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eq = ['filter_label_eq_example'] # List[str] | [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eq = ['filter_label_not_eq_example'] # List[str] | [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eql = ['filter_label_eql_example'] # List[str] | [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eql = ['filter_label_not_eql_example'] # List[str] | [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_prefix = ['filter_label_prefix_example'] # List[str] | [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_prefix = ['filter_label_not_prefix_example'] # List[str] | [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_suffix = ['filter_label_suffix_example'] # List[str] | [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_suffix = ['filter_label_not_suffix_example'] # List[str] | [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_match = ['filter_label_match_example'] # List[str] | [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_match = ['filter_label_not_match_example'] # List[str] | [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Role
        api_response = api_instance.get_role(id, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)
        print("The response of RolesApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_eq** | [**List[date]**](date.md)| [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_not_eq** | [**List[date]**](date.md)| [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gt** | [**List[date]**](date.md)| [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gte** | [**List[date]**](date.md)| [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lt** | [**List[date]**](date.md)| [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lte** | [**List[date]**](date.md)| [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_eq** | [**List[date]**](date.md)| [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_not_eq** | [**List[date]**](date.md)| [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gt** | [**List[date]**](date.md)| [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gte** | [**List[date]**](date.md)| [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lt** | [**List[date]**](date.md)| [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lte** | [**List[date]**](date.md)| [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_eq** | [**List[int]**](int.md)| [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_not_eq** | [**List[int]**](int.md)| [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gt** | [**List[int]**](int.md)| [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gte** | [**List[int]**](int.md)| [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lt** | [**List[int]**](int.md)| [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lte** | [**List[int]**](int.md)| [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eq** | [**List[str]**](str.md)| [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eq** | [**List[str]**](str.md)| [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eql** | [**List[str]**](str.md)| [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eql** | [**List[str]**](str.md)| [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_prefix** | [**List[str]**](str.md)| [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_prefix** | [**List[str]**](str.md)| [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_suffix** | [**List[str]**](str.md)| [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_suffix** | [**List[str]**](str.md)| [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_match** | [**List[str]**](str.md)| [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_match** | [**List[str]**](str.md)| [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**RolesSingle**](RolesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Role resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> RolesCollection list_roles(include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)

List Roles

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.roles_collection import RolesCollection
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
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
    api_instance = jubladb_api.RolesApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gt = ['2013-10-20'] # List[date] | [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gte = ['2013-10-20'] # List[date] | [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lt = ['2013-10-20'] # List[date] | [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lte = ['2013-10-20'] # List[date] | [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gt = ['2013-10-20'] # List[date] | [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gte = ['2013-10-20'] # List[date] | [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lt = ['2013-10-20'] # List[date] | [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lte = ['2013-10-20'] # List[date] | [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_eq = [56] # List[int] | [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_not_eq = [56] # List[int] | [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gt = [56] # List[int] | [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gte = [56] # List[int] | [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lt = [56] # List[int] | [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lte = [56] # List[int] | [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eq = ['filter_label_eq_example'] # List[str] | [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eq = ['filter_label_not_eq_example'] # List[str] | [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eql = ['filter_label_eql_example'] # List[str] | [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eql = ['filter_label_not_eql_example'] # List[str] | [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_prefix = ['filter_label_prefix_example'] # List[str] | [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_prefix = ['filter_label_not_prefix_example'] # List[str] | [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_suffix = ['filter_label_suffix_example'] # List[str] | [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_suffix = ['filter_label_not_suffix_example'] # List[str] | [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_match = ['filter_label_match_example'] # List[str] | [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_match = ['filter_label_not_match_example'] # List[str] | [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List Roles
        api_response = api_instance.list_roles(include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)
        print("The response of RolesApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_eq** | [**List[date]**](date.md)| [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_not_eq** | [**List[date]**](date.md)| [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gt** | [**List[date]**](date.md)| [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gte** | [**List[date]**](date.md)| [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lt** | [**List[date]**](date.md)| [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lte** | [**List[date]**](date.md)| [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_eq** | [**List[date]**](date.md)| [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_not_eq** | [**List[date]**](date.md)| [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gt** | [**List[date]**](date.md)| [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gte** | [**List[date]**](date.md)| [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lt** | [**List[date]**](date.md)| [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lte** | [**List[date]**](date.md)| [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_eq** | [**List[int]**](int.md)| [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_not_eq** | [**List[int]**](int.md)| [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gt** | [**List[int]**](int.md)| [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gte** | [**List[int]**](int.md)| [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lt** | [**List[int]**](int.md)| [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lte** | [**List[int]**](int.md)| [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eq** | [**List[str]**](str.md)| [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eq** | [**List[str]**](str.md)| [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eql** | [**List[str]**](str.md)| [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eql** | [**List[str]**](str.md)| [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_prefix** | [**List[str]**](str.md)| [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_prefix** | [**List[str]**](str.md)| [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_suffix** | [**List[str]**](str.md)| [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_suffix** | [**List[str]**](str.md)| [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_match** | [**List[str]**](str.md)| [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_match** | [**List[str]**](str.md)| [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**RolesCollection**](RolesCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Roles collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> RolesSingle update_role(id, roles_request, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)

Update Role

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
from jubladb_api.models.roles_readable_attribute import RolesReadableAttribute
from jubladb_api.models.roles_request import RolesRequest
from jubladb_api.models.roles_single import RolesSingle
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
    api_instance = jubladb_api.RolesApi(api_client)
    id = 'id_example' # str | ID of the resource
    roles_request = jubladb_api.RolesRequest() # RolesRequest | 
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_roles = [jubladb_api.RolesReadableAttribute()] # List[RolesReadableAttribute] | [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_created_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gt = ['2013-10-20'] # List[date] | [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_gte = ['2013-10-20'] # List[date] | [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lt = ['2013-10-20'] # List[date] | [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_start_on_lte = ['2013-10-20'] # List[date] | [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_not_eq = ['2013-10-20'] # List[date] | [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gt = ['2013-10-20'] # List[date] | [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_gte = ['2013-10-20'] # List[date] | [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lt = ['2013-10-20'] # List[date] | [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_end_on_lte = ['2013-10-20'] # List[date] | [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_eq = [56] # List[int] | [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_not_eq = [56] # List[int] | [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gt = [56] # List[int] | [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_gte = [56] # List[int] | [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lt = [56] # List[int] | [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_person_id_lte = [56] # List[int] | [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eq = ['filter_type_not_eq_example'] # List[str] | [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eql = ['filter_type_eql_example'] # List[str] | [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_eql = ['filter_type_not_eql_example'] # List[str] | [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_prefix = ['filter_type_prefix_example'] # List[str] | [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_prefix = ['filter_type_not_prefix_example'] # List[str] | [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_suffix = ['filter_type_suffix_example'] # List[str] | [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_suffix = ['filter_type_not_suffix_example'] # List[str] | [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_match = ['filter_type_match_example'] # List[str] | [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_not_match = ['filter_type_not_match_example'] # List[str] | [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eq = ['filter_label_eq_example'] # List[str] | [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eq = ['filter_label_not_eq_example'] # List[str] | [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_eql = ['filter_label_eql_example'] # List[str] | [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_eql = ['filter_label_not_eql_example'] # List[str] | [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_prefix = ['filter_label_prefix_example'] # List[str] | [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_prefix = ['filter_label_not_prefix_example'] # List[str] | [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_suffix = ['filter_label_suffix_example'] # List[str] | [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_suffix = ['filter_label_not_suffix_example'] # List[str] | [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_match = ['filter_label_match_example'] # List[str] | [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_label_not_match = ['filter_label_not_match_example'] # List[str] | [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Update Role
        api_response = api_instance.update_role(id, roles_request, include=include, sort=sort, fields_roles=fields_roles, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_created_at_eq=filter_created_at_eq, filter_created_at_not_eq=filter_created_at_not_eq, filter_created_at_gt=filter_created_at_gt, filter_created_at_gte=filter_created_at_gte, filter_created_at_lt=filter_created_at_lt, filter_created_at_lte=filter_created_at_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_start_on_eq=filter_start_on_eq, filter_start_on_not_eq=filter_start_on_not_eq, filter_start_on_gt=filter_start_on_gt, filter_start_on_gte=filter_start_on_gte, filter_start_on_lt=filter_start_on_lt, filter_start_on_lte=filter_start_on_lte, filter_end_on_eq=filter_end_on_eq, filter_end_on_not_eq=filter_end_on_not_eq, filter_end_on_gt=filter_end_on_gt, filter_end_on_gte=filter_end_on_gte, filter_end_on_lt=filter_end_on_lt, filter_end_on_lte=filter_end_on_lte, filter_person_id_eq=filter_person_id_eq, filter_person_id_not_eq=filter_person_id_not_eq, filter_person_id_gt=filter_person_id_gt, filter_person_id_gte=filter_person_id_gte, filter_person_id_lt=filter_person_id_lt, filter_person_id_lte=filter_person_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_type_eq=filter_type_eq, filter_type_not_eq=filter_type_not_eq, filter_type_eql=filter_type_eql, filter_type_not_eql=filter_type_not_eql, filter_type_prefix=filter_type_prefix, filter_type_not_prefix=filter_type_not_prefix, filter_type_suffix=filter_type_suffix, filter_type_not_suffix=filter_type_not_suffix, filter_type_match=filter_type_match, filter_type_not_match=filter_type_not_match, filter_label_eq=filter_label_eq, filter_label_not_eq=filter_label_not_eq, filter_label_eql=filter_label_eql, filter_label_not_eql=filter_label_not_eql, filter_label_prefix=filter_label_prefix, filter_label_not_prefix=filter_label_not_prefix, filter_label_suffix=filter_label_suffix, filter_label_not_suffix=filter_label_not_suffix, filter_label_match=filter_label_match, filter_label_not_match=filter_label_not_match, fields_people=fields_people, fields_groups=fields_groups)
        print("The response of RolesApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **roles_request** | [**RolesRequest**](RolesRequest.md)|  | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort roles according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_roles** | [**List[RolesReadableAttribute]**](RolesReadableAttribute.md)| [Include only specified fields of Role in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Role by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Role by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Role by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Role by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Role by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Role by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_created_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by created_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Role by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_eq** | [**List[date]**](date.md)| [Filter Role by start_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_not_eq** | [**List[date]**](date.md)| [Filter Role by start_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gt** | [**List[date]**](date.md)| [Filter Role by start_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_gte** | [**List[date]**](date.md)| [Filter Role by start_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lt** | [**List[date]**](date.md)| [Filter Role by start_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_start_on_lte** | [**List[date]**](date.md)| [Filter Role by start_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_eq** | [**List[date]**](date.md)| [Filter Role by end_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_not_eq** | [**List[date]**](date.md)| [Filter Role by end_on using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gt** | [**List[date]**](date.md)| [Filter Role by end_on using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_gte** | [**List[date]**](date.md)| [Filter Role by end_on using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lt** | [**List[date]**](date.md)| [Filter Role by end_on using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_end_on_lte** | [**List[date]**](date.md)| [Filter Role by end_on using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_eq** | [**List[int]**](int.md)| [Filter Role by person_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_not_eq** | [**List[int]**](int.md)| [Filter Role by person_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gt** | [**List[int]**](int.md)| [Filter Role by person_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_gte** | [**List[int]**](int.md)| [Filter Role by person_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lt** | [**List[int]**](int.md)| [Filter Role by person_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_person_id_lte** | [**List[int]**](int.md)| [Filter Role by person_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Role by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Role by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Role by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Role by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Role by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Role by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Role by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eq** | [**List[str]**](str.md)| [Filter Role by type using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eql** | [**List[str]**](str.md)| [Filter Role by type using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_eql** | [**List[str]**](str.md)| [Filter Role by type using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_prefix** | [**List[str]**](str.md)| [Filter Role by type using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_prefix** | [**List[str]**](str.md)| [Filter Role by type using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_suffix** | [**List[str]**](str.md)| [Filter Role by type using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_suffix** | [**List[str]**](str.md)| [Filter Role by type using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_match** | [**List[str]**](str.md)| [Filter Role by type using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_not_match** | [**List[str]**](str.md)| [Filter Role by type using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eq** | [**List[str]**](str.md)| [Filter Role by label using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eq** | [**List[str]**](str.md)| [Filter Role by label using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_eql** | [**List[str]**](str.md)| [Filter Role by label using eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_eql** | [**List[str]**](str.md)| [Filter Role by label using not_eql operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_prefix** | [**List[str]**](str.md)| [Filter Role by label using prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_prefix** | [**List[str]**](str.md)| [Filter Role by label using not_prefix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_suffix** | [**List[str]**](str.md)| [Filter Role by label using suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_suffix** | [**List[str]**](str.md)| [Filter Role by label using not_suffix operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_match** | [**List[str]**](str.md)| [Filter Role by label using match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_label_not_match** | [**List[str]**](str.md)| [Filter Role by label using not_match operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**RolesSingle**](RolesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Role resource |  -  |
**202** | Accepted |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Conflict |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

