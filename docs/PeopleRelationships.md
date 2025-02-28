# PeopleRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**layer_group** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**roles** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 
**phone_numbers** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 
**social_accounts** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 
**additional_emails** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 

## Example

```python
from jubladb_api.models.people_relationships import PeopleRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleRelationships from a JSON string
people_relationships_instance = PeopleRelationships.from_json(json)
# print the JSON string representation of the object
print(PeopleRelationships.to_json())

# convert the object into a dict
people_relationships_dict = people_relationships_instance.to_dict()
# create an instance of PeopleRelationships from a dict
people_relationships_from_dict = PeopleRelationships.from_dict(people_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


