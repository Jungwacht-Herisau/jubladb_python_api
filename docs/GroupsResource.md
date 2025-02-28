# GroupsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Groups**](Groups.md) |  | [optional] 
**relationships** | [**GroupsRelationships**](GroupsRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.groups_resource import GroupsResource

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsResource from a JSON string
groups_resource_instance = GroupsResource.from_json(json)
# print the JSON string representation of the object
print(GroupsResource.to_json())

# convert the object into a dict
groups_resource_dict = groups_resource_instance.to_dict()
# create an instance of GroupsResource from a dict
groups_resource_from_dict = GroupsResource.from_dict(groups_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


