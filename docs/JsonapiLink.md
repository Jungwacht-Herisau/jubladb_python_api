# JsonapiLink

A link **MUST** be represented as either: a string containing the link's URL or a link object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | A string containing the link&#39;s URL. | 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_link import JsonapiLink

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiLink from a JSON string
jsonapi_link_instance = JsonapiLink.from_json(json)
# print the JSON string representation of the object
print(JsonapiLink.to_json())

# convert the object into a dict
jsonapi_link_dict = jsonapi_link_instance.to_dict()
# create an instance of JsonapiLink from a dict
jsonapi_link_from_dict = JsonapiLink.from_dict(jsonapi_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


