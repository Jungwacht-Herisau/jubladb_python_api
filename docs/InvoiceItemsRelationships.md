# InvoiceItemsRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | [**CoursesRelationshipsContact**](CoursesRelationshipsContact.md) |  | [optional] 

## Example

```python
from jubladb_api.models.invoice_items_relationships import InvoiceItemsRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItemsRelationships from a JSON string
invoice_items_relationships_instance = InvoiceItemsRelationships.from_json(json)
# print the JSON string representation of the object
print(InvoiceItemsRelationships.to_json())

# convert the object into a dict
invoice_items_relationships_dict = invoice_items_relationships_instance.to_dict()
# create an instance of InvoiceItemsRelationships from a dict
invoice_items_relationships_from_dict = InvoiceItemsRelationships.from_dict(invoice_items_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


