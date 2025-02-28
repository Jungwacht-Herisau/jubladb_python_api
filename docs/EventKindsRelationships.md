# EventKindsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind_category** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kinds_relationships import EventKindsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindsRelationships from a JSON string
event_kinds_relationships_instance = EventKindsRelationships.from_json(json)
# print the JSON string representation of the object
print(EventKindsRelationships.to_json())

# convert the object into a dict
event_kinds_relationships_dict = event_kinds_relationships_instance.to_dict()
# create an instance of EventKindsRelationships from a dict
event_kinds_relationships_from_dict = EventKindsRelationships.from_dict(event_kinds_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


