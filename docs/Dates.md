# Dates

Date attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** |  | [optional] [readonly] 
**label** | **str** |  | [optional] [readonly] 
**location** | **str** |  | [optional] [readonly] 
**start_at** | **datetime** |  | [optional] [readonly] 
**finish_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from jubladb_api.models.dates import Dates

# TODO update the JSON string below
json = "{}"
# create an instance of Dates from a JSON string
dates_instance = Dates.from_json(json)
# print the JSON string representation of the object
print(Dates.to_json())

# convert the object into a dict
dates_dict = dates_instance.to_dict()
# create an instance of Dates from a dict
dates_from_dict = Dates.from_dict(dates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


