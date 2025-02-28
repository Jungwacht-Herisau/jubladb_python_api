# EventKindsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventKindsResource**](EventKindsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kinds_request import EventKindsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindsRequest from a JSON string
event_kinds_request_instance = EventKindsRequest.from_json(json)
# print the JSON string representation of the object
print(EventKindsRequest.to_json())

# convert the object into a dict
event_kinds_request_dict = event_kinds_request_instance.to_dict()
# create an instance of EventKindsRequest from a dict
event_kinds_request_from_dict = EventKindsRequest.from_dict(event_kinds_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


