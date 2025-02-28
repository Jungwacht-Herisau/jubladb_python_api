# RolesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Roles**](Roles.md) |  | [optional] 
**relationships** | [**RolesRelationships**](RolesRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.roles_resource import RolesResource

# TODO update the JSON string below
json = "{}"
# create an instance of RolesResource from a JSON string
roles_resource_instance = RolesResource.from_json(json)
# print the JSON string representation of the object
print(RolesResource.to_json())

# convert the object into a dict
roles_resource_dict = roles_resource_instance.to_dict()
# create an instance of RolesResource from a dict
roles_resource_from_dict = RolesResource.from_dict(roles_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


