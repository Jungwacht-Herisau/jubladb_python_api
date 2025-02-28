# JsonapiErrorSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pointer** | **str** | A JSON Pointer [RFC6901] to the associated entity in the request document [e.g. \&quot;/data\&quot; for a primary data object, or \&quot;/data/attributes/title\&quot; for a specific attribute]. | [optional] 
**parameter** | **str** | A string indicating which query parameter caused the error. | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_error_source import JsonapiErrorSource

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiErrorSource from a JSON string
jsonapi_error_source_instance = JsonapiErrorSource.from_json(json)
# print the JSON string representation of the object
print(JsonapiErrorSource.to_json())

# convert the object into a dict
jsonapi_error_source_dict = jsonapi_error_source_instance.to_dict()
# create an instance of JsonapiErrorSource from a dict
jsonapi_error_source_from_dict = JsonapiErrorSource.from_dict(jsonapi_error_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


