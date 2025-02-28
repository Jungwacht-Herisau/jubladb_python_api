# EventKindCategoriesSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**EventKindCategoriesResource**](EventKindCategoriesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kind_categories_single import EventKindCategoriesSingle

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindCategoriesSingle from a JSON string
event_kind_categories_single_instance = EventKindCategoriesSingle.from_json(json)
# print the JSON string representation of the object
print(EventKindCategoriesSingle.to_json())

# convert the object into a dict
event_kind_categories_single_dict = event_kind_categories_single_instance.to_dict()
# create an instance of EventKindCategoriesSingle from a dict
event_kind_categories_single_from_dict = EventKindCategoriesSingle.from_dict(event_kind_categories_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


