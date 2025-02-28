# GroupsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**creator** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**updater** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**deleter** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**parent** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**layer_group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**phone_numbers** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 
**social_accounts** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 
**additional_emails** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 

## Example

```python
from jubladb_api.models.groups_relationships import GroupsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsRelationships from a JSON string
groups_relationships_instance = GroupsRelationships.from_json(json)
# print the JSON string representation of the object
print(GroupsRelationships.to_json())

# convert the object into a dict
groups_relationships_dict = groups_relationships_instance.to_dict()
# create an instance of GroupsRelationships from a dict
groups_relationships_from_dict = GroupsRelationships.from_dict(groups_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


