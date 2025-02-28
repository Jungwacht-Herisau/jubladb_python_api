# JsonapiJsonapi

An object describing the server's implementation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_jsonapi import JsonapiJsonapi

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiJsonapi from a JSON string
jsonapi_jsonapi_instance = JsonapiJsonapi.from_json(json)
# print the JSON string representation of the object
print(JsonapiJsonapi.to_json())

# convert the object into a dict
jsonapi_jsonapi_dict = jsonapi_jsonapi_instance.to_dict()
# create an instance of JsonapiJsonapi from a dict
jsonapi_jsonapi_from_dict = JsonapiJsonapi.from_dict(jsonapi_jsonapi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


