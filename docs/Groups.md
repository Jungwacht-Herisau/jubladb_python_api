# Groups

Group attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] [readonly] 
**short_name** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**layer** | **bool** |  | [optional] [readonly] 
**parent_id** | **int** |  | [optional] [readonly] 
**layer_group_id** | **int** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**email** | **str** |  | [optional] [readonly] 
**address** | **str** |  | [optional] [readonly] 
**zip_code** | **int** |  | [optional] [readonly] 
**town** | **str** |  | [optional] [readonly] 
**country** | **str** |  | [optional] [readonly] 
**require_person_add_requests** | **bool** |  | [optional] [readonly] 
**self_registration_url** | **str** |  | [optional] [readonly] 
**archived_at** | **datetime** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 
**deleted_at** | **datetime** |  | [optional] [readonly] 
**logo** | **str** |  This *extra field* will only be present if requested explicitely with the &#x60;extra_fields[groups]&#x60; parameter. See [Graphiti Resource Extra fields](https://www.graphiti.dev/guides/concepts/resources#extra-fields) for more information.  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.groups import Groups

# TODO update the JSON string below
json = "{}"
# create an instance of Groups from a JSON string
groups_instance = Groups.from_json(json)
# print the JSON string representation of the object
print(Groups.to_json())

# convert the object into a dict
groups_dict = groups_instance.to_dict()
# create an instance of Groups from a dict
groups_from_dict = Groups.from_dict(groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


