# PeopleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PeopleResource**](PeopleResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.people_request import PeopleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PeopleRequest from a JSON string
people_request_instance = PeopleRequest.from_json(json)
# print the JSON string representation of the object
print(PeopleRequest.to_json())

# convert the object into a dict
people_request_dict = people_request_instance.to_dict()
# create an instance of PeopleRequest from a dict
people_request_from_dict = PeopleRequest.from_dict(people_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


