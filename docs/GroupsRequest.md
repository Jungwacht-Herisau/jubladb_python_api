# GroupsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsResource**](GroupsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.groups_request import GroupsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsRequest from a JSON string
groups_request_instance = GroupsRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsRequest.to_json())

# convert the object into a dict
groups_request_dict = groups_request_instance.to_dict()
# create an instance of GroupsRequest from a dict
groups_request_from_dict = GroupsRequest.from_dict(groups_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


