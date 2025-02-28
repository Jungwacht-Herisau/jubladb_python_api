# EventsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventsResource**](EventsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.events_request import EventsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsRequest from a JSON string
events_request_instance = EventsRequest.from_json(json)
# print the JSON string representation of the object
print(EventsRequest.to_json())

# convert the object into a dict
events_request_dict = events_request_instance.to_dict()
# create an instance of EventsRequest from a dict
events_request_from_dict = EventsRequest.from_dict(events_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


