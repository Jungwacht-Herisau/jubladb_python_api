# EventsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Events**](Events.md) |  | [optional] 
**relationships** | [**EventsRelationships**](EventsRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.events_resource import EventsResource

# TODO update the JSON string below
json = "{}"
# create an instance of EventsResource from a JSON string
events_resource_instance = EventsResource.from_json(json)
# print the JSON string representation of the object
print(EventsResource.to_json())

# convert the object into a dict
events_resource_dict = events_resource_instance.to_dict()
# create an instance of EventsResource from a dict
events_resource_from_dict = EventsResource.from_dict(events_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


