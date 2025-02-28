# jubladb_api.EventKindCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_kind_category**](EventKindCategoriesApi.md#get_event_kind_category) | **GET** /api/event_kind_categories/{id} | Fetch Event kind category
[**list_event_kind_categories**](EventKindCategoriesApi.md#list_event_kind_categories) | **GET** /api/event_kind_categories | List Event kind categories


# **get_event_kind_category**
> EventKindCategoriesSingle get_event_kind_category(id, sort=sort, fields_event_kind_categories=fields_event_kind_categories, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte)

Fetch Event kind category

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.event_kind_categories_readable_attribute import EventKindCategoriesReadableAttribute
from jubladb_api.models.event_kind_categories_single import EventKindCategoriesSingle
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
    api_instance = jubladb_api.EventKindCategoriesApi(api_client)
    id = 'id_example' # str | ID of the resource
    sort = ['sort_example'] # List[str] | [Sort event_kind_categories according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_event_kind_categories = [jubladb_api.EventKindCategoriesReadableAttribute()] # List[EventKindCategoriesReadableAttribute] | [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Kind category by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Kind category by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Kind category by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Kind category by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Kind category by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Kind category by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)

    try:
        # Fetch Event kind category
        api_response = api_instance.get_event_kind_category(id, sort=sort, fields_event_kind_categories=fields_event_kind_categories, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte)
        print("The response of EventKindCategoriesApi->get_event_kind_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventKindCategoriesApi->get_event_kind_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **sort** | [**List[str]**](str.md)| [Sort event_kind_categories according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_event_kind_categories** | [**List[EventKindCategoriesReadableAttribute]**](EventKindCategoriesReadableAttribute.md)| [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Kind category by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Kind category by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Kind category by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Kind category by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Kind category by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Kind category by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 

### Return type

[**EventKindCategoriesSingle**](EventKindCategoriesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Kind category resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_kind_categories**
> EventKindCategoriesCollection list_event_kind_categories(sort=sort, fields_event_kind_categories=fields_event_kind_categories, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte)

List Event kind categories

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.event_kind_categories_collection import EventKindCategoriesCollection
from jubladb_api.models.event_kind_categories_readable_attribute import EventKindCategoriesReadableAttribute
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
    api_instance = jubladb_api.EventKindCategoriesApi(api_client)
    sort = ['sort_example'] # List[str] | [Sort event_kind_categories according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_event_kind_categories = [jubladb_api.EventKindCategoriesReadableAttribute()] # List[EventKindCategoriesReadableAttribute] | [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Kind category by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Kind category by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Kind category by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Kind category by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Kind category by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Kind category by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)

    try:
        # List Event kind categories
        api_response = api_instance.list_event_kind_categories(sort=sort, fields_event_kind_categories=fields_event_kind_categories, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte)
        print("The response of EventKindCategoriesApi->list_event_kind_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventKindCategoriesApi->list_event_kind_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**List[str]**](str.md)| [Sort event_kind_categories according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_event_kind_categories** | [**List[EventKindCategoriesReadableAttribute]**](EventKindCategoriesReadableAttribute.md)| [Include only specified fields of Kind category in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Kind category by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Kind category by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Kind category by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Kind category by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Kind category by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Kind category by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 

### Return type

[**EventKindCategoriesCollection**](EventKindCategoriesCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Kind categories collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

