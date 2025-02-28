# JsonapiLinkOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | **str** | A string containing the link&#39;s URL. | 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 

## Example

```python
from jubladb_api.models.jsonapi_link_one_of import JsonapiLinkOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of JsonapiLinkOneOf from a JSON string
jsonapi_link_one_of_instance = JsonapiLinkOneOf.from_json(json)
# print the JSON string representation of the object
print(JsonapiLinkOneOf.to_json())

# convert the object into a dict
jsonapi_link_one_of_dict = jsonapi_link_one_of_instance.to_dict()
# create an instance of JsonapiLinkOneOf from a dict
jsonapi_link_one_of_from_dict = JsonapiLinkOneOf.from_dict(jsonapi_link_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


