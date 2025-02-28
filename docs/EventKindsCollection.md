# EventKindsCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[EventKindsResource]**](EventKindsResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.event_kinds_collection import EventKindsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of EventKindsCollection from a JSON string
event_kinds_collection_instance = EventKindsCollection.from_json(json)
# print the JSON string representation of the object
print(EventKindsCollection.to_json())

# convert the object into a dict
event_kinds_collection_dict = event_kinds_collection_instance.to_dict()
# create an instance of EventKindsCollection from a dict
event_kinds_collection_from_dict = EventKindsCollection.from_dict(event_kinds_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


