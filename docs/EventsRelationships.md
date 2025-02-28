# EventsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contact** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**kind** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 
**dates** | [**CoursesRelationshipsDates**](CoursesRelationshipsDates.md) |  | [optional] 

## Example

```python
from jubladb_api.models.events_relationships import EventsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of EventsRelationships from a JSON string
events_relationships_instance = EventsRelationships.from_json(json)
# print the JSON string representation of the object
print(EventsRelationships.to_json())

# convert the object into a dict
events_relationships_dict = events_relationships_instance.to_dict()
# create an instance of EventsRelationships from a dict
events_relationships_from_dict = EventsRelationships.from_dict(events_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


