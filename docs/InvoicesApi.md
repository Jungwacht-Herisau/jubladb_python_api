# jubladb_api.InvoicesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /api/invoices/{id} | Fetch Invoice
[**list_invoices**](InvoicesApi.md#list_invoices) | **GET** /api/invoices | List Invoices
[**update_invoice**](InvoicesApi.md#update_invoice) | **PUT** /api/invoices/{id} | Update Invoice


# **get_invoice**
> InvoicesSingle get_invoice(id, include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)

Fetch Invoice

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.invoice_items_readable_attribute import InvoiceItemsReadableAttribute
from jubladb_api.models.invoices_readable_attribute import InvoicesReadableAttribute
from jubladb_api.models.invoices_single import InvoicesSingle
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
    api_instance = jubladb_api.InvoicesApi(api_client)
    id = 'id_example' # str | ID of the resource
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_invoices = [jubladb_api.InvoicesReadableAttribute()] # List[InvoicesReadableAttribute] | [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_eq = [56] # List[int] | [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_not_eq = [56] # List[int] | [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gt = [56] # List[int] | [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gte = [56] # List[int] | [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lt = [56] # List[int] | [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lte = [56] # List[int] | [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_invoice_items = [jubladb_api.InvoiceItemsReadableAttribute()] # List[InvoiceItemsReadableAttribute] | [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Fetch Invoice
        api_response = api_instance.get_invoice(id, include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)
        print("The response of InvoicesApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_invoices** | [**List[InvoicesReadableAttribute]**](InvoicesReadableAttribute.md)| [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_invoice_items** | [**List[InvoiceItemsReadableAttribute]**](InvoiceItemsReadableAttribute.md)| [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**InvoicesSingle**](InvoicesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Invoice resource |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> InvoicesCollection list_invoices(include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)

List Invoices

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.invoice_items_readable_attribute import InvoiceItemsReadableAttribute
from jubladb_api.models.invoices_collection import InvoicesCollection
from jubladb_api.models.invoices_readable_attribute import InvoicesReadableAttribute
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
    api_instance = jubladb_api.InvoicesApi(api_client)
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_invoices = [jubladb_api.InvoicesReadableAttribute()] # List[InvoicesReadableAttribute] | [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_eq = [56] # List[int] | [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_not_eq = [56] # List[int] | [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gt = [56] # List[int] | [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gte = [56] # List[int] | [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lt = [56] # List[int] | [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lte = [56] # List[int] | [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_invoice_items = [jubladb_api.InvoiceItemsReadableAttribute()] # List[InvoiceItemsReadableAttribute] | [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # List Invoices
        api_response = api_instance.list_invoices(include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)
        print("The response of InvoicesApi->list_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->list_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_invoices** | [**List[InvoicesReadableAttribute]**](InvoicesReadableAttribute.md)| [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_invoice_items** | [**List[InvoiceItemsReadableAttribute]**](InvoiceItemsReadableAttribute.md)| [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**InvoicesCollection**](InvoicesCollection.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Invoices collection |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_invoice**
> InvoicesSingle update_invoice(id, invoices_request, include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)

Update Invoice

### Example

* Api Key Authentication (ServiceTokenAuthHeader):
* Api Key Authentication (ServiceTokenAuthParam):

```python
import jubladb_api
from jubladb_api.models.groups_readable_attribute import GroupsReadableAttribute
from jubladb_api.models.invoice_items_readable_attribute import InvoiceItemsReadableAttribute
from jubladb_api.models.invoices_readable_attribute import InvoicesReadableAttribute
from jubladb_api.models.invoices_request import InvoicesRequest
from jubladb_api.models.invoices_single import InvoicesSingle
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
    api_instance = jubladb_api.InvoicesApi(api_client)
    id = 'id_example' # str | ID of the resource
    invoices_request = jubladb_api.InvoicesRequest() # InvoicesRequest | 
    include = ['include_example'] # List[str] | [Include related resources](https://jsonapi.org/format/#fetching-includes) (optional)
    sort = ['sort_example'] # List[str] | [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending `id` and descending `-id` fields the same time   (optional)
    fields_invoices = [jubladb_api.InvoicesReadableAttribute()] # List[InvoicesReadableAttribute] | [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    filter_id_eq = [56] # List[int] | [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_not_eq = [56] # List[int] | [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gt = [56] # List[int] | [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_gte = [56] # List[int] | [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lt = [56] # List[int] | [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_id_lte = [56] # List[int] | [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_eq = [56] # List[int] | [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_not_eq = [56] # List[int] | [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gt = [56] # List[int] | [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_gte = [56] # List[int] | [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lt = [56] # List[int] | [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_group_id_lte = [56] # List[int] | [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_eq = [56] # List[int] | [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_not_eq = [56] # List[int] | [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gt = [56] # List[int] | [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_gte = [56] # List[int] | [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lt = [56] # List[int] | [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    filter_recipient_id_lte = [56] # List[int] | [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) (optional)
    fields_groups = [jubladb_api.GroupsReadableAttribute()] # List[GroupsReadableAttribute] | [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_people = [jubladb_api.PeopleReadableAttribute()] # List[PeopleReadableAttribute] | [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)
    fields_invoice_items = [jubladb_api.InvoiceItemsReadableAttribute()] # List[InvoiceItemsReadableAttribute] | [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) (optional)

    try:
        # Update Invoice
        api_response = api_instance.update_invoice(id, invoices_request, include=include, sort=sort, fields_invoices=fields_invoices, filter_id_eq=filter_id_eq, filter_id_not_eq=filter_id_not_eq, filter_id_gt=filter_id_gt, filter_id_gte=filter_id_gte, filter_id_lt=filter_id_lt, filter_id_lte=filter_id_lte, filter_group_id_eq=filter_group_id_eq, filter_group_id_not_eq=filter_group_id_not_eq, filter_group_id_gt=filter_group_id_gt, filter_group_id_gte=filter_group_id_gte, filter_group_id_lt=filter_group_id_lt, filter_group_id_lte=filter_group_id_lte, filter_recipient_id_eq=filter_recipient_id_eq, filter_recipient_id_not_eq=filter_recipient_id_not_eq, filter_recipient_id_gt=filter_recipient_id_gt, filter_recipient_id_gte=filter_recipient_id_gte, filter_recipient_id_lt=filter_recipient_id_lt, filter_recipient_id_lte=filter_recipient_id_lte, fields_groups=fields_groups, fields_people=fields_people, fields_invoice_items=fields_invoice_items)
        print("The response of InvoicesApi->update_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->update_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource | 
 **invoices_request** | [**InvoicesRequest**](InvoicesRequest.md)|  | 
 **include** | [**List[str]**](str.md)| [Include related resources](https://jsonapi.org/format/#fetching-includes) | [optional] 
 **sort** | [**List[str]**](str.md)| [Sort invoices according to one or more criteria](https://jsonapi.org/format/#fetching-sorting)  You should not include both ascending &#x60;id&#x60; and descending &#x60;-id&#x60; fields the same time   | [optional] 
 **fields_invoices** | [**List[InvoicesReadableAttribute]**](InvoicesReadableAttribute.md)| [Include only specified fields of Invoice in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **filter_id_eq** | [**List[int]**](int.md)| [Filter Invoice by id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gt** | [**List[int]**](int.md)| [Filter Invoice by id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_gte** | [**List[int]**](int.md)| [Filter Invoice by id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lt** | [**List[int]**](int.md)| [Filter Invoice by id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_id_lte** | [**List[int]**](int.md)| [Filter Invoice by id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by group_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gt** | [**List[int]**](int.md)| [Filter Invoice by group_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_gte** | [**List[int]**](int.md)| [Filter Invoice by group_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lt** | [**List[int]**](int.md)| [Filter Invoice by group_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_group_id_lte** | [**List[int]**](int.md)| [Filter Invoice by group_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_not_eq** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using not_eq operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_gte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using gte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lt** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lt operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **filter_recipient_id_lte** | [**List[int]**](int.md)| [Filter Invoice by recipient_id using lte operator](https://jsonapi.org/format/#fetching-filtering) | [optional] 
 **fields_groups** | [**List[GroupsReadableAttribute]**](GroupsReadableAttribute.md)| [Include only specified fields of Group in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_people** | [**List[PeopleReadableAttribute]**](PeopleReadableAttribute.md)| [Include only specified fields of Person in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 
 **fields_invoice_items** | [**List[InvoiceItemsReadableAttribute]**](InvoiceItemsReadableAttribute.md)| [Include only specified fields of Invoice item in response](https://jsonapi.org/format/#fetching-sparse-fieldsets) | [optional] 

### Return type

[**InvoicesSingle**](InvoicesSingle.md)

### Authorization

[ServiceTokenAuthHeader](../README.md#ServiceTokenAuthHeader), [ServiceTokenAuthParam](../README.md#ServiceTokenAuthParam)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK: Invoice resource |  -  |
**202** | Accepted |  -  |
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**403** | Conflict |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

