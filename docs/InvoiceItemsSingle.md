# InvoiceItemsSingle


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InvoiceItemsResource**](InvoiceItemsResource.md) |  | [optional] 
**included** | [**List[JsonapiResource]**](JsonapiResource.md) | To reduce the number of HTTP requests, servers **MAY** allow responses that include related resources along with the requested primary resources. Such responses are called \&quot;compound documents\&quot;. | [optional] 
**meta** | **Dict[str, object]** | Non-standard meta-information that can not be represented as an attribute or relationship. | [optional] 
**links** | [**AdditionalEmailsSingleLinks**](AdditionalEmailsSingleLinks.md) |  | [optional] 
**jsonapi** | [**JsonapiJsonapi**](JsonapiJsonapi.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoice_items_single import InvoiceItemsSingle

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItemsSingle from a JSON string
invoice_items_single_instance = InvoiceItemsSingle.from_json(json)
# print the JSON string representation of the object
print(InvoiceItemsSingle.to_json())

# convert the object into a dict
invoice_items_single_dict = invoice_items_single_instance.to_dict()
# create an instance of InvoiceItemsSingle from a dict
invoice_items_single_from_dict = InvoiceItemsSingle.from_dict(invoice_items_single_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


