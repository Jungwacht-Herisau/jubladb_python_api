# DatesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DatesResource**](DatesResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.dates_request import DatesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DatesRequest from a JSON string
dates_request_instance = DatesRequest.from_json(json)
# print the JSON string representation of the object
print(DatesRequest.to_json())

# convert the object into a dict
dates_request_dict = dates_request_instance.to_dict()
# create an instance of DatesRequest from a dict
dates_request_from_dict = DatesRequest.from_dict(dates_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


