# JsonapiInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_info import JsonapiInfo

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiInfo from a JSON string
jsonapi_info_instance = JsonapiInfo.from_json(json)
# print the JSON string representation of the object
print(JsonapiInfo.to_json())

# convert the object into a dict
jsonapi_info_dict = jsonapi_info_instance.to_dict()
# create an instance of JsonapiInfo from a dict
jsonapi_info_from_dict = JsonapiInfo.from_dict(jsonapi_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


