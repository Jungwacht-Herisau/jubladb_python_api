# jubladb_api.EventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /api/events/{id} | Fetch Event
[**list_events**](EventsApi.md#list_events) | **GET** /api/events | List Events


# **get_event**
> EventsSingle get_event(id, include=include, sort=sort, fields_events=fields_events, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_kind_id_eq=filter_kind_id_eq, filter_kind_id_not_eq=filter_kind_id_not_eq, filter_kind_id_gt=filter_kind_id_gt, filter_kind_id_gte=filter_kind_id_gte, filter_kind_id_lt=filter_kind_id_lt, filter_kind_id_lte=filter_kind_id_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_type_eq=filter_type_eq, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_before_or_on_eq=filter_before_or_on_eq, filter_after_or_on_eq=filter_after_or_on_eq, filter_kind_category_id_eq=filter_kind_category_id_eq, fields_people=fields_people, fields_event_kinds=fields_event_kinds, fields_dates=fields_dates)

Fetch Event

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.dates_readable_attribute import DatesReadableAttribute
from jubladb_api.models.event_kinds_readable_attribute import EventKindsReadableAttribute
from jubladb_api.models.events_readable_attribute import EventsReadableAttribute
from jubladb_api.models.events_single import EventsSingle
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
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
    api_instance = jubladb_api.EventsApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort events according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_events = [jubladb_api.EventsReadableAttribute()] # List[EventsReadableAttribute] | [Include only specified fields of Event in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Event by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Event by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Event by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Event by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Event by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Event by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_eq = [56] # List[int] | [Filter Event by kind_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_not_eq = [56] # List[int] | [Filter Event by kind_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_gt = [56] # List[int] | [Filter Event by kind_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_gte = [56] # List[int] | [Filter Event by kind_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_lt = [56] # List[int] | [Filter Event by kind_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_lte = [56] # List[int] | [Filter Event by kind_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Event by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Event by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Event by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_before_or_on_eq = '2013-10-20' # date | [Filter Event by before_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_after_or_on_eq = '2013-10-20' # date | [Filter Event by after_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_category_id_eq = [56] # List[int] | [Filter Event by kind_category_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_event_kinds = [jubladb_api.EventKindsReadableAttribute()] # List[EventKindsReadableAttribute] | [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_dates = [jubladb_api.DatesReadableAttribute()] # List[DatesReadableAttribute] | [Include only specified fields of Date in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Event
        api_response = api_instance.get_event(id, include=include, sort=sort, fields_events=fields_events, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_kind_id_eq=filter_kind_id_eq, filter_kind_id_not_eq=filter_kind_id_not_eq, filter_kind_id_gt=filter_kind_id_gt, filter_kind_id_gte=filter_kind_id_gte, filter_kind_id_lt=filter_kind_id_lt, filter_kind_id_lte=filter_kind_id_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_type_eq=filter_type_eq, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_before_or_on_eq=filter_before_or_on_eq, filter_after_or_on_eq=filter_after_or_on_eq, filter_kind_category_id_eq=filter_kind_category_id_eq, fields_people=fields_people, fields_event_kinds=fields_event_kinds, fields_dates=fields_dates)
        print("The response of EventsApi->get_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort events according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_events** | [**List[EventsReadableAttribute]**](EventsReadableAttribute.md)| [Include only specified fields of Event in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Event by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Event by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Event by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Event by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Event by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Event by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_eq** | [**List[int]**](int.md)| [Filter Event by kind_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_not_eq** | [**List[int]**](int.md)| [Filter Event by kind_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_gt** | [**List[int]**](int.md)| [Filter Event by kind_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_gte** | [**List[int]**](int.md)| [Filter Event by kind_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_lt** | [**List[int]**](int.md)| [Filter Event by kind_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_lte** | [**List[int]**](int.md)| [Filter Event by kind_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Event by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Event by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Event by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_before_or_on_eq** | **date**| [Filter Event by before_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_after_or_on_eq** | **date**| [Filter Event by after_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_category_id_eq** | [**List[int]**](int.md)| [Filter Event by kind_category_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_event_kinds** | [**List[EventKindsReadableAttribute]**](EventKindsReadableAttribute.md)| [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_dates** | [**List[DatesReadableAttribute]**](DatesReadableAttribute.md)| [Include only specified fields of Date in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**EventsSingle**](EventsSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Event resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_events**
> EventsCollection list_events(include=include, sort=sort, fields_events=fields_events, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_kind_id_eq=filter_kind_id_eq, filter_kind_id_not_eq=filter_kind_id_not_eq, filter_kind_id_gt=filter_kind_id_gt, filter_kind_id_gte=filter_kind_id_gte, filter_kind_id_lt=filter_kind_id_lt, filter_kind_id_lte=filter_kind_id_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_type_eq=filter_type_eq, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_before_or_on_eq=filter_before_or_on_eq, filter_after_or_on_eq=filter_after_or_on_eq, filter_kind_category_id_eq=filter_kind_category_id_eq, fields_people=fields_people, fields_event_kinds=fields_event_kinds, fields_dates=fields_dates)

List Events

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.dates_readable_attribute import DatesReadableAttribute
from jubladb_api.models.event_kinds_readable_attribute import EventKindsReadableAttribute
from jubladb_api.models.events_collection import EventsCollection
from jubladb_api.models.events_readable_attribute import EventsReadableAttribute
from jubladb_api.models.people_readable_attribute import PeopleReadableAttribute
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
    api_instance = jubladb_api.EventsApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort events according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_events = [jubladb_api.EventsReadableAttribute()] # List[EventsReadableAttribute] | [Include only specified fields of Event in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Event by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Event by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Event by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Event by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Event by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Event by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_eq = [56] # List[int] | [Filter Event by kind_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_not_eq = [56] # List[int] | [Filter Event by kind_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_gt = [56] # List[int] | [Filter Event by kind_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_gte = [56] # List[int] | [Filter Event by kind_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_lt = [56] # List[int] | [Filter Event by kind_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_id_lte = [56] # List[int] | [Filter Event by kind_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_not_eq = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_gte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lt = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_updated_at_lte = ['2013-10-20T19:20:30+01:00'] # List[datetime] | [Filter Event by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_type_eq = ['filter_type_eq_example'] # List[str] | [Filter Event by type using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Event by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Event by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_before_or_on_eq = '2013-10-20' # date | [Filter Event by before_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_after_or_on_eq = '2013-10-20' # date | [Filter Event by after_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_kind_category_id_eq = [56] # List[int] | [Filter Event by kind_category_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_event_kinds = [jubladb_api.EventKindsReadableAttribute()] # List[EventKindsReadableAttribute] | [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_dates = [jubladb_api.DatesReadableAttribute()] # List[DatesReadableAttribute] | [Include only specified fields of Date in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List Events
        api_response = api_instance.list_events(include=include, sort=sort, fields_events=fields_events, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_kind_id_eq=filter_kind_id_eq, filter_kind_id_not_eq=filter_kind_id_not_eq, filter_kind_id_gt=filter_kind_id_gt, filter_kind_id_gte=filter_kind_id_gte, filter_kind_id_lt=filter_kind_id_lt, filter_kind_id_lte=filter_kind_id_lte, filter_updated_at_eq=filter_updated_at_eq, filter_updated_at_not_eq=filter_updated_at_not_eq, filter_updated_at_gt=filter_updated_at_gt, filter_updated_at_gte=filter_updated_at_gte, filter_updated_at_lt=filter_updated_at_lt, filter_updated_at_lte=filter_updated_at_lte, filter_type_eq=filter_type_eq, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_before_or_on_eq=filter_before_or_on_eq, filter_after_or_on_eq=filter_after_or_on_eq, filter_kind_category_id_eq=filter_kind_category_id_eq, fields_people=fields_people, fields_event_kinds=fields_event_kinds, fields_dates=fields_dates)
        print("The response of EventsApi->list_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->list_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort events according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_events** | [**List[EventsReadableAttribute]**](EventsReadableAttribute.md)| [Include only specified fields of Event in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Event by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Event by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Event by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Event by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Event by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Event by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_eq** | [**List[int]**](int.md)| [Filter Event by kind_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_not_eq** | [**List[int]**](int.md)| [Filter Event by kind_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_gt** | [**List[int]**](int.md)| [Filter Event by kind_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_gte** | [**List[int]**](int.md)| [Filter Event by kind_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_lt** | [**List[int]**](int.md)| [Filter Event by kind_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_id_lte** | [**List[int]**](int.md)| [Filter Event by kind_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_eq** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_not_eq** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gt** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_gte** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lt** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_updated_at_lte** | [**List[datetime]**](datetime.md)| [Filter Event by updated_at using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_type_eq** | [**List[str]**](str.md)| [Filter Event by type using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Event by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Event by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_before_or_on_eq** | **date**| [Filter Event by before_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_after_or_on_eq** | **date**| [Filter Event by after_or_on using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_kind_category_id_eq** | [**List[int]**](int.md)| [Filter Event by kind_category_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_event_kinds** | [**List[EventKindsReadableAttribute]**](EventKindsReadableAttribute.md)| [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_dates** | [**List[DatesReadableAttribute]**](DatesReadableAttribute.md)| [Include only specified fields of Date in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**EventsCollection**](EventsCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Events collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

