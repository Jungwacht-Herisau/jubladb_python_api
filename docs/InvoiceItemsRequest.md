# InvoiceItemsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**InvoiceItemsResource**](InvoiceItemsResource.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoice_items_request import InvoiceItemsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItemsRequest from a JSON string
invoice_items_request_instance = InvoiceItemsRequest.from_json(json)
# print the JSON string representation of the object
print(InvoiceItemsRequest.to_json())

# convert the object into a dict
invoice_items_request_dict = invoice_items_request_instance.to_dict()
# create an instance of InvoiceItemsRequest from a dict
invoice_items_request_from_dict = InvoiceItemsRequest.from_dict(invoice_items_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


