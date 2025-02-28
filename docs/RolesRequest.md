# RolesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RolesResource**](RolesResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.roles_request import RolesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RolesRequest from a JSON string
roles_request_instance = RolesRequest.from_json(json)
# print the JSON string representation of the object
print(RolesRequest.to_json())

# convert the object into a dict
roles_request_dict = roles_request_instance.to_dict()
# create an instance of RolesRequest from a dict
roles_request_from_dict = RolesRequest.from_dict(roles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


