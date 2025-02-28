# PersonNameResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**PersonName**](PersonName.md) |  | [optional] 
**relationships** | **object** | Members of the relationships object (\&quot;relationships\&quot;) represent references from the resource object in which it&#39;s defined to other resource objects. | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.person_name_resource import PersonNameResource

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNameResource from a JSON string
person_name_resource_instance = PersonNameResource.from_json(json)
# print the JSON string representation of the object
print(PersonNameResource.to_json())

# convert the object into a dict
person_name_resource_dict = person_name_resource_instance.to_dict()
# create an instance of PersonNameResource from a dict
person_name_resource_from_dict = PersonNameResource.from_dict(person_name_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


