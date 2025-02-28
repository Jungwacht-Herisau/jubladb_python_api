# Events

Event attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_ids** | **int** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**kind_id** | **int** |  | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**application_conditions** | **str** |  | [optional] [readonly] 
**motto** | **str** |  | [optional] [readonly] 
**cost** | **str** |  | [optional] [readonly] 
**location** | **str** |  | [optional] [readonly] 
**application_opening_at** | **date** |  | [optional] [readonly] 
**application_closing_at** | **date** |  | [optional] [readonly] 
**application_contact_id** | **int** |  | [optional] [readonly] 
**external_application_link** | **str** |  | [optional] [readonly] 
**maximum_participants** | **int** |  | [optional] [readonly] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.events import Events

# TODO update the JSON string below
json = "{}"
# create an instance of Events from a JSON string
events_instance = Events.from_json(json)
# print the JSON string representation of the object
print(Events.to_json())

# convert the object into a dict
events_dict = events_instance.to_dict()
# create an instance of Events from a dict
events_from_dict = Events.from_dict(events_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


