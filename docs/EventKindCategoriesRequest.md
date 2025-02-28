# EventKindCategoriesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventKindCategoriesResource**](EventKindCategoriesResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kind_categories_request import EventKindCategoriesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindCategoriesRequest from a JSON string
event_kind_categories_request_instance = EventKindCategoriesRequest.from_json(json)
# print the JSON string representation of the object
print(EventKindCategoriesRequest.to_json())

# convert the object into a dict
event_kind_categories_request_dict = event_kind_categories_request_instance.to_dict()
# create an instance of EventKindCategoriesRequest from a dict
event_kind_categories_request_from_dict = EventKindCategoriesRequest.from_dict(event_kind_categories_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


