# PersonNameRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PersonNameResource**](PersonNameResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.person_name_request import PersonNameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PersonNameRequest from a JSON string
person_name_request_instance = PersonNameRequest.from_json(json)
# print the JSON string representation of the object
print(PersonNameRequest.to_json())

# convert the object into a dict
person_name_request_dict = person_name_request_instance.to_dict()
# create an instance of PersonNameRequest from a dict
person_name_request_from_dict = PersonNameRequest.from_dict(person_name_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


