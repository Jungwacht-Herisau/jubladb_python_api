# JsonapiLinkage

The \"type\" and \"id\" to non-empty members.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**Types**](Types.md) |  | 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**id** | **str** |  | 

## Example

```python
from jubladb_api.models.jsonapi_linkage import JsonapiLinkage

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiLinkage from a JSON string
jsonapi_linkage_instance = JsonapiLinkage.from_json(json)
# print the JSON string representation of the object
print(JsonapiLinkage.to_json())

# convert the object into a dict
jsonapi_linkage_dict = jsonapi_linkage_instance.to_dict()
# create an instance of JsonapiLinkage from a dict
jsonapi_linkage_from_dict = JsonapiLinkage.from_dict(jsonapi_linkage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


