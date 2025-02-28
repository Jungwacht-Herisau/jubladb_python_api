# EventKindsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**EventKinds**](EventKinds.md) |  | [optional] 
**relationships** | [**EventKindsRelationships**](EventKindsRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kinds_resource import EventKindsResource

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindsResource from a JSON string
event_kinds_resource_instance = EventKindsResource.from_json(json)
# print the JSON string representation of the object
print(EventKindsResource.to_json())

# convert the object into a dict
event_kinds_resource_dict = event_kinds_resource_instance.to_dict()
# create an instance of EventKindsResource from a dict
event_kinds_resource_from_dict = EventKindsResource.from_dict(event_kinds_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


