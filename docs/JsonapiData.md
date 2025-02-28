# JsonapiData

The document's \"primary data\" is a representation of the resource or collection of resources targeted by a request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**SocialAccounts**](SocialAccounts.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_data import JsonapiData

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiData from a JSON string
jsonapi_data_instance = JsonapiData.from_json(json)
# print the JSON string representation of the object
print(JsonapiData.to_json())

# convert the object into a dict
jsonapi_data_dict = jsonapi_data_instance.to_dict()
# create an instance of JsonapiData from a dict
jsonapi_data_from_dict = JsonapiData.from_dict(jsonapi_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


