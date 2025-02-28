# CoursesRelationshipsContact


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JsonapiRelationshipLinks**](JsonapiRelationshipLinks.md) |  | [optional] 
**data** | [**JsonapiLinkage**](JsonapiLinkage.md) |  | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.courses_relationships_contact import CoursesRelationshipsContact

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesRelationshipsContact from a JSON string
courses_relationships_contact_instance = CoursesRelationshipsContact.from_json(json)
# print the JSON string representation of the object
print(CoursesRelationshipsContact.to_json())

# convert the object into a dict
courses_relationships_contact_dict = courses_relationships_contact_instance.to_dict()
# create an instance of CoursesRelationshipsContact from a dict
courses_relationships_contact_from_dict = CoursesRelationshipsContact.from_dict(courses_relationships_contact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


