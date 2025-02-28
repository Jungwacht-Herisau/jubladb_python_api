# Roles

Role attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**start_on** | **date** |  | [optional] [readonly] 
**end_on** | **date** |  | [optional] [readonly] 
**person_id** | **int** |  | [optional] 
**group_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**label** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.roles import Roles

# TODO update the JSON string below
json = "{}"
# create an instance of Roles from a JSON string
roles_instance = Roles.from_json(json)
# print the JSON string representation of the object
print(Roles.to_json())

# convert the object into a dict
roles_dict = roles_instance.to_dict()
# create an instance of Roles from a dict
roles_from_dict = Roles.from_dict(roles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


