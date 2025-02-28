# GroupsCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GroupsResource]**](GroupsResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.groups_collection import GroupsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsCollection from a JSON string
groups_collection_instance = GroupsCollection.from_json(json)
# print the JSON string representation of the object
print(GroupsCollection.to_json())

# convert the object into a dict
groups_collection_dict = groups_collection_instance.to_dict()
# create an instance of GroupsCollection from a dict
groups_collection_from_dict = GroupsCollection.from_dict(groups_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


