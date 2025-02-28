# EventKindCategoriesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventKindCategoriesResource]**](EventKindCategoriesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kind_categories_collection import EventKindCategoriesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindCategoriesCollection from a JSON string
event_kind_categories_collection_instance = EventKindCategoriesCollection.from_json(json)
# print the JSON string representation of the object
print(EventKindCategoriesCollection.to_json())

# convert the object into a dict
event_kind_categories_collection_dict = event_kind_categories_collection_instance.to_dict()
# create an instance of EventKindCategoriesCollection from a dict
event_kind_categories_collection_from_dict = EventKindCategoriesCollection.from_dict(event_kind_categories_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


