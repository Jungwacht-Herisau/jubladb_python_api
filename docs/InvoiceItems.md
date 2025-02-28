# InvoiceItems

Invoice item attributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**unit_cost** | **float** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**cost** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**cost_center** | **str** |  | [optional] 
**account** | **str** |  | [optional] 

## Example

```python
from jubladb_api.models.invoice_items import InvoiceItems

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItems from a JSON string
invoice_items_instance = InvoiceItems.from_json(json)
# print the JSON string representation of the object
print(InvoiceItems.to_json())

# convert the object into a dict
invoice_items_dict = invoice_items_instance.to_dict()
# create an instance of InvoiceItems from a dict
invoice_items_from_dict = InvoiceItems.from_dict(invoice_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


