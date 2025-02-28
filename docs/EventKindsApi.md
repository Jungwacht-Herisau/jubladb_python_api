# jubladb_api.EventKindsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_kind**](EventKindsApi.md#get_event_kind) | **GET** /api/event_kinds/{id} | Fetch Event kind
[**list_event_kinds**](EventKindsApi.md#list_event_kinds) | **GET** /api/event_kinds | List Event kinds


# **get_event_kind**
> EventKindsSingle get_event_kind(id, include=include, sort=sort, fields_event_kinds=fields_event_kinds, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, fields_event_kind_categories=fields_event_kind_categories)

Fetch Event kind

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.event_kind_categories_readable_attribute import EventKindCategoriesReadableAttribute
from jubladb_api.models.event_kinds_readable_attribute import EventKindsReadableAttribute
from jubladb_api.models.event_kinds_single import EventKindsSingle
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
    api_instance = jubladb_api.EventKindsApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort event_kinds according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_event_kinds = [jubladb_api.EventKindsReadableAttribute()] # List[EventKindsReadableAttribute] | [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Kind by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Kind by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Kind by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Kind by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Kind by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Kind by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_event_kind_categories = [jubladb_api.EventKindCategoriesReadableAttribute()] # List[EventKindCategoriesReadableAttribute] | [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Event kind
        api_response = api_instance.get_event_kind(id, include=include, sort=sort, fields_event_kinds=fields_event_kinds, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, fields_event_kind_categories=fields_event_kind_categories)
        print("The response of EventKindsApi->get_event_kind:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventKindsApi->get_event_kind: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort event_kinds according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_event_kinds** | [**List[EventKindsReadableAttribute]**](EventKindsReadableAttribute.md)| [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Kind by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Kind by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Kind by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Kind by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Kind by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Kind by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_event_kind_categories** | [**List[EventKindCategoriesReadableAttribute]**](EventKindCategoriesReadableAttribute.md)| [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**EventKindsSingle**](EventKindsSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Kind resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_kinds**
> EventKindsCollection list_event_kinds(include=include, sort=sort, fields_event_kinds=fields_event_kinds, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, fields_event_kind_categories=fields_event_kind_categories)

List Event kinds

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.event_kind_categories_readable_attribute import EventKindCategoriesReadableAttribute
from jubladb_api.models.event_kinds_collection import EventKindsCollection
from jubladb_api.models.event_kinds_readable_attribute import EventKindsReadableAttribute
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
    api_instance = jubladb_api.EventKindsApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort event_kinds according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_event_kinds = [jubladb_api.EventKindsReadableAttribute()] # List[EventKindsReadableAttribute] | [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Kind by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Kind by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Kind by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Kind by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Kind by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Kind by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_event_kind_categories = [jubladb_api.EventKindCategoriesReadableAttribute()] # List[EventKindCategoriesReadableAttribute] | [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List Event kinds
        api_response = api_instance.list_event_kinds(include=include, sort=sort, fields_event_kinds=fields_event_kinds, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, fields_event_kind_categories=fields_event_kind_categories)
        print("The response of EventKindsApi->list_event_kinds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventKindsApi->list_event_kinds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort event_kinds according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_event_kinds** | [**List[EventKindsReadableAttribute]**](EventKindsReadableAttribute.md)| [Include only specified fields of Kind in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Kind by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Kind by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Kind by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Kind by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Kind by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Kind by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_event_kind_categories** | [**List[EventKindCategoriesReadableAttribute]**](EventKindCategoriesReadableAttribute.md)| [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**EventKindsCollection**](EventKindsCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Kinds collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

