# DatesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DatesResource]**](DatesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.dates_collection import DatesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DatesCollection from a JSON string
dates_collection_instance = DatesCollection.from_json(json)
# print the JSON string representation of the object
print(DatesCollection.to_json())

# convert the object into a dict
dates_collection_dict = dates_collection_instance.to_dict()
# create an instance of DatesCollection from a dict
dates_collection_from_dict = DatesCollection.from_dict(dates_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


