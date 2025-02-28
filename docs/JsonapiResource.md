# JsonapiResource


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
from jubladb_api.models.jsonapi_resource import JsonapiResource

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiResource from a JSON string
jsonapi_resource_instance = JsonapiResource.from_json(json)
# print the JSON string representation of the object
print(JsonapiResource.to_json())

# convert the object into a dict
jsonapi_resource_dict = jsonapi_resource_instance.to_dict()
# create an instance of JsonapiResource from a dict
jsonapi_resource_from_dict = JsonapiResource.from_dict(jsonapi_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


