# JsonapiRelationshipLinks

A resource object **MAY** contain references to other resource objects (\"relationships\"). Relationships may be to-one or to-many. Relationships can be specified by including a member in a resource's links object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_self** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 
**related** | [**JsonapiLink**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_relationship_links import JsonapiRelationshipLinks

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiRelationshipLinks from a JSON string
jsonapi_relationship_links_instance = JsonapiRelationshipLinks.from_json(json)
# print the JSON string representation of the object
print(JsonapiRelationshipLinks.to_json())

# convert the object into a dict
jsonapi_relationship_links_dict = jsonapi_relationship_links_instance.to_dict()
# create an instance of JsonapiRelationshipLinks from a dict
jsonapi_relationship_links_from_dict = JsonapiRelationshipLinks.from_dict(jsonapi_relationship_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


