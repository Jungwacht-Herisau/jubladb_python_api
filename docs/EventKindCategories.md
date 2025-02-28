# EventKindCategories

Kind category attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] [readonly] 
**order** | **int** |  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.event_kind_categories import EventKindCategories

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindCategories from a JSON string
event_kind_categories_instance = EventKindCategories.from_json(json)
# print the JSON string representation of the object
print(EventKindCategories.to_json())

# convert the object into a dict
event_kind_categories_dict = event_kind_categories_instance.to_dict()
# create an instance of EventKindCategories from a dict
event_kind_categories_from_dict = EventKindCategories.from_dict(event_kind_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


