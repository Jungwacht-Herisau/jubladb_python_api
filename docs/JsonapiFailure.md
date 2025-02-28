# JsonapiFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[JsonapiError]**](JsonapiError.md) |  | 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_failure import JsonapiFailure

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiFailure from a JSON string
jsonapi_failure_instance = JsonapiFailure.from_json(json)
# print the JSON string representation of the object
print(JsonapiFailure.to_json())

# convert the object into a dict
jsonapi_failure_dict = jsonapi_failure_instance.to_dict()
# create an instance of JsonapiFailure from a dict
jsonapi_failure_from_dict = JsonapiFailure.from_dict(jsonapi_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


