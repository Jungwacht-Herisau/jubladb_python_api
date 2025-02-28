# CoursesRelationshipsDates


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JsonapiRelationshipLinks**](JsonapiRelationshipLinks.md) |  | [optional] 
**data** | [**List[JsonapiLinkage]**](JsonapiLinkage.md) | An array of objects each containing \&quot;type\&quot; and \&quot;id\&quot; members for to-many relationships. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.courses_relationships_dates import CoursesRelationshipsDates

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesRelationshipsDates from a JSON string
courses_relationships_dates_instance = CoursesRelationshipsDates.from_json(json)
# print the JSON string representation of the object
print(CoursesRelationshipsDates.to_json())

# convert the object into a dict
courses_relationships_dates_dict = courses_relationships_dates_instance.to_dict()
# create an instance of CoursesRelationshipsDates from a dict
courses_relationships_dates_from_dict = CoursesRelationshipsDates.from_dict(courses_relationships_dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


