# CoursesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CoursesResource**](CoursesResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.courses_request import CoursesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoursesRequest from a JSON string
courses_request_instance = CoursesRequest.from_json(json)
# print the JSON string representation of the object
print(CoursesRequest.to_json())

# convert the object into a dict
courses_request_dict = courses_request_instance.to_dict()
# create an instance of CoursesRequest from a dict
courses_request_from_dict = CoursesRequest.from_dict(courses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


