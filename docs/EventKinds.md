# EventKinds

Kind attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] [readonly] 
**short_name** | **str** |  | [optional] [readonly] 
**general_information** | **str** |  | [optional] [readonly] 
**application_conditions** | **str** |  | [optional] [readonly] 
**minimum_age** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.event_kinds import EventKinds

# TODO update the JSON string below
json = "{}"
# create an instance of EventKinds from a JSON string
event_kinds_instance = EventKinds.from_json(json)
# print the JSON string representation of the object
print(EventKinds.to_json())

# convert the object into a dict
event_kinds_dict = event_kinds_instance.to_dict()
# create an instance of EventKinds from a dict
event_kinds_from_dict = EventKinds.from_dict(event_kinds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


