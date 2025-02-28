# JsonapiPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**last** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**prev** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**next** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_pagination import JsonapiPagination

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiPagination from a JSON string
jsonapi_pagination_instance = JsonapiPagination.from_json(json)
# print the JSON string representation of the object
print(JsonapiPagination.to_json())

# convert the object into a dict
jsonapi_pagination_dict = jsonapi_pagination_instance.to_dict()
# create an instance of JsonapiPagination from a dict
jsonapi_pagination_from_dict = JsonapiPagination.from_dict(jsonapi_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


