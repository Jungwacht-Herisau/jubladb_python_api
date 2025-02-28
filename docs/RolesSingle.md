# RolesSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**RolesResource**](RolesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.roles_single import RolesSingle

# TODO update the JSON string below
json = "{}"
# create an instance of RolesSingle from a JSON string
roles_single_instance = RolesSingle.from_json(json)
# print the JSON string representation of the object
print(RolesSingle.to_json())

# convert the object into a dict
roles_single_dict = roles_single_instance.to_dict()
# create an instance of RolesSingle from a dict
roles_single_from_dict = RolesSingle.from_dict(roles_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


