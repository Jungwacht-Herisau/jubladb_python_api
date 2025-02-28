# InvoiceItemsResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**InvoiceItems**](InvoiceItems.md) |  | [optional] 
**relationships** | [**InvoiceItemsRelationships**](InvoiceItemsRelationships.md) |  | [optional] 
**links** | [**Dict[str, JsonapiLink]**](JsonapiLink.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoice_items_resource import InvoiceItemsResource

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItemsResource from a JSON string
invoice_items_resource_instance = InvoiceItemsResource.from_json(json)
# print the JSON string representation of the object
print(InvoiceItemsResource.to_json())

# convert the object into a dict
invoice_items_resource_dict = invoice_items_resource_instance.to_dict()
# create an instance of InvoiceItemsResource from a dict
invoice_items_resource_from_dict = InvoiceItemsResource.from_dict(invoice_items_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


