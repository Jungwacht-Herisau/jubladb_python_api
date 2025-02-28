# InvoicesCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InvoicesResource]**](InvoicesResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoices_collection import InvoicesCollection

# TODO update the JSON string below
json = "{}"
# create an instance of InvoicesCollection from a JSON string
invoices_collection_instance = InvoicesCollection.from_json(json)
# print the JSON string representation of the object
print(InvoicesCollection.to_json())

# convert the object into a dict
invoices_collection_dict = invoices_collection_instance.to_dict()
# create an instance of InvoicesCollection from a dict
invoices_collection_from_dict = InvoicesCollection.from_dict(invoices_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


