# JsonapiError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 
**status** | **str** | The HTTP status code applicable to this problem, expressed as a string value. | [optional] 
**code** | **str** | An application-specific error code, expressed as a string value. | [optional] 
**title** | **str** | A short, human-readable summary of the problem. It **SHOULD NOT** change from occurrence to occurrence of the problem, except for purposes of localization. | [optional] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] 
**source** | [**JsonapiErrorSource**](JsonapiErrorSource.md) |  | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_error import JsonapiError

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiError from a JSON string
jsonapi_error_instance = JsonapiError.from_json(json)
# print the JSON string representation of the object
print(JsonapiError.to_json())

# convert the object into a dict
jsonapi_error_dict = jsonapi_error_instance.to_dict()
# create an instance of JsonapiError from a dict
jsonapi_error_from_dict = JsonapiError.from_dict(jsonapi_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


