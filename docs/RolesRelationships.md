# RolesRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**person** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**layer_group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 

## Example

```python
from jubladb_api.models.roles_relationships import RolesRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of RolesRelationships from a JSON string
roles_relationships_instance = RolesRelationships.from_json(json)
# print the JSON string representation of the object
print(RolesRelationships.to_json())

# convert the object into a dict
roles_relationships_dict = roles_relationships_instance.to_dict()
# create an instance of RolesRelationships from a dict
roles_relationships_from_dict = RolesRelationships.from_dict(roles_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


