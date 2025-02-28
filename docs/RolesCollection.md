# RolesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RolesResource]**](RolesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.roles_collection import RolesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of RolesCollection from a JSON string
roles_collection_instance = RolesCollection.from_json(json)
# print the JSON string representation of the object
print(RolesCollection.to_json())

# convert the object into a dict
roles_collection_dict = roles_collection_instance.to_dict()
# create an instance of RolesCollection from a dict
roles_collection_from_dict = RolesCollection.from_dict(roles_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


